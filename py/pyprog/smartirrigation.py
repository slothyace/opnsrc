import RPi.GPIO as gpio
import time as t
import requests
import dht11

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(4,gpio.IN)
gpio.setup(26,gpio.OUT)
pwm = gpio.PWM(26,50)

instance = dht11.DHT11(pin=21)
result = instance.read()
count=1

while True:
    result = instance.read()
    hmdty = result.humidity
    temp = result.temperature
    if result.is_valid():
        print("Humidity:",hmdty)
        print("Temperature: ", temp)
        resp = requests.get('https://api.thingspeak.com/update?api_key=<APIKEY>&field1=%s&field2=%s' %(hmdty,temp))
        print('sent')
        if hmdty <65 and temp >25:
            print('Opening Valve')
            pwm.start(3)
            t.sleep(9)
            print('Closing Valve')
            pwm.start(0)
        elif hmdty <65 and temp <25:
            print('Opening Valve')
            pwm.start(3)
            t.sleep(6)
            print('Closing Valve')
            pwm.start(0)
        elif hmdty >65:
            print('No watering done.')
    count=count+1
    if count > 3:
        if gpio.input(4):
            print('water level acceptable')
        else:
            TKN= '<TKN>'
            chatid='<CHATID>'
            message='Tank water level is low, please refill soon. - SmartIrri'
            url= f'https://api.telegram.org/bot{TKN}/sendMessage?chat_id={chatid}&text={message}'
            print(requests.get(url).json())
            print('water level low, please refill soon')
        count=1
    t.sleep(20)
