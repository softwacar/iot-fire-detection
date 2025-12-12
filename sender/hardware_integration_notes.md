# 🔌 Hardware Integration Notes (KY-026 Flame Sensor)

## 📌 Purpose
This document explains how the current mock-based flame sensor implementation
will be replaced with real KY-026 hardware readings once the Raspberry Pi and
sensor are physically available.

---

## 🧩 Current Implementation Status
- Flame sensor data is generated using a mock function
- No GPIO access is required at this stage
- MQTT publishing logic is fully implemented and tested independently

This approach allows software development to proceed without hardware dependency.

---

## 🔥 KY-026 Flame Sensor Overview
- Sensor Type: Infrared flame detection
- Output:
  - Digital Output (DO): Flame detected / not detected
  - Analog Output (AO): Flame intensity level
- Operating Voltage: 3.3V – 5V

---

## 🔗 Planned Raspberry Pi GPIO Connections
- **VCC:** Raspberry Pi 3.3V
- **GND:** Raspberry Pi GND
- **AO (Analog Output):** External ADC module (e.g., MCP3008)
- **DO (Digital Output):** Raspberry Pi GPIO pin (e.g., GPIO17)

> Note: Raspberry Pi does not support analog input directly.
> An ADC module is required for analog readings.

---

## 🧠 Software Changes Required
The following function in `publisher.py` will be updated:

Current mock function:
- Generates random values
- Simulates flame detection logic

Future hardware-based function will:
- Read GPIO digital input (DO) for flame detection
- Optionally read analog value via ADC
- Preserve the same JSON payload structure

This ensures seamless integration with Node-RED and MQTT subscribers.

---

## 🔄 Migration Strategy
1. Keep MQTT publish logic unchanged
2. Replace mock sensor function with GPIO-based implementation
3. Validate readings with real flame source
4. Re-test MQTT message delivery and visualization

---

## ✅ Design Advantage
- Clean separation between hardware access and communication logic
- Minimal code changes required during hardware integration
- Reduced risk during final system assembly
