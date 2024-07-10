import pygetwindow
import time
from pywinauto import Desktop

current = None


def get_current_window():
    global current
    try:
        window = pygetwindow.getActiveWindow()
        if window is None:
            return "No active window"
        if window.title != current:
            current = window.title
            return current
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    while True:
        title = get_current_window()
        if title is not None:
            print(title)
        time.sleep(1)
