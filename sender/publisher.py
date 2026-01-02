import time
import json
import datetime
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

FLAME_PIN = 17   # KY-026 D0
LED_PIN = 27     # Kırmızı LED

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

BROKER = "localhost"
TOPIC = "iot/fire/sensor"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, 1883, 60)

print("🔥 Fire detection started...")

try:
    while True:
        flame = GPIO.input(FLAME_PIN)   # 0 = ALEV VAR
        flame_detected = (flame == 0)

        GPIO.output(LED_PIN, GPIO.HIGH if flame_detected else GPIO.LOW)

        data = {
            "flame_detected": flame_detected,
            "sensor_value": flame,
            "timestamp": datetime.datetime.now().isoformat()
        }

        client.publish(TOPIC, json.dumps(data))
        print("Published:", data)

        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped")

finally:
    GPIO.cleanup()
