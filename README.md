# IoT Fire Detection System

## Project Description
This project implements a fire detection system using a KY-026 flame sensor connected to a Raspberry Pi.
The Raspberry Pi publishes sensor data via MQTT in JSON format.
A subscriber running on a PC uses Node-RED to visualize the incoming data on a dashboard.

## Hardware Components
- Raspberry Pi
- KY-026 Flame Sensor
- LED
- 150Ω Resistor
- Breadboard
- Jumper Wires

## Software Technologies
- Python
- MQTT (Mosquitto Broker)
- Node-RED Dashboard

## System Architecture
1. The KY-026 flame sensor detects fire or flame intensity.
2. Raspberry Pi reads sensor data and formats it as JSON.
3. Raspberry Pi publishes data to an MQTT broker.
4. Node-RED subscribes to the MQTT topic.
5. Data is visualized on a Node-RED dashboard (charts/indicators).

## Data Format (MQTT Payload Example)
```json
{
  "flame_detected": true,
  "sensor_value": 320,
  "timestamp": "2025-01-12T14:32:10"
}
