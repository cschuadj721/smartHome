## 아래 내용은 클라우드 서버가 존재하며, 웹호스팅 서비스를 통해 웹사이트 주소가 존재한다는 가정하에 작성함 (해당 주소 및 서버 정보는 자신의 것으로 수정해서 적용 할것)

[스마트홈 안드로이드 앱 만들기 노트](https://www.notion.so/1844bd4c6166804087fcd68965c62604?pvs=21) 

pycharm  실행

새 pycharm 프로젝트 생성

터미널 실행 (VENV 가상환경 활성화 체크)

django 라이브러리 설치

```c
pip insatll django       
```

django 프로젝트 생성 (프로젝트명: myproject)

```c
 django-admin startproject smartHome
```

이때 주의할 사항!

여기서 최상단의 smartHome은 파이참에서 새 프로젝트 생성시 입력한 프로젝트 명이고

그 바로 아래의 smartHome은 위의 django 프로젝트 생성에서 생성된 프로젝트명이다. (자동생성)

그리고 또 그 아래의 smartHome은 django 프로젝트의 기본값이 설정되어있는 폴더이다. (자동생성)

따라서 파이참에서 smartHome으로 프로젝트를 생성하고 장고프로젝트를 같은이름으로 생성하면 똑같은 이름의 폴더가

smartHome/smartHome/smartHome 이렇게 세개까지 생기게 된다.

이렇게 되면 혼동이 생길수도 있기때문에, 일반적으로 파이참 프로젝트명과, 장고 프로젝트명을 다르게 만들기도 한다.

 

아래 폴더 구조 이미지 참고

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/21ea20c3-ecf7-4b88-88f4-e7a965f9d121/9d3afe57-f541-453d-b554-68e4a1c2cd60/image.png)

프로젝트 폴더로 이동

```jsx
cd smarthome

(.venv) PS C:\pythonWorks\smartHome\smartHome>
```

위의 폴더로 이동 한뒤 장고 웹앱 설치 (웹앱이름 controller) 

이 때 생성되는 앱이 실제 보여지는 화면과 기능을 담당한다

만일 다른 추가적인 화면과 기능이 필요하다면 또다른 app을 만들면된다.

현재 프로젝트에서는 controller 라는 app 하나만 생성했음

```c
python manage.py startapp controller
```

smartHome/smartHome/smartHome/setting.py 에 앱 리스트에 controller 추가

```c
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'controller',  # 추가된 라인
]
```

smartHome/smartHome/smartHome/urls.py 에 다음 내용 추가

이렇게 설정하면 웹주소를 입력하면 controller의 화면으로 자동으로 연결된다.

```c
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('controller.urls')),  # 앞에서 생성한 앱의 주소 입력

]

```

