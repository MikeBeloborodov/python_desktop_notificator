import os
import sys
import time

from notifypy import Notify

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    try:
        sys.argv[1]
        time.sleep(int(sys.argv[1]))
    except Exception:
        time.sleep(180)
    notification = Notify()
    notification.title = "Notification!"
    notification.message = "Notification!"
    notification.audio = ROOT_DIR + "/sound.wav"

    notification.send()


if __name__ == "__main__":
    main()
