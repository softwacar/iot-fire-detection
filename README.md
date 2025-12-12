# 🔥 IoT Fire Detection System

## 📘 Project Description
This project implements a fire detection system using a KY-026 flame sensor connected to a Raspberry Pi.
The Raspberry Pi publishes sensor data via MQTT.
Node-RED is used to subscribe to the data and visualize it on a dashboard.

## 🧰 Hardware Components
- Raspberry Pi
- KY-026 Flame Sensor
- LED
- 150Ω Resistor
- Breadboard
- Jumper Wires

## 💻 Software Technologies
- Python
- MQTT (Mosquitto Broker)
- Node-RED Dashboard

## 🧠 System Architecture
- The KY-026 sensor detects fire or flame intensity.
- Raspberry Pi reads the sensor data.
- Data is sent to an MQTT broker.
- Node-RED subscribes to the MQTT topic.
- Sensor data is visualized on a dashboard.

## 📡 MQTT Data Format
Example JSON message sent over MQTT:

    {
      "flame_detected": true,
      "sensor_value": 320,
      "timestamp": "2025-01-12T14:32:10"
    }

## 📂 Repository Structure
- sender/     Raspberry Pi MQTT publisher (Python)
- receiver/   MQTT subscriber tools
- node-red/   Node-RED flows and dashboard
- hardware/   Circuit diagrams and connections
- docs/       Project documentation

## 👥 Team Members
- Abdullah Acar
- Edina Bajric
- Riad Efendic
- Edis Ahmethodzic
- Ares Orascanin

## 🎓 Course
IoT Fundamentals