smartHome/smartHome/controller폴더에 [url.py](http://url.py) 파일 생성 후 아래 코드 추가

아래의 코드들은 controller 웹앱의 모든 파이선 함수정보들을 갖는다.

아래에 함수정보를 입력해놓지 않으면 웹에서 기능이 작동하지 않는다.

작동방식은 api 호출 방식을 사용하며 그리고 이 api들은 외부 앱(인터넷브라우저, 안드로이드 앱, 컴퓨터의 파이선앱) 등에서도 호출해서 사용할 수 있게된다. 

외부에서 사용하려면 추가적으로 외부접근을 허용해주어야 한다.

```jsx
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
```

외부접근 허용 코드 (settings.py)

```c
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'controller',
    'corsheaders', # 이 라인 추가

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware', # 이 라인 추가

]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

CORS_ALLOW_ALL_ORIGINS = True # 이 라인 추가

```

myApp폴더에 [view.py](http://view.py) 파일에 아래 코드 추가

```jsx
from django.shortcuts import render

def index(request):
    return render(request, 'controller/index.html')
```

서버테스트(로컬 테스트)

```c
python manage.py runserver
```

## 앱의 화면 만들기

웹앱폴더 안에 templates라는 폴더 만들기

이 폴더안에 웹앱과 동일한이름의 폴더를 만들기

그 안에 index.html이라는 파일 생성하고 그안에 화면의 html 내용 입력하기

아래는 예시 코드

```jsx
# classifier/views.py

from django.shortcuts import render
from django.apps import apps
from .custom_layers import AttentionWeightedSum, ReduceSumCustom

def index(request):
    prediction = None
    if request.method == 'POST':
        review = request.POST.get('review', '')
        if review.strip():
            # Access the loaded model and resources from AppConfig
            classifier_config = apps.get_app_config('classifier')

            model = classifier_config.model
            tokenizer = classifier_config.tokenizer
            label_encoder = classifier_config.label_encoder
            max_length = classifier_config.max_length

            if model:
                # Preprocess the review
                from nltk.tokenize import word_tokenize
                from nltk.corpus import stopwords
                from nltk.stem import WordNetLemmatizer
                import numpy as np
                from tensorflow.keras.preprocessing.sequence import pad_sequences

                lemmatizer = WordNetLemmatizer()
                stop_words = set(stopwords.words('english'))

                def preprocess_text(sentence):
                    tokens = word_tokenize(sentence)
                    tokens = [word.lower() for word in tokens if word.isalpha()]
                    tokens = [word for word in tokens if word not in stop_words]
                    tokens = [lemmatizer.lemmatize(word) for word in tokens]
                    return ' '.join(tokens)

                preprocessed_review = preprocess_text(review)

                # Convert to sequence
                sequence = tokenizer.texts_to_sequences([preprocessed_review])

                # Pad sequence
                padded_sequence = pad_sequences(sequence, maxlen=max_length, padding='post')

                # Predict
                prediction_prob = model.predict(padded_sequence)
                predicted_index = np.argmax(prediction_prob, axis=1)
                predicted_genre = label_encoder.inverse_transform(predicted_index)[0]

                prediction = predicted_genre
            else:
                prediction = "Model not loaded."
        else:
            prediction = "Please enter a valid review."

    return render(request, 'classifier/index.html', {'prediction': prediction})

```

## DB 생성하기

먼저 DB 구조를 정의 한다 (models.py)

아래는 smarthome예시 코드

```python
from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    brightness = models.FloatField()

    def __str__(self):
        return f"SensorData at {self.timestamp} - Temp: {self.temperature}, Humidity: {self.humidity}, Brightness: {self.brightness}"

class ActuatorControl(models.Model):
    MAIN_LED_CHOICES = [(0, 'Off'), (1, 'On')]
    HEATER_LED_CHOICES = [(0, 'Off'), (1, 'On')]
    FAN_CHOICES = [(0, 'Off'), (1, 'On')]
    SERVO_MOTOR_CHOICES = [(0, 'Locked'), (1, 'Unlocked')]

    main_led_choice = models.IntegerField(choices=MAIN_LED_CHOICES, default=0)  # remote choice
    heater_led_choice = models.IntegerField(choices=HEATER_LED_CHOICES, default=0)  # remote choice
    fan_choice = models.IntegerField(choices=FAN_CHOICES, default=0)  # remote choice
    servo_motor_choice = models.IntegerField(choices=SERVO_MOTOR_CHOICES, default=0)  # remote choice

    main_led_status = models.IntegerField(choices=MAIN_LED_CHOICES, default=0)  # actual status
    heater_led_status = models.IntegerField(choices=HEATER_LED_CHOICES, default=0)  # actual status
    fan_status = models.IntegerField(choices=FAN_CHOICES, default=0)  # actual status
    servo_motor_status = models.IntegerField(choices=SERVO_MOTOR_CHOICES, default=0)  # actual status

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

```

DB와 유저를 생성한다 (ubuntu postgres 기준) ( 이미 만들었으면 패스)

```python
sudo -u postgres psql

#이하 postgres 쿼리
CREATE DATABASE smarthomedb;

#아이디: abcd , 비번:1234
CREATE USER aaaa WITH PASSWORD '1111';

GRANT ALL PRIVILEGES ON DATABASE smarthomedb TO abcd;

```

setting.py에 DB 와 user 정보를 입력한다

아래는 예시 코드

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'smarthomedb',
        'USER': 'aaaa',  # Replace with your actual DB user
        'PASSWORD': '1111',  # Replace with your actual DB password
        'HOST': '111.111.11.111',  # Your DB IP
        'PORT': '5432',
    }
}
```

# 테이블 생성

정의된 모델을 터미널에서 migrate(생성) 시킨다

makemigrations와 migrate는 위에서 정의된 table 정보와 DB정보를 활용하여 자동으로 DB에 테이블들을 생성한다.

**주의사항: 만일 model.py에서 수정이 일어나거나, DB의 테이블구조에 수정이 일어난 경우 불일치로 인해 오작동 할 수 있기때문에, 만일 수정이 일어난 경우 DB를 삭제한 후 다시 만들어 준뒤 다시 아래 코드들을 실행하여 다시 만들어 주어야 할 수도 있다. 어떤때는 아래코드만 입력하면 table들이 자동 수정되는 경우도 있다. 

일단 아래 코드를 입력해보고 변경사항이 적용되는지 안되는지 파악한 후 적용이 되지 않거나, 에러가 발생하면 DB를 삭제하고 다시 만들어 시도해 본다.

```python
(.venv) PS C:\pythonWorks\smartHome\smartHome>

