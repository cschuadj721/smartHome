from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Main index page
    path('update_actuator', views.update_actuator, name='update_actuator'),
    path('update_sensor_choice', views.update_sensor_choice, name='update_sensor_choice'),
    path('get_last_60_sensor_data', views.get_last_60_sensor_data, name='get_last_60_sensor_data'),
    path('get_latest_sensor_data', views.get_latest_sensor_data, name='get_latest_sensor_data'),
    path('get_actuator_status', views.get_actuator_status, name='get_actuator_status'),
    path('update-brightness/', views.update_brightness, name='update_brightness'),
    path('change-light-mode/', views.change_light_mode, name='change_light_mode'),

    # path('toggle_emergency', views.toggle_emergency, name='toggle_emergency'),
    # path('move_up', views.move_up, name='move_up'),
    # path('move_down', views.move_down, name='move_down'),
    # path('stop_elevator', views.stop_elevator, name='stop_elevator'),
    # path('status', views.status, name='status'),  # Add the status path here
]