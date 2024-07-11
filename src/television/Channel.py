import pygetwindow
import time
from typing import Optional


def get_current_window():
    window = pygetwindow.getActiveWindow()
    if window is None:
        return None
    return window.title


if __name__ == "__main__":
    current: Optional[str] = None
    while True:
        title = get_current_window()
        if title != current:
            print(title)
            current = title
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print("Exiting...")
            break