python manage.py makemigrations

python manage.py migrate

```

# 앱의 기능을 담당하는 최고 핵심 코드

## controller/views.py

```python
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import SensorData, ActuatorControl, ThresholdSettings, SensorDataChoices, ActuatorStatus

# 최초화면 뿌려주는 함수
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

# 현재 센서 on/off 상태 DB에서 불러오는 함수
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

# 최근 60개의 온습도 데이터 DB에서 불러오는 함수 (그래프 그리기 용도) 
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

# 화면에서 ON/OFF 버튼 누를때 상태 변환 시키는 함수
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

# 앱에서 온습도 설정 바꾸는 경우 값 DB에 전달하는 함수
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

            # Function to round to the nearest 0.5
            def round_to_half(value):
                return round(value * 2) / 2

            # Check for each field and update only if it's provided
            if 'temperature_choice' in data:
                sensor_choices.temperature_choice = round_to_half(data['temperature_choice'])

            if 'humidity_choice' in data:
                sensor_choices.humidity_choice = round_to_half(data['humidity_choice'])

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

# 밝기 값 변환하는 경우 DB에 전달하는 함수
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

# 조명 모드 변환하는 경우 DB에 전달하는 함수
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
```

# 화면 만들기

controller 폴더 아래에 template 폴더 생성

templates 폴더 아래에 controller 폴더 생성 (app이름과 일치시켜야함! 프로젝트이름아님!)

controller 폴더에 index.html 파일 생성

index.html (smartHome  예시코드)

```python
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Smart Environment Control</title>

    <!-- CSRF token in meta tag -->
  <meta name="csrf-token" content="{{ csrf_token }}">

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet"/>

  <!-- Bootstrap 4.5.2 -->
  <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet"/>

  <!-- FontAwesome -->
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet"/>

  <!-- jQuery UI CSS (for draggable) -->
  <link rel="stylesheet" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css"/>

  <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>스마트 홈 컨트롤 프로그램</title>

  <!-- Bootstrap CSS (adjust version if needed) -->
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/css/bootstrap.min.css"
  />

  <style>
    body {
      font-family: 'Roboto', sans-serif;
      background-color: #f4f7fc;
    }

    .container {
      max-width: 1200px;
      margin-top: 50px;
    }

    h1 {
      font-size: 2.5rem;
      color: #333;
      font-weight: 700;
    }

    .card {
      margin-top: 0px;
      border-radius: 15px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }

    .card-body {
      padding: 30px;
    }

    .card-title {
      font-size: 1.8rem;
      color: #555;
      font-weight: 600;
    }

    .control-panel {
      margin-top: 0px;
    }

    .footer {
      background-color: #343a40;
      color: white;
      padding: 20px;
      text-align: center;
      font-size: 1rem;
      margin-top: 50px;
    }
    .footer a {
      color: #17a2b8;
      text-decoration: none;
    }

    /* Graph Container */
    .graph-container {
      width: 100%;
      height: 400px;
      position: relative; /* for absolutely-positioned elements */
    }

    /* Horizontal lines */
    .horizontal-line {
      position: absolute;
      left: 0;
      width: 100%;
      height: 2px;
      background-color: #ff6347;
      pointer-events: none; /* so clicks pass through to handle */
    }
    .humidity-line {
      background-color: #ff69b4;
    }

    /* Circular handles */
    .temp-handle,
    .humidity-handle {
      position: absolute;
      width: 30px;
      height: 30px;
      border-radius: 50%;
      top: 100px; /* default position */
      cursor: move;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
    }
    .temp-handle {
      background-color: #ff6347;
      left: -15px; /* half the handle's width outside the container for nice look */
    }
    .humidity-handle {
      background-color: #ff69b4;
      right: -15px;
    }

    /* Device control buttons */
    .control-panel button {
      width: 100%;
      padding: 15px;
      font-size: 1.2rem;
      border-radius: 10px;
      border: none;
      transition: background-color 0.3s ease;
      margin-bottom: 10px;
    }
    .control-panel button:hover {
      background-color: #007bff;
      color: #fff;
    }

    /* Status panel */
    .status-panel {
      margin-top: 0px; /* Some spacing from the card above */
      padding: 0px;
    }

    /* Example styling for horizontal status items */
    .status-item {
      text-align: center;
      border-right: 1px solid #ddd;
      padding: 0px 0;
    }
    /* Remove right border on last item */
    .status-item:last-child {
      border-right: none;
    }
  </style>
