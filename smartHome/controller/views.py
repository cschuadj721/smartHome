import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import SensorData, ActuatorControl, ThresholdSettings, SensorDataChoices

@csrf_exempt
def index(request):
    # Get the latest sensor data
    sensor_data = SensorData.objects.order_by('-timestamp').first()

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


@csrf_exempt
def update_actuator(request):
    """
    Accepts JSON data with exactly one of the following fields:
      {
        "main_led": 0 or 1,
        "heater_led": 0 or 1,
        "fan": 0 or 1,
        "servo_motor": 0 or 1
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
