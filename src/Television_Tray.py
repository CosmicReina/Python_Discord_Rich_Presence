import pystray
from PIL import Image

image = Image.open("television.ico")


def action_exit(icon: pystray.Icon, _):
    icon.stop()


class TelevisionMenu(pystray.Menu):
    item_exit = pystray.MenuItem("Exit", action_exit)

    def __init__(self):
        super().__init__(self.item_exit)


icon = pystray.Icon(name="Television", icon=image, title="Television", menu=TelevisionMenu())
icon.run()