</head>
<body>
  <div class="container">
    <!-- Header -->
    <header class="text-center">
      <h1>스마트 홈 컨트롤 프로그램</h1>
      <p class="lead text-muted">Control and monitor the temperature, humidity, and actuators for a comfortable environment.</p>
    </header>

    <!-- Main Content Row -->
<div class="row">
  <!-- Left Panel: Graph and Status -->
  <div class="col-md-8 mb-4">
    <!-- '온도/습도 변화 (1시간)' Card -->
    <div class="card">
      <div class="card-body">
        <h4 class="card-title">온도/습도 변화 (1시간)</h4>
        <div class="graph-container">
          <!-- Chart.js Canvas -->
          <canvas id="realTimeGraph"></canvas>

          <!-- Temperature line + handle -->
          <div id="tempLine" class="horizontal-line" style="top:100px;"></div>
          <div id="tempHandle" class="temp-handle"></div>

          <!-- Humidity line + handle -->
          <div id="humidLine" class="horizontal-line humidity-line" style="top:200px;"></div>
          <div id="humidHandle" class="humidity-handle"></div>
        </div>
      </div>
    </div>

    <!-- '현재 상태' Card -->
    <div class="card status-panel mt-4">
      <div class="card-body">
        <h5 class="card-title">현재 상태</h5>
        <!-- Display 4 statuses horizontally -->
        <div class="row">
          <div class="col-md-3 status-item">
            <strong>에어컨</strong>
            <div id="acStatus">{{ fan_status_text }}</div>
          </div>
          <div class="col-md-3 status-item">
            <strong>거실등</strong>
            <div id="lightStatus">{{ main_led_status_text }}</div>
          </div>
          <div class="col-md-3 status-item">
            <strong>현관문 잠금</strong>
            <div id="lockStatus">{{ servo_motor_status_text }}</div>
          </div>
          <div class="col-md-3 status-item">
            <strong>보일러</strong>
            <div id="boilerStatus">{{ heater_led_status_text }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Right Panel: Device Control and Lighting Settings -->
  <div class="col-md-4 mb-4">
    <!-- '원격 제어' Card -->
    <div class="card control-panel">
      <div class="card-body">
        <h4 class="card-title">원격 제어</h4>
        <button id="acToggle" class="btn btn-success btn-lg">에어컨 ON/OFF</button>
        <button id="lightToggle" class="btn btn-danger btn-lg">거실등 ON/OFF</button>
        <button id="lockToggle" class="btn btn-warning btn-lg">현관문 잠금/해제</button>
        <button id="boilerToggle" class="btn btn-info btn-lg">보일러 ON/OFF</button>
      </div>
    </div>

    <!-- '조명 설정' Card -->

    <div class="card mt-3">
      <div class="card-body">
        <h4 class="card-title">조명 밝기</h4>
        <!-- Add your lighting control options here -->
        <input type="range" id="brightnessSlider" class="form-control-range" min="0" max="100" value="50" oninput="updateBrightnessValue(this.value)">
        <p>밝기: <span id="brightnessValue">50</span>%</p>
      </div>
    </div>

    <div class="card mt-3">
      <div class="card-body">
        <h4 class="card-title">조명 모드</h4>
        <!-- Add your lighting control options here -->
        <button id="normalMode" class="btn btn-primary btn-lg btn-block" onclick="setLightingMode('normal')">노멀모드</button>
        <button id="cinemaMode" class="btn btn-dark btn-lg btn-block" onclick="setLightingMode('cinema')">시네마모드</button>
        <button id="militaryMode" class="btn btn-success btn-lg btn-block" onclick="setLightingMode('military')">군대모드</button>
      </div>
    </div>
  </div>
</div>

    <!-- Footer -->
    <div class="footer">
      <p>&copy; 2025 Smart Environment Control System. Built with
        <a href="https://www.djangoproject.com/" target="_blank">Django</a>
        and <a href="https://www.python.org/" target="_blank">Python</a>.
      </p>
    </div>
  </div>

  <!-- JS Libraries -->
  <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <script>
    ////////////////////////////////////////////////////////////////////////////
    // 1. Setup Chart.js with two Y-axes (temp / humidity) using numeric x-axis
    ////////////////////////////////////////////////////////////////////////////
    const ctx = document.getElementById('realTimeGraph').getContext('2d');
    let xIndex = 600;  // Start at 600 to simulate the last 5 minutes (600 x 0.5s = 5 minutes)

    // Chart.js initial setup
    const realTimeGraph = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],  // Empty initially, will populate with the last 600 timestamps
            datasets: [
                {
                    label: 'Temperature (°C)',
                    yAxisID: 'tempAxis',
                    borderColor: 'rgb(255, 99, 132)',
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    data: [],
                    fill: true
                },
                {
                    label: 'Humidity (%)',
                    yAxisID: 'humidAxis',
                    borderColor: 'rgb(54, 162, 235)',
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    data: [],
                    fill: true
                }
            ]
        },
        options: {
            responsive: true,
            animation: false,
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom',
                    min: 0,
                    max: 60, // Display last 600 data points (5 minutes)
                    title: {
                        display: true,
                        text: 'interval (1 minute steps)'
                    }
                },
                tempAxis: {
                    type: 'linear',
                    position: 'left',
                    min: 0,
                    max: 40,
                    title: {
                        display: true,
                        text: 'Temperature (°C)'
                    }
                },
                humidAxis: {
                    type: 'linear',
                    position: 'right',
                    min: 0,
                    max: 100,
                    title: {
                        display: true,
                        text: 'Humidity (%)'
                    },
                    grid: {
                        drawOnChartArea: false
                    }
                }
            }
        }
    });

    // Fetch the initial last 60 data points from the backend
    function updateLastGraph() {
        fetch('/get_last_60_sensor_data')
            .then(response => response.json())
            .then(data => {
                // Set the initial data points
                realTimeGraph.data.labels = data.labels;
                realTimeGraph.data.datasets[0].data = data.temperature;
                realTimeGraph.data.datasets[1].data = data.humidity;
                realTimeGraph.update();
            });
    }

    setInterval(updateLastGraph, 3000); // 1 minute update

    ////////////////////////////////////////////////////////////////////////////
    // 3. Draggable Horizontal Lines
    ////////////////////////////////////////////////////////////////////////////
    // We'll constrain the handles so that they can't go outside the .graph-container,
    // and keep the line in sync with the handle's Y-position.

    // Helper to clamp a value between min and max
    function clamp(val, min, max) {
      return Math.max(min, Math.min(max, val));
    }

    const chartHeight = 400;  // The .graph-container is 400px high
    const marginTop = 30;     // Set top margin (adjust as needed)
    const marginBottom = -130;  // Set bottom margin (adjust as needed)

