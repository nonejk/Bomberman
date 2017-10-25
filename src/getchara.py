""" getting input from user
"""
from __future__ import print_function
import signal
import sys

class get_chara:
    """ getting input from user
    """
    # getting a single character from stdin
    def __init__(self):
        self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


class _GetchUnix:
    """ getting input from user
    """
    def __init__(self):
        import tty

    def __call__(self):
        import tty
        import termios
        file_descriptor = sys.stdin.fileno()
        old_settings = termios.tcgetattr(file_descriptor)
        try:
            tty.setraw(sys.stdin.fileno())
            character = sys.stdin.read(1)
        finally:
            termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_settings)
        return character

class AlarmException(Exception):
    """ handling exceptions
    """
    def __init__(self):
        pass
    pass


def alarm_handler(signum, frame):
    """ handling alarms
    """
    raise AlarmException


class nonBlockingCharInput:
    """ getting input from user
    """
    def __init__(self):
        pass

    global timeLimit
    timeLimit = 1

    def __call__(self):
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.alarm(timeLimit)
        try:
            text = get_chara()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''
