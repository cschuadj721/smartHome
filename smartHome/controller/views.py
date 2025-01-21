import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import SensorData, ActuatorControl, ThresholdSettings, SensorDataChoices, ActuatorStatus

@csrf_exempt
def index(request):
    # Get the latest sensor data (we no longer have the timestamp field)
    sensor_data = SensorData.objects.first()  # Get the first available entry

    # Get actuator control data
    actuator_control = ActuatorControl.objects.first()

    # Get threshold settings
    thresholds = ThresholdSettings.objects.first()

    context = {
        'sensor_data': sensor_data,
        'actuator_control': actuator_control,
        'thresholds': thresholds
    }
    return render(request, 'controller/index.html', context)


def get_actuator_status(request):
    try:
        # Fetch the actuator control data (assuming there's only one row in the table)
        actuator_status = ActuatorStatus.objects.first()

        if not actuator_status:
            return JsonResponse({'status': 'failure', 'message': 'No actuator control data found'}, status=404)

        # Prepare data for the response based on the new model and field names
        data = {
            'acStatus': 'ON' if actuator_status.fan_status else 'OFF',
            'lightStatus': 'ON' if actuator_status.main_led_status else 'OFF',
            'lockStatus': 'LOCKED' if actuator_status.servo_motor_status == 0 else 'UNLOCKED',
            'boilerStatus': 'ON' if actuator_status.heater_led_status else 'OFF'
        }

        return JsonResponse(data)

    except Exception as e:
        return JsonResponse({'status': 'failure', 'message': str(e)}, status=500)

def get_last_60_sensor_data(request):
    # Fetch the last 600 sensor data entries (no longer ordered by timestamp)
    sensor_data = SensorData.objects.all().order_by('-id')[:60]  # Using 'id' as a fallback for ordering

    # Prepare the data to send back to the frontend
    data = {
        'labels': [i for i in range(len(sensor_data))],
        'temperature': [entry.temperature for entry in sensor_data],
        'humidity': [entry.humidity for entry in sensor_data],
    }

    return JsonResponse(data)

def get_latest_sensor_data(request):
    # Fetch the latest sensor data entry (no longer ordered by timestamp)
    latest_data = SensorData.objects.first()  # Get the first entry

    # Return the latest data as JSON
    if latest_data:
        data = {
            'temperature': latest_data.temperature,
            'humidity': latest_data.humidity,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'status': 'failure', 'message': 'No sensor data available'}, status=400)

@csrf_exempt
def update_actuator(request):
    """
    Accepts JSON data with exactly one of the following fields:
      {
        "main_led": 0 or 1,
        "heater_led": 0 or 1,
        "fan": 0 or 1,
        "servo_motor": 0 or 1
        "main_led_mode": 0, 1, or 2 (for normal, cinema, or military modes)
      }
    and updates ONLY that field in the database.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            # Fetch or create the single actuator control row
            actuator_control, _ = ActuatorControl.objects.get_or_create(pk=1)

            # Update only the field provided in the POST data.
            if 'main_led' in data:
                actuator_control.main_led_choice = data['main_led']

            if 'heater_led' in data:
                actuator_control.heater_led_choice = data['heater_led']

            if 'fan' in data:
                actuator_control.fan_choice = data['fan']

            if 'servo_motor' in data:
                actuator_control.servo_motor_choice = data['servo_motor']

            if 'main_led_mode' in data:
                actuator_control.main_led_mode_choice = data['main_led_mode']


            # Save updates
            actuator_control.save()

            return JsonResponse({'status': 'success'}, status=200)

        except Exception as e:
            return JsonResponse({'status': 'failure', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'failure', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def update_sensor_choice(request):
    """
    Accepts JSON data with temperature_choice and/or humidity_choice,
    and updates the corresponding fields in the SensorDataChoices model.
    """
    if request.method == 'POST':
        try:
            # Get the data from the request body
            data = json.loads(request.body.decode('utf-8'))

            # Get or create the SensorDataChoices row (pk=1 means it's the only row)
            sensor_choices, created = SensorDataChoices.objects.get_or_create(pk=1)

            # Check for each field and update only if it's provided
            if 'temperature_choice' in data:
                sensor_choices.temperature_choice = data['temperature_choice']

            if 'humidity_choice' in data:
                sensor_choices.humidity_choice = data['humidity_choice']

            if 'brightness_choice' in data:
                sensor_choices.brightness_choice = data['brightness_choice']

            # Save the updated choices
            sensor_choices.save()

            return JsonResponse({'status': 'success'}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'status': 'failure', 'message': 'Invalid JSON data'}, status=400)
        except KeyError as e:
            return JsonResponse({'status': 'failure', 'message': f'Missing key: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'failure', 'message': f'Error: {str(e)}'}, status=500)

    return JsonResponse({'status': 'failure', 'message': 'Invalid request method'}, status=400)

@csrf_exempt  # Disable CSRF protection for this view if needed (use only if necessary)
def update_brightness(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            brightness = data.get('brightness')  # Extract brightness value

            # Update the actuator status with the new brightness value
            actuator_status = ActuatorStatus.objects.first()  # Assuming one actuator status object
            if actuator_status:
                actuator_status.brightness = brightness  # Update brightness field
                actuator_status.save()

            return JsonResponse({'status': 'success', 'brightness': brightness})
        except Exception as e:
            return JsonResponse({'status': 'failure', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'failure', 'message': 'Invalid method'}, status=400)

@csrf_exempt  # Disable CSRF protection for this view if needed (use only if necessary)
def change_light_mode(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse incoming JSON data
            mode = data.get('mode')  # Extract the mode value (normal, cinema, military)

            # Assuming you store mode in actuator status or handle it in another way
            actuator_status = ActuatorStatus.objects.first()  # Assuming one actuator status object
            if actuator_status:
                actuator_status.light_mode = mode  # Update the light mode
                actuator_status.save()

            return JsonResponse({'status': 'success', 'mode': mode})
        except Exception as e:
            return JsonResponse({'status': 'failure', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'failure', 'message': 'Invalid method'}, status=400)