// --- Temperature line/handle ---
$('#tempHandle').draggable({
  axis: 'y',
  containment: [
    0,                          // Left edge (no left margin needed)
    marginTop,                  // Top margin
    0,                          // Right edge (no right margin needed)
    chartHeight - marginBottom  // Bottom margin
  ], // This confines the handle within the graph area, including margins
  drag: function(event, ui) {
    // Ensure the handle stays within the defined containment area
    const handleHeight = 30;
    ui.position.top = clamp(ui.position.top, marginTop, chartHeight - marginBottom - handleHeight);

    // Move line to the same Y position
    $('#tempLine').css('top', ui.position.top + 'px');

    // Convert pixel to temperature (roughly 0°C @ bottom to 40°C @ top)
    const maxTemp = 40; // Maximum temperature value (Top = 40°C)
    const minTemp = -34;  // Minimum temperature value (Bottom = 0°C)

    // Calculate the range of the graph that corresponds to the temperature scale
    const graphRange = chartHeight - marginTop - marginBottom;

    // Invert the scale, so top = 40°C, bottom = 0°C
    const tempValue = maxTemp - ((ui.position.top - marginTop) / graphRange) * (maxTemp - minTemp);
    console.log('Target Temperature: ' + tempValue.toFixed(1) + '°C');

    // Send the updated temperature choice to the server
    updateSensorChoice('temperature_choice', tempValue);
  }
});

