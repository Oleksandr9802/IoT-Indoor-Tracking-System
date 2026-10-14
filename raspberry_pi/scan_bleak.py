import asyncio
from datetime import datetime
from bleak import BleakScanner
import requests

target_tag = "c2:05:a7:79:40:92".lower()
location = "bedroom"  # Change this on each Pi

def rssi_to_zone(rssi):
    if rssi > -60:
        return "🟢 IN ROOM"
    elif -75 < rssi <= -60:
        return "🟡 NEARBY"
    else:
        return "🔴 FAR or LEFT"

def send_to_backend(rssi, zone):
    payload = {
        "device": target_tag,
        "zone": zone,
        "rssi": rssi,
        "location": location,
        "timestamp": datetime.now().isoformat()
    }
    try:
        res = requests.post("http://<your-backend-ip>:8000/footsteps/", json=payload)
        print(f"✅ Sent to backend: {res.status_code}")
    except Exception as e:
        print(f"❌ Failed to send: {e}")

def detection_callback(device, adv_data):
    if device.address.lower() == target_tag:
        zone = rssi_to_zone(adv_data.rssi)
        print(f"{datetime.now()} 🎯 Tag found! RSSI: {adv_data.rssi} → {zone}")
        send_to_backend(adv_data.rssi, zone)
        print("-" * 40)

async def scan_loop():
    print(f"🔁 BLE Scanner starting for location: {location}")
    scanner = BleakScanner(detection_callback=detection_callback)
    await scanner.start()

    try:
        while True:
            await asyncio.sleep(5)
            print("🔍 Scanning...")
    except KeyboardInterrupt:
        print("🛑 Stopping scan.")
    finally:
        await scanner.stop()

asyncio.run(scan_loop())
