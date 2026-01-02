import time
import json
import datetime
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

FLAME_PIN = 17   # KY-026 D0
LED_PIN = 27     # Harici LED

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

BROKER = "localhost"
TOPIC = "iot/fire/sensor"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, 1883, 60)

print("🔥 Fire detection started...")

try:
    while True:
        flame = GPIO.input(FLAME_PIN)   # 0 = alev var
        flame_detected = (flame == 0)

        GPIO.output(LED_PIN, GPIO.HIGH if flame_detected else GPIO.LOW)

        data = {
            "flame_detected": flame_detected,
            "sensor_value": 1 if flame_detected else 0,
            "timestamp": datetime.datetime.now().isoformat()
        }

        client.publish(TOPIC, json.dumps(data))
        print("Published:", data)

        time.sleep(2)

except KeyboardInterrupt:
    print("Stopped")

finally:
    GPIO.cleanup()