// Keep the initial alignment of the temperature line and handle
$('#tempLine').css('top', $('#tempHandle').position().top + 'px');

// --- Humidity line/handle ---
$('#humidHandle').draggable({
  axis: 'y',
  containment: [
    0,                          // Left edge (no left margin needed)
    marginTop,                  // Top margin
    0,                          // Right edge (no right margin needed)
    chartHeight - marginBottom  // Bottom margin
  ], // This confines the handle within the graph area, including margins
  drag: function(event, ui) {
    const handleHeight = 30;
    ui.position.top = clamp(ui.position.top, marginTop, chartHeight - marginBottom - handleHeight);

    $('#humidLine').css('top', ui.position.top + 'px');

    const maxHum = 100; // Maximum humidity value (Top = 100%)
    const minHum = -84;   // Minimum humidity value (Bottom = 0%)

    // Calculate the range of the graph that corresponds to the humidity scale
    const graphRange = chartHeight - marginTop - marginBottom;

    // Invert the scale, so top = 100%, bottom = 0%
    const humValue = maxHum - ((ui.position.top - marginTop) / graphRange) * (maxHum - minHum);
    console.log('Target Humidity: ' + humValue.toFixed(1) + '%');

    // Send the updated humidity choice to the server
    updateSensorChoice('humidity_choice', humValue);
  }
});

// Keep the initial alignment of the humidity line and handle
$('#humidLine').css('top', $('#humidHandle').position().top + 'px');

function fetchAndUpdateStatus() {
    fetch('/get_actuator_status')
        .then(response => response.json())
        .then(data => {
            // Update the status in the card dynamically
            if (data.acStatus) {
                document.getElementById('acStatus').innerText = data.acStatus;
            }
            if (data.lightStatus) {
                document.getElementById('lightStatus').innerText = data.lightStatus;
            }
            if (data.lockStatus) {
                document.getElementById('lockStatus').innerText = data.lockStatus;
            }
            if (data.boilerStatus) {
                document.getElementById('boilerStatus').innerText = data.boilerStatus;
            }
        })
        .catch(error => {
            console.error('Error fetching actuator status:', error);
        });
}

// Call the function every 1 second (1000 milliseconds)
setInterval(fetchAndUpdateStatus, 1000);

   // 1) Track local states:
    //    (You can initialize them based on real db values if you like.)
    let acOn = false;
    let lightOn = false;
    let locked = true;      // assume door is locked initially
    let boilerOn = false;

    // 3) Each toggle button triggers a fetch POST to /update_actuator with JSON data
    // For toggling the AC (fan)

