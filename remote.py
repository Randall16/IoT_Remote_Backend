import subprocess
from enum import Enum

COMMAND = 'irsend'
FLAG1 = 'SEND_ONCE'
TV_NAME = 'sony'

class RemoteButton(Enum):
    POWER = 'KEY_POWER'
    INPUT = 'KEY_KBDINPUTASSIST_ACCEPT'
    VOLUME_UP = 'KEY_VOLUMEUP'
    VOLUME_DOWN = 'KEY_VOLUMEDOWN'
    CHANNEL_UP = 'KEY_CHANNELUP'
    CHANNEL_DOWN = 'KEY_CHANNELDOWN'
    ZERO = 'KEY_NUMERIC_0'
    ONE = 'KEY_NUMERIC_1'
    TWO = 'KEY_NUMERIC_2'
    THREE = 'KEY_NUMERIC_3'
    FOUR = 'KEY_NUMERIC_4'
    FIVE = 'KEY_NUMERIC_5'
    SIX = 'KEY_NUMERIC_6'
    SEVEN = 'KEY_NUMERIC_7'
    EIGHT = 'KEY_NUMERIC_8'
    NINE = 'KEY_NUMERIC_9'
    UP = 'KEY_UP'
    DOWN = 'KEY_DOWN'
    RIGHT = 'KEY_RIGHT'
    LEFT = 'KEY_LEFT'
    SELECT = 'KEY_SELECT'
    MUTE = 'KEY_MUTE'


def send_signal(button: RemoteButton):
    # Create Bash command
    # button.value is appended three times because IR signal needs to be bursted
    # NOTE this varies from TV to TV so some will only it to be appended once
    command = [COMMAND, FLAG1, TV_NAME, button.value, button.value, button.value]
    subprocess.run(command)
