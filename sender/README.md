# 🔥 MQTT Publisher (Raspberry Pi)

## 📌 Overview
This module runs on the Raspberry Pi and is responsible for publishing flame sensor data to an MQTT broker.
At this stage, mock sensor data is used to simulate the KY-026 flame sensor until hardware integration is completed.

---

## 👤 Role & Responsibility
**Abdullah Acar – MQTT Publisher Developer**

Responsibilities:
- 📡 Generate flame sensor data (mock implementation)
- 🧾 Format sensor readings as JSON
- 🚀 Publish data periodically to an MQTT broker
- 🔗 Ensure compatibility with Node-RED subscribers

---

## ⚙️ MQTT Configuration
- **Broker:** localhost  
- **Port:** 1883  
- **Topic:** iot/fire/sensor  
- **Protocol:** MQTT  
- **Payload Format:** JSON  

---

## 🧾 JSON Payload Example
Example MQTT message payload:

{
  "flame_detected": true,
  "sensor_value": 320,
  "timestamp": "2025-01-12T14:32:10"
}

---

## 🧠 How It Works
1. 🎲 A mock flame sensor value between 0 and 1023 is generated.
2. 🚨 A threshold determines whether a flame is detected.
3. 🧾 Sensor data is formatted into a JSON object.
4. 📡 The message is published to the MQTT topic every 2 seconds.
5. 📊 Node-RED subscribes to this topic and visualizes the data.

---

## ▶️ How to Run
Install the required dependency:
pip install paho-mqtt

Run the publisher script:
python3 publisher.py

---

## 📝 Notes
- 🧪 Mock sensor data is intentionally used before real hardware integration.
- 🔌 The mock function will be replaced with GPIO-based KY-026 readings.
- 📊 This module is fully compatible with the Node-RED dashboard.

---

## ✅ Status
- MQTT publisher logic: Completed
- JSON data format: Finalized
- Hardware integration: Pending
