This project demonstrates an Analytics Pipeline where telemetry messages flow from a local Python producer → Azure Storage Queue → Azure Function → Azure SQL Database.
The producer script simulates IoT devices by sending JSON data to the queue.
An Azure Function with a Queue Trigger processes each batch, computes aggregates, and upserts them into SQL.
The SQL table DeviceMetrics stores count, avgTemp, minTemp, maxTemp, and lastSeen values per device.
Local development uses a virtual environment and Azure SDK packages.
Connection strings are stored securely in local.settings.json, not in code.
To run locally: activate venv, install dependencies, start producer, then run func start.
Azure SQL schema script is included for table creation.