function toggleAC() {
  acOn = !acOn;  // Flip the local state
  fetch('/update_actuator', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      fan: acOn ? 1 : 0
    })
  })
  .then(response => response.json())
  .then(data => {
    if(data.status !== 'success') {
      console.error('Error:', data.message);
    }
    // Do NOT change button text here; keep it static in HTML
  });
}

// Helper function to send the updated sensor choice to the server via AJAX
function updateSensorChoice(field, value) {
  fetch('/update_sensor_choice', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
    },
    body: JSON.stringify({
      [field]: value
    })
  })
  .then(response => response.json())
  .then(data => {
    if(data.status !== 'success') {
      console.error('Error:', data.message);
    }
  });
}

function toggleLight() {
  lightOn = !lightOn;
  fetch('/update_actuator', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      main_led: lightOn ? 1 : 0
    })
  })
  .then(response => response.json())
  .then(data => {
    if(data.status !== 'success') {
      console.error('Error:', data.message);
    }
  });
}

function toggleLock() {
  locked = !locked;
  fetch('/update_actuator', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      servo_motor: locked ? 0 : 1
    })
  })
  .then(response => response.json())
  .then(data => {
    if(data.status !== 'success') {
      console.error('Error:', data.message);
    }
  });
}

function toggleBoiler() {
  boilerOn = !boilerOn;
  fetch('/update_actuator', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      heater_led: boilerOn ? 1 : 0
    })
  })
  .then(response => response.json())
  .then(data => {
    if(data.status !== 'success') {
      console.error('Error:', data.message);
    }
  });
}

