from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    brightness = models.FloatField()

    class Meta:
        managed = False  # Tells Django not to manage this table (no migrations)
        db_table = 'controller_sensordata'  # Ensure this matches the table name in the database

    def __str__(self):
        return f"SensorData at {self.timestamp} - Temp: {self.temperature}, Humidity: {self.humidity}, Brightness: {self.brightness}"

class ActuatorControl(models.Model):
    MAIN_LED_CHOICES = [(0, 'Off'), (1, 'On')]
    HEATER_LED_CHOICES = [(0, 'Off'), (1, 'On')]
    FAN_CHOICES = [(0, 'Off'), (1, 'On')]
    SERVO_MOTOR_CHOICES = [(0, 'Locked'), (1, 'Unlocked')]

    main_led_choice = models.IntegerField(choices=MAIN_LED_CHOICES, default=0)
    heater_led_choice = models.IntegerField(choices=HEATER_LED_CHOICES, default=0)
    fan_choice = models.IntegerField(choices=FAN_CHOICES, default=0)
    servo_motor_choice = models.IntegerField(choices=SERVO_MOTOR_CHOICES, default=0)
    main_led_status = models.IntegerField(choices=MAIN_LED_CHOICES, default=0)
    heater_led_status = models.IntegerField(choices=HEATER_LED_CHOICES, default=0)
    fan_status = models.IntegerField(choices=FAN_CHOICES, default=0)
    servo_motor_status = models.IntegerField(choices=SERVO_MOTOR_CHOICES, default=0)

    class Meta:
        managed = False  # Tells Django not to manage this table (no migrations)
        db_table = 'controller_actuatorcontrol'  # Ensure this matches the table name in the database

    def __str__(self):
        return f"ActuatorControl - Main LED: {self.main_led_choice} (Choice), {self.main_led_status} (Status), Heater LED: {self.heater_led_choice} (Choice), {self.heater_led_status} (Status), Fan: {self.fan_choice} (Choice), {self.fan_status} (Status), Servo Motor: {self.servo_motor_choice} (Choice), {self.servo_motor_status} (Status)"

class ThresholdSettings(models.Model):
    temperature_threshold_min = models.FloatField(default=18.0)
    temperature_threshold_max = models.FloatField(default=30.0)
    humidity_threshold_min = models.FloatField(default=30.0)
    humidity_threshold_max = models.FloatField(default=60.0)
    brightness_threshold_min = models.FloatField(default=200)

    def __str__(self):
        return f"ThresholdSettings - Temp: {self.temperature_threshold_min} to {self.temperature_threshold_max}, Humidity: {self.humidity_threshold_min} to {self.humidity_threshold_max}, Brightness: {self.brightness_threshold_min}"
