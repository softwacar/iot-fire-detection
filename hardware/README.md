# 🔧 Hardware Setup (KY-026 + Raspberry Pi + LED)

## 📌 Overview
This folder documents the hardware part of the IoT Fire Detection project.
The system uses a KY-026 flame sensor connected to a Raspberry Pi. When flame is detected (or intensity changes),
the Raspberry Pi publishes the readings via MQTT and a Node-RED dashboard visualizes the data.
An LED is used as a local visual indicator on the Raspberry Pi side.

---

## 🧰 Components
- Raspberry Pi
- KY-026 Flame Sensor (flame detection module)
- LED
- 150Ω resistor
- Breadboard
- Jumper wires

---

## 🔥 KY-026 Flame Sensor (What it does)
The KY-026 module detects flame/IR light and typically provides:
- **DO (Digital Output):** On/Off indication (flame detected or not)
- **AO (Analog Output):** Intensity level (requires analog-to-digital conversion)

Note:
- Raspberry Pi does **not** support analog input directly. If we want to use AO, we will integrate an external ADC
  (e.g., MCP3008). Otherwise, we can start with DO for simple detection.

---

## 💡 LED Indicator
The LED provides immediate local feedback when flame is detected (or when the threshold is exceeded).
The LED must be connected in series with a **150Ω resistor** to limit current and protect the GPIO pin.

---

## 🔗 Hardware Data Flow
1. The KY-026 sensor detects flame / intensity changes.
2. Raspberry Pi reads sensor output (DO and/or AO via ADC).
3. Raspberry Pi publishes readings to the MQTT broker.
4. Node-RED subscribes and visualizes the data.
5. LED indicates detection locally.

---

## 🧭 Planned Connection Strategy (Pre-Hardware Plan)
Before physical assembly, we define the planned approach:
- Start with **Digital Output (DO)** to implement flame detection quickly.
- Optionally extend to **Analog Output (AO)** using an ADC for intensity measurements.

A detailed pin plan will be documented in `hardware/pin-plan.md`.

---

## 📷 Evidence & Documentation (To be added after assembly)
After hardware assembly, we will add:
- Breadboard wiring photos
- GPIO pin mapping diagram
- Testing photos / results (sensor + LED behavior)
- Any calibration notes (threshold tuning)

---

## ✅ Status
- Hardware documentation structure: Completed
- Physical wiring and testing: Pending (materials not yet available)
