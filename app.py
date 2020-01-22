import time, queue, threading
from flask import Flask, abort, request

from remote import Button, send_signal
from api_keys import VALID_KEYS


app = Flask(__name__)
queue = queue.Queue()

def press_button(button: Button, reps: int=0):
    queue.put(button)

@app.route('/api/<button>', methods=['POST'])
def handle_button(button: str):

    # Authenicate request
    request_api_key = request.headers.get('x-api-key', '')
    if request_api_key not in VALID_KEYS:
        return abort(401)
    
    # Ensure button is given
    if button == None:
        return abort(400)

    # Simplify button conversions by uppercasing
    button = button.upper()

    # Handle the button
    if button == 'VOLUME_UP':
        presses = 1
        json = request.get_json()
        if json != None:
            presses = json.get('presses', 1)

        press_button(Button.VOLUME_UP, presses)
    elif button == 'VOLUME_DOWN':
        presses = 1
        json = request.get_json()
        if json != None:
            presses = json.get('presses', 1)

        press_button(Button.VOLUME_DOWN, presses)
    elif button == 'POWER':
        press_button(Button.POWER)
    elif button == 'MUTE':
        press_button(Button.MUTE)
    elif button == 'INPUT':
        press_button(Button.INPUT)
    elif button == 'CHANNEL_UP':
        press_button(Button.CHANNEL_UP)
    elif button == 'CHANNEL_DOWN':
        press_button(Button.CHANNEL_DOWN)
    elif button == 'SELECT':
        press_button(Button.SELECT)
    elif button == 'UP':
        press_button(Button.UP)
    elif button == 'DOWN':
        press_button(Button.DOWN)
    elif button == 'LEFT':
        press_button(Button.LEFT)
    elif button == 'RIGHT':
        press_button(Button.RIGHT)
    elif button == 'ZERO':
        press_button(Button.ZERO)
    elif button == 'ONE':
        press_button(Button.ONE)
    elif button == 'TWO':
        press_button(Button.TWO)
    elif button == 'THREE':
        press_button(Button.THREE)
    elif button == 'FOUR':
        press_button(Button.FOUR)
    elif button == 'FIVE':
        press_button(Button.FIVE)
    elif button == 'SIX':
        press_button(Button.SIX)
    elif button == 'SEVEN':
        press_button(Button.SEVEN)
    elif button == 'EIGHT':
        press_button(Button.EIGHT)
    elif button == 'NINE':
        press_button(Button.NINE)
    else:
        return abort(400)

    return '%s sent' % button



def handle_signals():
    while True:
        if not queue.empty():
            button = queue.get()
            send_signal(button)
            time.sleep(0.1)

# Run the app
if __name__ == "__main__":
    thread = threading.Thread(target=handle_signals)
    thread.start()
    app.run(host='0.0.0.0', debug=True)