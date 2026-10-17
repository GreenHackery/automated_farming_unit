import serial, json
from datetime import datetime, timezone

with serial.Serial("/dev/ttyACM0", 115200, timeout=2) as ser:
    while True:
        line = ser.readline().decode(errors="ignore").strip()
        if not line:
            continue
        try:
            data = json.loads(line)
        except ValueError:
            continue
        data["timestamp"] = datetime.now(timezone.utc).isoformat()
        print(data)