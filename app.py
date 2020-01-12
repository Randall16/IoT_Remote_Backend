from flask import Flask, abort, request

from remote import Button, send_signal
from api_keys import VALID_KEYS

app = Flask(__name__)

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

        send_signal(Button.VOLUME_UP, presses)
    elif button == 'VOLUME_DOWN':
        presses = 1
        json = request.get_json()
        if json != None:
            presses = json.get('presses', 1)

        send_signal(Button.VOLUME_DOWN, presses)
    elif button == 'POWER':
        send_signal(Button.POWER)
    elif button == 'MUTE':
        send_signal(Button.MUTE)
    elif button == 'INPUT':
        send_signal(Button.INPUT)
    elif button == 'CHANNEL_UP':
        send_signal(Button.CHANNEL_UP)
    elif button == 'CHANNEL_DOWN':
        send_signal(Button.CHANNEL_DOWN)
    elif button == 'SELECT':
        send_signal(Button.SELECT)
    elif button == 'UP':
        send_signal(Button.UP)
    elif button == 'DOWN':
        send_signal(Button.DOWN)
    elif button == 'LEFT':
        send_signal(Button.LEFT)
    elif button == 'RIGHT':
        send_signal(Button.RIGHT)
    elif button == 'ZERO':
        send_signal(Button.ZERO)
    elif button == 'ONE':
        send_signal(Button.ONE)
    elif button == 'TWO':
        send_signal(Button.TWO)
    elif button == 'THREE':
        send_signal(Button.THREE)
    elif button == 'FOUR':
        send_signal(Button.FOUR)
    elif button == 'FIVE':
        send_signal(Button.FIVE)
    elif button == 'SIX':
        send_signal(Button.SIX)
    elif button == 'SEVEN':
        send_signal(Button.SEVEN)
    elif button == 'EIGHT':
        send_signal(Button.EIGHT)
    elif button == 'NINE':
        send_signal(Button.NINE)
    else:
        return abort(400)


    return '%s sent' % button


# Run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True) 