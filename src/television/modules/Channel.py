import time
from typing import Optional

import pygetwindow


def get_current_window() -> Optional[str]:
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
            break
