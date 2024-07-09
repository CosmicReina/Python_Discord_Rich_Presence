import time
import os

import pypresence
from pypresence import Presence

start = time.time()

APPLICATION_ID = "1260226649870565537"
RPC = Presence(APPLICATION_ID)
NAME = os.path.basename(__file__).split(".")[0]


def run():
    RPC.connect()
    print(f"Presence {NAME} has started.")

    try:
        while True:
            RPC.update(
                details="Watching Television",
                state="Switching Channels",
                large_image="television",
                large_text="Watching Television",
                start=int(start),
            )
            time.sleep(1)
    except KeyboardInterrupt:
        RPC.close()
        print(f"Presence {NAME} has stopped due to a keyboard interrupt.")
    except pypresence.PipeClosed:
        print(f"Presence {NAME} has stopped due to the pipe being closed.")


if __name__ == "__main__":
    run()
