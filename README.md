# Keylogger Application

This repository contains a Python keylogger application that captures keystrokes and sends the logged data to an Express server over HTTP. This application is built for **educational purposes only**. Use this software responsibly and ethically. Always obtain permission before logging any keystrokes.

## Features
- Captures keystrokes using Python's `pynput` library.
- Sends captured keystroke logs to an Express server at a specified time interval.
- Gracefully handles server errors by saving unsent logs to a local file (`unsend_logs.txt`).

---

## Prerequisites
Ensure the following tools are installed on your system:
- Python 3.6+
- Node.js

---

## Setup Instructions

### 1. Install Dependencies
#### Python
Run the following command to install Python dependencies:

```bash
pip install -r requirements.txt
```

#### Express Server
Navigate to the `server/` folder and install dependencies using:

```bash
npm install
```

### 2. Running the Application

#### Step 1: Start the Express Server
Use the following command to start the server on `http://localhost:8080`:

```bash
node server.js
```

#### Step 2: Run the Keylogger
Run the Python keylogger script:

```bash
python keylogger.py
```

---

## Configuration
Modify the following variables in the `keylogger.py` script to suit your environment:

```python
ip_address = "localhost"  # Server IP address
port_number = "8080"      # Server Port
```

You can also set the time interval (in seconds) for sending logs by updating:

```python
time_interval = 10
```

---

## Keylogger Script Overview

### Core Functionality
1. **Keystroke Capture**:
   Captures keystrokes using the `pynput` library and stores them in a global string variable `text`.

2. **Periodic HTTP POST Requests**:
   Periodically sends the captured keystrokes to the configured server endpoint (`http://<ip_address>:<port_number>`).

3. **Error Handling**:
   - Writes unsent logs to `unsend_logs.txt`.
   - Logs server connection issues in the console.

---

## Express Server Overview
The Express server listens for incoming POST requests on port `8080`. It accepts JSON data and logs the received keystroke data to the console.

### Example `server.js`
```javascript
const express = require('express');
const app = express();
const port = 8080;

app.use(express.json());

app.post('/', (req, res) => {
    console.log('Received Data:', req.body);
    res.status(200).send('Logs received');
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
```

---

## Ethics and Legal Considerations
- **Permission**: Always obtain proper consent before running this keylogger on any device.
- **Legal Compliance**: Ensure compliance with local laws and regulations.
- **Disclaimer**: This software is intended for educational purposes only. Unauthorized use is strictly prohibited and punishable under applicable laws.

---

## License
This project is licensed under the [MIT License](LICENSE).
