# IoT-Indoor-Tracking-System
Developed an IoT-based indoor tracking system using two Raspberry Pi Zero 2 W devices and Bluetooth Low Energy (BLE) technology to monitor device proximity across different rooms.

- **Python & BLE:** Implemented asynchronous Bluetooth scanning using the Bleak library to detect nearby devices and estimate proximity through RSSI measurements.
- **Backend Development:** Built a FastAPI REST API to receive real-time device information, including signal strength, location, and timestamps.
- **Linux & Automation:** Configured Raspberry Pi devices for headless operation using SSH and automated Python scripts with systemd services.
- **Networking:** Established HTTP communication between Raspberry Pi devices and a centralized backend over a local network.
- **System Design:** Explored multi-device signal comparison to identify the closest Raspberry Pi and reduce duplicate location reports.

**Technologies:** Python, Raspberry Pi, Linux, Bluetooth Low Energy (BLE), FastAPI, REST APIs, SSH, systemd, asyncio.
