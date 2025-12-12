import json
import time
import random
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/fire/sensor"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)
client.loop_start()

def read_flame_sensor():
   # Mock flame sensor data (used before real hardware integration)
    value = random.randint(0, 1023)
    flame_detected = value > 300
    return value, flame_detected

while True:
    sensor_value, flame = read_flame_sensor()

    payload = {
        "flame_detected": flame,
        "sensor_value": sensor_value,
        "timestamp": datetime.now().isoformat()
    }

    client.publish(TOPIC, json.dumps(payload))
    print("Published:", payload)

    time.sleep(2)
