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
        flame_raw = GPIO.input(FLAME_PIN)
        flame_detected = (flame_raw == 0)  # KY-026: 0 = alev

        GPIO.output(LED_PIN, flame_detected)

        data = {
            "flame_detected": flame_detected,
            "timestamp": datetime.datetime.now().isoformat()
        }

        client.publish(TOPIC, json.dumps(data))
        print("Published:", data)

        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped")

finally:
    GPIO.cleanup()
