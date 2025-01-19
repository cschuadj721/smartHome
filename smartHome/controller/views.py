from django.http import JsonResponse
# from .models import Controller
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import SensorData, ActuatorControl, ThresholdSettings

def index(request):
    # # Get the latest sensor data
    # sensor_data = SensorData.objects.order_by('-timestamp').first()
    #
    # # Get actuator control data (you can modify this to fetch specific control data as needed)
    # actuator_control = ActuatorControl.objects.first()
    #
    # # Fetch threshold settings
    # thresholds = ThresholdSettings.objects.first()
    #
    # if request.method == 'POST':
    #     # Manual control of actuators via POST requests (e.g., turning on the main LED)
    #     if 'main_led' in request.POST:
    #         actuator_control.main_led = int(request.POST['main_led'])
    #     if 'heater_led' in request.POST:
    #         actuator_control.heater_led = int(request.POST['heater_led'])
    #     if 'fan' in request.POST:
    #         actuator_control.fan = int(request.POST['fan'])
    #     if 'servo_motor' in request.POST:
    #         actuator_control.servo_motor = int(request.POST['servo_motor'])
    #     actuator_control.save()
    #
    # context = {
    #     'sensor_data': sensor_data,
    #     'actuator_control': actuator_control,
    #     'thresholds': thresholds
    # }
    # return render(request, 'controller/index.html', context)
   return render(request, 'controller/index.html')