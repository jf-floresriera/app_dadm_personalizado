import wave, struct, math
import os

def make_sound(file_name, freq, duration, volume=32767.0):
    sample_rate = 44100
    n_samples = int(duration * sample_rate)
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with wave.open(file_name, 'w') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sample_rate)
        for i in range(n_samples):
            # Onda senoidal simple (Beep)
            value = int(volume * math.sin(2 * math.pi * freq * i / sample_rate))
            data = struct.pack('<h', value)
            w.writeframesraw(data)

# Sonidos para RETO_5 y App Personalizada (Clásico)
make_sound('app/src/main/res/raw/sword.wav', 440, 0.15) # Tono 1 (X)
make_sound('app/src/main/res/raw/swish.wav', 660, 0.15) # Tono 2 (O)

# Sonidos adicionales para App Personalizada
make_sound('app/src/main/res/raw/wave_sound.wav', 300, 0.3)
make_sound('app/src/main/res/raw/seagull_sound.wav', 880, 0.3)
make_sound('app/src/main/res/raw/harp_sound.wav', 500, 0.2)
make_sound('app/src/main/res/raw/cuatro_sound.wav', 550, 0.2)
make_sound('app/src/main/res/raw/whip_sound.wav', 700, 0.15)
make_sound('app/src/main/res/raw/banjo_sound.wav', 400, 0.25)
print("Sonidos generados exitosamente.")