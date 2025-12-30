# MQTT Receiver & Dashboard (Node-RED)

## Project: Fire Detection System  
**Component:** MQTT Subscriber and Data Visualization  
**Course:** IoT Fundamentals

---

## 1. Overview

This component represents the **receiver (subscriber) side** of the Fire Detection IoT project.  
The receiver is implemented using **Node-RED** and runs on a PC/laptop. Its purpose is to:

- Subscribe to fire sensor data published over MQTT
- Parse JSON-formatted messages
- Visualize fire detection status and sensor readings in real time using a dashboard

No physical hardware is required for the receiver side.

---

## 2. Technologies Used

- Node.js  
- Node-RED  
- Node-RED Dashboard  
- MQTT (Mosquitto broker)  
- JSON  

---

## 3. MQTT Configuration

- **Broker:** `test.mosquitto.org`  
  (Can be replaced with the Raspberry Pi IP address in the final setup)
- **Port:** `1883`
- **Topic:**

---

## 4. MQTT Message Format

The receiver expects JSON messages in the following format:

json
{
"flame_detected": true,
"sensor_value": 320,
"timestamp": "2025-01-12T14:32:10"
}

### Field Description

- **flame_detected** (boolean):  
  Indicates whether a fire has been detected by the flame sensor.

- **sensor_value** (integer):  
  Analog value measured by the flame sensor.

- **timestamp** (string):  
  Time at which the sensor measurement was recorded.

---

## 5. Node-RED Flow Description

The Node-RED flow is composed of the following nodes:

### MQTT In  
Subscribes to the topic `iot/fire/sensor` and receives sensor data messages from the MQTT broker.

### JSON  
Converts incoming MQTT payloads from string format into JSON objects so they can be processed inside Node-RED.

### Change Nodes  
The flow uses multiple Change nodes to prepare data for visualization:
- Extracts `sensor_value` and forwards it as a numeric payload for chart visualization
- Extracts `flame_detected` and converts it into a human-readable fire status message
- Sets `msg.topic` to ensure proper rendering of data in the chart widget

### UI Chart  
Displays the flame sensor value over time using a line chart.

### UI Text  
Displays the current fire detection status:
- 🔥 **FIRE DETECTED**
- ✅ **No Fire**

### Inject (Testing Only)  
Used during development to simulate MQTT messages without requiring physical hardware.

---

## 6. Dashboard Layout

The Node-RED dashboard consists of the following elements:

- **Tab:** Fire Monitor  
- **Group:** Sensor Data  

### Widgets:
- Fire status text indicator  
- Flame sensor value line chart  

The dashboard can be accessed via the following URL: http://localhost:1880/ui


---

## 7. Testing

The receiver was tested using:
- Inject nodes with mock JSON data
- Live MQTT messages received from the broker

Debug nodes were used to verify correct message structure and ensure that numerical and boolean data types were processed correctly.

---

## 8. Files Included

receiver/
├── README.md
└── node-red/
├── fire_detection_node_red_flow.json
└── dashboard.png

---

## 9. Notes

- The receiver component does not require physical sensors or additional hardware.
- The system is fully compatible with the Raspberry Pi MQTT publisher.
- The dashboard updates in real time as new MQTT messages are received.

---

## 10. Conclusion

This receiver implementation demonstrates MQTT subscription, JSON message handling, and real-time data visualization using Node-RED. It fulfills all requirements of the Fire Detection IoT project and provides a clear and effective monitoring interface.
