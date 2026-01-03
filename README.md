# 🔥 IoT Fire Detection System

## 📘 Project Description
This project implements a fire detection system using a KY-026 flame sensor connected to a Raspberry Pi.
The Raspberry Pi reads the digital output of the flame sensor and publishes detection data via MQTT.
Node-RED is used to subscribe to the MQTT data and visualize the fire detection status on a dashboard.

The system also provides local visual feedback using an LED and is capable of operating fully offline.

## 🧰 Hardware Components
- Raspberry Pi
- KY-026 Flame Sensor
- LED
- Resistor (current-limiting for LED)
- Breadboard
- Jumper wires

## 💻 Software Technologies
- Python 3
- MQTT (Mosquitto Broker)
- Node-RED Dashboard

## 🧠 System Architecture
- The KY-026 flame sensor detects the presence of a flame.
- Raspberry Pi reads the digital sensor output.
- Sensor data is published to an MQTT broker.
- Node-RED subscribes to the MQTT topic.
- Fire detection data is visualized on a dashboard and indicated locally using an LED.

## 📡 MQTT Data Format
Example JSON message sent over MQTT:

{
  "flame_detected": true,
  "raw_sensor_value": 1,
  "timestamp": "2026-01-03T15:52:49"
}

## 📂 Repository Structure
- sender/        Raspberry Pi MQTT publisher (Python)
- receiver/      MQTT subscriber tools
- node-red/      Node-RED flows and dashboard
- hardware/      Circuit diagrams and connections
- docs/          Project documentation

## 👥 Team Members
- Abdullah Acar
- Edina Bajric
- Riad Efendic
- Edis Ahmethodzic
- Ares Orascanin

## 🎓 Course
IoT Fundamentals

