# ⚠️ Error Handling & System Robustness

## 📌 Purpose
This document describes potential error scenarios in the IoT Fire Detection System
and explains how the system is designed to handle or mitigate these issues.

---

## 🔌 MQTT Broker Unavailable
**Scenario:**  
The MQTT broker is not running or becomes unreachable.

**Impact:**  
The publisher cannot deliver sensor data to subscribers.

**Mitigation Strategy:**  
- Publisher attempts reconnection
- Errors are logged to the console
- System continues running without crashing

---

## 🌐 Network Connectivity Loss
**Scenario:**  
Network connection between Raspberry Pi and PC is lost.

**Impact:**  
Messages cannot be received by Node-RED.

**Mitigation Strategy:**  
- MQTT client maintains connection loop
- Data publishing resumes automatically after reconnection
- No manual restart required

---

## 🔥 Sensor Failure or Invalid Readings
**Scenario:**  
The flame sensor produces invalid or noisy values.

**Impact:**  
Incorrect fire detection status.

**Mitigation Strategy:**  
- Threshold-based filtering
- Validation of sensor value range
- Future implementation of averaging or debounce logic

---

## ⏱️ Timing & Performance Issues
**Scenario:**  
High publish frequency causes performance degradation.

**Impact:**  
Increased CPU or network usage.

**Mitigation Strategy:**  
- Fixed publish interval (2 seconds)
- Adjustable timing parameters
- Lightweight JSON payload

---

## 🔄 Graceful Degradation
In case of partial system failures, the system is designed to:
- Continue operating in a reduced functionality mode
- Avoid system crashes
- Preserve communication structure for fast recovery

---

## ✅ Reliability Summary
- Modular system design
- Clear separation between hardware, communication, and visualization
- Fault-tolerant com
