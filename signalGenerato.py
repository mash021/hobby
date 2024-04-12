import pyaudio
import numpy as np
import tkinter as tk

# تنظیمات صوتی setting Audio
SAMPLE_RATE = 32000
BUFFER_SIZE = 256


# تعریف موج‌ها define wave type
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
        
# تابع برای پخش نت (play note)
def play_note():
    frequency = float(note_frequency.get())
    duration = float(note_duration.get())
    wave_type = wave_type_var.get()

    wave_generator = WaveGenerator(wave_type)
    samples = wave_generator.generate_wave(frequency, duration)

    # تعریف و شروع Stream
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=SAMPLE_RATE, output=True)
    stream.write(samples.astype(np.float32).tobytes())

    # متوقف کردن و بستن Stream
    stream.stop_stream()
    stream.close()
    p.terminate()

