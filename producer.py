import json
import os
import time
import random
from azure.storage.queue import QueueClient

queue_conn = "DefaultEndpointsProtocol=https;AccountName=snehastorage12;AccountKey=fwk6NzUTqsExADHjRLrqiuE6PLJHJl5gB61+4p7oMEZGwCbmjGSdsCI3V7XRE6y1gcLBuOXpUa+M+AStr7aE8Q==;EndpointSuffix=core.windows.net"
queue_name = "device-telemetry"

client = QueueClient.from_connection_string(queue_conn, queue_name)

while True:
    message = {
        "deviceId": f"device-{random.randint(1,5)}",
        "timestamp": time.time(),
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(40, 90), 2)
    }

    client.send_message(json.dumps(message))
    print("Sent:", message)

    time.sleep(1)   # 1 message per second