// Function to change the main LED mode
function changeMainLedMode(mode) {
  // Send the selected mode to the server (main_led_mode: 0, 1, or 2)
  fetch('/update_actuator', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      main_led_mode: mode // Send the mode value to the server
    })
  })
  .then(response => response.json())
  .then(data => {
    if (data.status !== 'success') {
      console.error('Error:', data.message);
    } else {
      console.log(`Main LED mode updated to: ${mode}`);
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

function updateBrightnessValue(value) {
    document.getElementById('brightnessValue').innerText = value;
  }

// Update the brightness display text
function updateBrightnessValue(value) {
    document.getElementById('brightnessValue').innerText = value;
}

// Send the brightness value to the server (via AJAX)
function sendBrightnessToServer(brightness) {
    const data = {
        brightness: brightness
    };

    fetch('/update-brightness/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken() // CSRF protection in Django
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Brightness updated:', data);
        // Optionally, update UI or display a success message
        alert(`Brightness updated to: ${data.brightness}%`);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Attach event listeners
document.getElementById('acToggle').addEventListener('click', toggleAC);
document.getElementById('lightToggle').addEventListener('click', toggleLight);
document.getElementById('lockToggle').addEventListener('click', toggleLock);
document.getElementById('boilerToggle').addEventListener('click', toggleBoiler);

// Event listener for the brightness slider
document.getElementById('brightnessSlider').addEventListener('input', function() {
    const brightnessValue = this.value;
    updateSensorChoice('brightness_choice', brightnessValue);
});

// Function to handle mode button clicks
document.getElementById('normalMode').addEventListener('click', function() {
  changeMainLedMode(0); // Normal mode
});

document.getElementById('cinemaMode').addEventListener('click', function() {
  changeMainLedMode(1); // Cinema mode
});

document.getElementById('militaryMode').addEventListener('click', function() {
  changeMainLedMode(2); // Military mode
});

  </script>
</body>
</html>

```

## 깃서버에 프로젝트 올리기

** 파이참에서는 먼저 enable VCS control 활성화 해주어야 git 메뉴 쓸수 있음(현재 버전 기준)

깃허브에 레포지토리 생성하여 프로젝트 업로드 하기

클라우드 서버 접속하기

깃서버에 업로드한 smartHome 프로젝트 clone 해오기

(우분투기준) 이때 **PAT를 비번으로 입력!!!!! (일반 비번은 ubuntu에서 허용 안됨. PAT 없으면 생성해야함)

** 아래 깃 우분투 연동 참고

[우분투 깃허브 연동 (2)](https://www.notion.so/2-1844bd4c616680e68695de77f7c67662?pvs=21)

클라우드 서버의 가상환경 활성화 시키기 (이때 반드시 manage.py가 있는 폴더에서 활성화 시켜야 한다.)

```jsx
python3 -m venv venv
source venv/bin/activate

```

requirements 설치하기 파일이 다른곳에 있다면 복사해 와서 설치하던가 가서 설치하던가 없다면 개별적으로 필요 라이브러리들을 설치한다.

```jsx
pip install -r requirements.txt

```

# 서버 배포하기

manage.py가 있는 폴더에서 gunicorn 실행 (프로젝트 명으로 실행해야함 (정확히 입력할것)

이것은 테스트 모드로 ctrl+c 눌러서 종료시키면 서버도 같이 종료됨

gunicorn 설치 (장고 웹서버 실행 툴)

```python
pip install gunicorn
```

```jsx
gunicorn --workers 3 --bind unix:/run/gunicorn/smartHome.sock smartHome.wsgi:application

```

## 아래는 웹서버 관련 다양한 명령어 모음

```jsx

#gunicorn 실행 상태 보기
ps aux | grep gunicorn 
 
#백그라운드에서 실행시키기 (& 맨 뒤에 추가하면 됨)
#백그라운드에서 실행시키면 ctrl+c 눌러서 종료시켜도 서버에서 계속 실행됨
gunicorn --bind unix:/run/gunicorn/smartHome.sock smartHome.wsgi:application &

#권한 지정 (권한 지정을 해주어야 브라우저를 통해 사이트를 불러올 수 있음)
sudo chown www-data:www-data /run/gunicorn/smartHome.sock
sudo chmod 755 /run/gunicorn/smartHome.sock

#또는
sudo chown www-data:www-data /run/gunicorn/elevator.sock
sudo chmod 666 /run/gunicorn/elevator.sock

#재시작 커맨드 (무언가 변경되면 재시작 하기)
sudo systemctl daemon-reload
sudo systemctl restart nginx
sudo systemctl restart gunicorn

#웹앱이 올바로 작동하지 않는 경우 에러 찍어보기
sudo tail -f /var/log/nginx/error.log  

```

# 프록시 설정(smarthome 예제기준)

```python
cd /etc/nginx/sites-available/
nano smarthome
```

프록시 설정예제 (/etc/nginx/sites-available/smarthome)

```python

server {
    server_name smarthome.pababel.com;

    # Favicon request handling (same as your reviewclassifier setup)
    location = /favicon.ico {
        access_log off;
        log_not_found off;
    }

    # Static files handling (modify the root path as per your elevator project directory)
    location /static/ {
        root /root/djangoProjects/smartHome/smartHome;  # Adjust to correct static file path
    }

    # Proxy the remaining requests to Gunicorn on http://127.0.0.1:8001
    location / {
        proxy_pass http://unix:/run/gunicorn/smartHome.sock;  # Pointing to 8001, as per your requirement
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/elevator.pababel.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/elevator.pababel.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}
server {
    if ($host = smarthome.pababel.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot

    server_name smarthome.pababel.com;
    listen 80;
    return 404; # managed by Certbot

}

```

싸이트 활성화

```python
sudo ln -s /etc/nginx/sites-available/smartHome /etc/nginx/sites-enabled/
```

아래 파일의 코드 메모장에 백업해놓기

```python
nano /etc/nginx/sites-enabled/default
```

https 활성화 (이것을 반드시 해주어야 웹 접속이 가능해진다)

```jsx
sudo certbot --nginx -d smarthome.pababel.com
```

cerbot 이 default로 만든 파일 수정하기  (!!만약 충돌을 일이켜 웹이 정상작동 하지 않는 경우 체크해볼것!! ) 앞에 백업해 놓은 내용으로 붙여넣어 볼것

```python
nano /etc/nginx/sites-enabled/default
```
