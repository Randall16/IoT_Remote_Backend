import time
from flask import Flask, abort, request
from threading import Lock

import config
from remote import RemoteButton, send_signal

# Globals
app = Flask(__name__)
lock = Lock()
MINIMUM_TIME_BETWEEN_SIGNALS = 0.08


# Functions
def press_button(button: RemoteButton):
    # Using a lock because to ensure only one signal is being sent at a time
    lock.acquire()
    send_signal(button)
    time.sleep(MINIMUM_TIME_BETWEEN_SIGNALS)
    lock.release()


@app.route('/api/<button>', methods=['POST'])
def handle_button(button: str):

    # Authenticate request
    request_api_key = request.headers.get('x-api-key', '')
    if request_api_key not in config.VALID_KEYS:
        return abort(401)
    
    # Ensure button is given
    if button == None:
        return abort(400)

    # Simplify button conversions by uppercasing
    button = button.upper()

    # Handle the button
    press_button(RemoteButton[button])

    return button + ' was successfully sent!'


# Run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0')