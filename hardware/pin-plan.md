# 📍 GPIO Pin Plan (Pre-Hardware)

## 📌 Purpose
This document defines the planned GPIO pin assignments for the hardware components
used in the IoT Fire Detection project. The plan is prepared before physical assembly
to ensure a clean and organized wiring process.

---

## 🧠 Design Considerations
- Raspberry Pi GPIO pins operate at **3.3V**
- GPIO pins must not exceed current limits
- LED must be protected with a resistor
- Start with **Digital Output (DO)** from KY-026 for simplicity
- Keep pin assignments flexible in case of hardware constraints

---

## 🔥 KY-026 Flame Sensor – Planned Connections

| KY-026 Pin | Raspberry Pi Pin | GPIO | Description |
|-----------|------------------|------|-------------|
| VCC       | 3.3V             | —    | Power supply |
| GND       | GND              | —    | Ground |
| DO        | GPIO17           | 17   | Digital flame detection |

> Note: AO (Analog Output) is not used initially because Raspberry Pi has no native ADC.
> AO can be connected later via an external ADC module (e.g., MCP3008).

---

## 💡 LED – Planned Connections

| Component | Raspberry Pi Pin | GPIO | Description |
|---------|------------------|------|-------------|
| LED (+) | GPIO27           | 27   | Flame indicator output |
| LED (−) | GND              | —    | Ground (via 150Ω resistor) |

- The LED is connected in series with a **150Ω resistor**
- GPIO27 is chosen as a general-purpose output pin

---

## 🔄 Optional Future Extension (Analog Reading)
If analog flame intensity measurement is required:
- Use an external ADC (e.g., MCP3008)
- Connect KY-026 AO → ADC input channel
- Connect ADC to Raspberry Pi via SPI (MOSI, MISO, CLK, CS)

This extension will not affect the existing MQTT or Node-RED configuration.

---

## ⚠️ Safety Notes
- Do not connect 5V directly to GPIO pins
- Always use a resistor with the LED
- Double-check wiring before powering the Raspberry Pi

---

## ✅ Status
- Pin planning: Completed
- Physical verification: Pending (materials not yet available)
