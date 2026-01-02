import time
import json
import datetime
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

# -------- GPIO SETUP --------
FLAME_PIN = 17  # GPIO17

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME_PIN, GPIO.IN)

# -------- MQTT SETUP --------
BROKER = "localhost"     # Raspberry Pi üzerinde Mosquitto
PORT = 1883
TOPIC = "iot/fire/sensor"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)
client.loop_start()

print("🔥 Fire detection started...")

try:
    while True:
        flame_detected = GPIO.input(FLAME_PIN) == 0
        # KY-026: Alev varsa genelde LOW verir

        payload = {
            "flame_detected": flame_detected,
            "sensor_value": 1 if flame_detected else 0,
            "timestamp": datetime.datetime.now().isoformat()
        }

        client.publish(TOPIC, json.dumps(payload))
        print("Published:", payload)

        time.sleep(2)

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    GPIO.cleanup()
    client.loop_stop()
    client.disconnect()
