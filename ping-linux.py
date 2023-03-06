import subprocess
import logging
import json
import requests as r
from datetime import datetime
from pathlib import Path

#---------------------------------------------------------------
#               Configuration
#---------------------------------------------------------------

# Load the configuration settings from the JSON file
with open(Path("config.json")) as f:
    config = json.load(f)

# Telegram credentials
TELEGRAM_TOKEN = config["telegram_token"]
TELEGRAM_CHAT_ID = config["telegram_chat_id"]

# IP address of the server to monitor
SERVER_IP = config["server_ip"]

#---------------------------------------------------------------
#               Initialization
#---------------------------------------------------------------

# Load the previous server state
with open(Path("status.json")) as f:
    serv_status = json.load(f)

# Initialize the logger
logger = logging.getLogger("Status")
logger.setLevel(logging.INFO)
handler = logging.FileHandler(Path("log_connection.log"), encoding="utf-8", mode="a")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

#---------------------------------------------------------------
#               Server monitoring
#---------------------------------------------------------------

def check_server():
    # Execute the ping command
    cmd = ["ping", SERVER_IP, "-c", "4"]
    response = subprocess.run(cmd, stdout=subprocess.PIPE)
    lines = response.stdout.decode("utf-8").splitlines()
    
    # Check if the server is online
    if "4 packets received" in lines[-2]:
        logger.info("Server UP")

        # Update the server state
        serv_status["status_server"] = 1
        serv_status["day"] = datetime.now().day

        # Check the ping
        time_line = lines[-1]
        response = time_line.split("=")[-1].removesuffix(" ms").split("/")
        ping = float(response[1].replace(",", "."))
        
        if ping > 200:
            logger.warning(f"High ping: {ping} ms")
            send_telegram_message(message="HIGH Ping")
    else:
        logger.error("Server DOWN")

        # Update the server state
        serv_status["status_server"] = 0

        # Send a Telegram message
        send_telegram_message(message="Server DOWN")

#---------------------------------------------------------------
#               Telegram integration
#---------------------------------------------------------------

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}"
    r.get(url)

#---------------------------------------------------------------
#               Main function
#---------------------------------------------------------------

if __name__ == "__main__":
    # Load the previous server state
    with open(Path("status.json")) as f:
        serv_status = json.load(f)

    # Check if the server is already online
    if serv_status["status_server"] == 1:
        check_server()
