import os
import sys
import threading
import time

from pypresence import Presence

import pystray
from PIL import Image


TRAY_CLOSED = False


def resource_path(relative_path: str):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def action_exit(icon: pystray.Icon, _):
    global TRAY_CLOSED
    TRAY_CLOSED = True
    icon.stop()


# Pystray
class TelevisionMenu(pystray.Menu):
    item_exit = pystray.MenuItem("Exit", action_exit)

    def __init__(self):
        super().__init__(self.item_exit)


IMAGE_PATH = resource_path("resources/television.ico")
IMAGE = Image.open(IMAGE_PATH)
ICON = pystray.Icon(name="Television", icon=IMAGE, title="Television", menu=TelevisionMenu())


# PyPresence
START = time.time()

APPLICATION_ID = "1260226649870565537"
RPC = Presence(APPLICATION_ID)
NAME = os.path.basename(__file__).split(".")[0]


def run_rpc():
    RPC.connect()
    print(f"Presence {NAME} has started.")

    try:
        while not TRAY_CLOSED:
            RPC.update(
                details="Watching television",
                state="Switching channels",
                large_image="television",
                large_text="Watching television",
                start=int(START),
            )
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"Presence {NAME} has stopped due to a keyboard interrupt.")
    except Exception as e:
        print(f"Presence {NAME} has stopped due to an error: {e}")

    RPC.close()
    print(f"Presence {NAME} has stopped.")


def run_icon():
    ICON.run()


thread_icon = threading.Thread(target=run_icon, daemon=True)
thread_rpc = threading.Thread(target=run_rpc, daemon=True)

thread_icon.start()
thread_rpc.start()

thread_icon.join()
thread_rpc.join()
