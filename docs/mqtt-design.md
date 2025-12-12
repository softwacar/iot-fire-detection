# 📡 MQTT Topic & Data Design

## 📌 Purpose
This document describes the MQTT communication design used in the IoT Fire Detection project.
It defines the topic structure, message format, and design decisions to ensure reliable data exchange
between the Raspberry Pi publisher and Node-RED subscriber.

---

## 🧭 MQTT Architecture Overview
- **Publisher:** Raspberry Pi (Python script)
- **Broker:** Mosquitto (running on Raspberry Pi)
- **Subscriber:** Node-RED (PC)
- **Communication Model:** Publish / Subscribe

---

## 🧵 Topic Design
**Main Topic:**
iot/fire/sensor

### Design Rationale
- `iot` → Identifies IoT-based system
- `fire` → Project domain (fire detection)
- `sensor` → Source of data (flame sensor)

This structure is simple, readable, and scalable for future extensions.

---

## 🧾 Message Payload Design
The MQTT messages are formatted in JSON to ensure compatibility with Node-RED
and ease of data parsing and visualization.

### Payload Fields Description
- `flame_detected`  
  - Type: Boolean  
  - Description: Indicates whether a flame is detected based on threshold logic

- `sensor_value`  
  - Type: Integer  
  - Range: 0 – 1023  
  - Description: Raw analog value from the flame sensor

- `timestamp`  
  - Type: String  
  - Format: ISO 8601  
  - Description: Time when the data was published

---

## 🧠 Threshold Logic
A flame is considered detected when the sensor value exceeds a predefined threshold.

- **Threshold Value:** 300
- **Reason:** Empirically chosen for reliable fire detection while avoiding noise

---

## 🔄 Data Flow Summary
1. Sensor data is read (mock data before hardware integration).
2. Threshold logic determines flame detection status.
3. Data is packaged into a JSON object.
4. Message is published to the MQTT broker.
5. Node-RED subscribes to the topic and visualizes the data.

---

## ✅ Design Benefits
- Lightweight and efficient communication
- Easy integration with Node-RED dashboard
- Clear data semantics for visualization and analysis
- Hardware-independent design during development
