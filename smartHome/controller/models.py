from django.db import models

class SensorData(models.Model):
    # timestamp = models.DateTimeField(auto_now_add=True)  # Remove this line
    temperature = models.FloatField()
    humidity = models.FloatField()
    brightness = models.FloatField()


    def __str__(self):
        return f"SensorData - Temp: {self.temperature}, Humidity: {self.humidity}, Brightness: {self.brightness}"


class SensorDataChoices(models.Model):
    temperature_choice = models.FloatField(default=0.0)  # Preferred temperature value
    humidity_choice = models.FloatField(default=0.0)  # Preferred humidity value
    brightness_choice = models.FloatField(default=0.0)  # Preferred brightness value

    def __str__(self):
        return f"Preferred Settings - Temp: {self.temperature_choice}, Humidity: {self.humidity_choice}, Brightness: {self.brightness_choice}"


class ActuatorControl(models.Model):
    MAIN_LED_CHOICES = [(0, 'Off'), (1, 'On')]
    HEATER_LED_CHOICES = [(0, 'Off'), (1, 'On')]
    FAN_CHOICES = [(0, 'Off'), (1, 'On')]
    SERVO_MOTOR_CHOICES = [(0, 'Locked'), (1, 'Unlocked')]
    MAIN_LED_MODE_CHOICES = [(0, 'Normal'), (1, 'cinema'), (2, 'military')]

    main_led_choice = models.IntegerField(choices=MAIN_LED_CHOICES, default=0)
    heater_led_choice = models.IntegerField(choices=HEATER_LED_CHOICES, default=0)
    fan_choice = models.IntegerField(choices=FAN_CHOICES, default=0)
    servo_motor_choice = models.IntegerField(choices=SERVO_MOTOR_CHOICES, default=0)
    main_led_mode_choice = models.IntegerField(choices=MAIN_LED_MODE_CHOICES, default=0)


    def __str__(self):
        return f"ActuatorControl - Main LED: {self.main_led_choice}, Heater LED: {self.heater_led_choice}, Fan: {self.fan_choice}, Servo Motor: {self.servo_motor_choice}, Main LED Mode: {self.main_led_mode_choice}"

class ActuatorStatus(models.Model):

    main_led_status = models.IntegerField(choices=ActuatorControl.MAIN_LED_CHOICES, default=0)
    heater_led_status = models.IntegerField(choices=ActuatorControl.HEATER_LED_CHOICES, default=0)
    fan_status = models.IntegerField(choices=ActuatorControl.FAN_CHOICES, default=0)
    servo_motor_status = models.IntegerField(choices=ActuatorControl.SERVO_MOTOR_CHOICES, default=0)


    def __str__(self):
        return f"ActuatorStatus - Main LED: {self.main_led_status}, Heater LED: {self.heater_led_status}, Fan: {self.fan_status}, Servo Motor: {self.servo_motor_status}"


class ThresholdSettings(models.Model):
    temperature_threshold_min = models.FloatField(default=18.0)
    temperature_threshold_max = models.FloatField(default=30.0)
    humidity_threshold_min = models.FloatField(default=30.0)
    humidity_threshold_max = models.FloatField(default=60.0)
    brightness_threshold_min = models.FloatField(default=200)

    def __str__(self):
        return f"ThresholdSettings - Temp: {self.temperature_threshold_min} to {self.temperature_threshold_max}, Humidity: {self.humidity_threshold_min} to {self.humidity_threshold_max}, Brightness: {self.brightness_threshold_min}"
