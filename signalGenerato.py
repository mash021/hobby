import pyaudio
import numpy as np
import tkinter as tk

# تنظیمات صوتی
SAMPLE_RATE = 32000
BUFFER_SIZE = 256


# تعریف موج‌ها
class WaveGenerator:
    def __init__(self, wave_type):
        self.wave_type = wave_type

    def generate_wave(self, frequency, duration):
        t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
        if self.wave_type == 'sine':
            return np.sin(2 * np.pi * frequency * t)
        elif self.wave_type == 'triangle':
            return np.abs(2 * np.pi * frequency * t - 2 * np.pi * frequency * t)
        elif self.wave_type == 'square':
            return np.sign(np.sin(2 * np.pi * frequency * t))
