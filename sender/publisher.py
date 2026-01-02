import time
import json
import datetime
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

# -------- GPIO SETTINGS --------
FLAME_PIN = 17  # KY-026 D0 -> GPIO17 (Pin 11)

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME_PIN, GPIO.IN)

# -------- MQTT SETTINGS --------
BROKER = "localhost"          # Mosquitto Raspberry Pi üzerinde
PORT = 1883
TOPIC = "iot/fire/sensor"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT, 60)

print("🔥 Fire detection started...")

try:
    while True:
        flame_signal = GPIO.input(FLAME_PIN)
        flame_detected = (flame_signal == 0)  # KY-026: 0 = fire detected

        data = {
            "flame_detected": flame_detected,
            "sensor_value": int(flame_detected),
            "timestamp": datetime.datetime.now().isoformat()
        }

        client.publish(TOPIC, json.dumps(data))
        print("Published:", data)

        time.sleep(2)

except KeyboardInterrupt:
    print("🛑 Stopped by user")

finally:
    GPIO.cleanup()
