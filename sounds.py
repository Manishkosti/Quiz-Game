"""
Cross‑platform sound helpers.
Falls back silently if winsound (Windows‑only) isn’t available.
"""

import time, sys

try:
    import winsound
    _BEEP = winsound.Beep
except ImportError:  # non‑Windows
    def _BEEP(freq, dur):
        pass  # no‑op

def _tone(freq: int, dur: int):
    _BEEP(freq, dur)
    time.sleep(dur / 1000)

def play_welcome_sound():
    _tone(2000, 400); _tone(2600, 400)

def play_correct_sound():
    _tone(2500, 300)

def play_wrong_sound():
    _tone(800, 600)
