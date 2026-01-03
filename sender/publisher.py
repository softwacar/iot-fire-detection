import time
import json
import datetime
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

# GPIO pins
FLAME_PIN = 17   # KY-026 DO (digital output)
LED_PIN = 27     # Red LED

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)

# MQTT settings
BROKER = "localhost"
TOPIC = "iot/fire/sensor"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, 1883, 60)

print("Fire detection system started")

try:
    while True:
        flame_signal = GPIO.input(FLAME_PIN)

        # ACTIVE-HIGH logic
        flame_detected = (flame_signal == 1)

        # LED control
        GPIO.output(LED_PIN, GPIO.HIGH if flame_detected else GPIO.LOW)

        # Payload
        data = {
            "flame_detected": flame_detected,
            "raw_sensor_value": flame_signal,
            "timestamp": datetime.datetime.now().isoformat()
        }

        client.publish(TOPIC, json.dumps(data))
        print("Published:", data)

        time.sleep(1)

except KeyboardInterrupt:
    print("System stopped")

finally:
    GPIO.cleanup()
