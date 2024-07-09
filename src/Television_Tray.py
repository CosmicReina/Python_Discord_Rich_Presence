import pystray
import sys
import os
from PIL import Image


def resource_path(relative_path: str):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


image_path = resource_path("television.ico")
image = Image.open(image_path)


def action_exit(icon: pystray.Icon, _):
    icon.stop()


class TelevisionMenu(pystray.Menu):
    item_exit = pystray.MenuItem("Exit", action_exit)

    def __init__(self):
        super().__init__(self.item_exit)


icon = pystray.Icon(name="Television", icon=image, title="Television", menu=TelevisionMenu())
icon.run()
