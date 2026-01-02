import time
import json
import datetime
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

# ===== GPIO SETUP =====
FLAME_PIN = 17  # D0 -> GPIO17

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME_PIN, GPIO.IN)

# ===== MQTT SETUP =====
BROKER = "localhost"        # Mosquitto Raspberry Pi üzerinde
PORT = 1883
TOPIC = "iot/fire/sensor"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print("🔥 Fire detection started (KY-026)...")

try:
    while True:
        flame_raw = GPIO.input(FLAME_PIN)
        flame_detected = (flame_raw == 0)  # KY-026: 0 = fire

        data = {
            "flame_detected": flame_detected,
            "sensor_value": int(flame_detected),  # 1 or 0
            "timestamp": datetime.datetime.now().isoformat()
        }

        client.publish(TOPIC, json.dumps(data))
        print("Published:", data)

        time.sleep(2)

except KeyboardInterrupt:
    print("⛔ Stopped by user")

finally:
    GPIO.cleanup()
