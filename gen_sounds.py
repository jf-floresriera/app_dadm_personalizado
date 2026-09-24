import wave, struct, math
import os

def make_melody(file_name, notes, volume=32767.0):
    sample_rate = 44100
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with wave.open(file_name, 'w') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sample_rate)
        for freq, duration in notes:
            n_samples = int(duration * sample_rate)
            for i in range(n_samples):
                # Onda cuadrada mezclada con senoidal para que suene un poco mejor (estilo 8-bits retro)
                sine = math.sin(2 * math.pi * freq * i / sample_rate)
                value = int(volume * 0.5 * (sine + (1 if sine > 0 else -1)))
                data = struct.pack('<h', value)
                w.writeframesraw(data)

# Melodía de Victoria (Arpegio Mayor Feliz)
make_melody('app/src/main/res/raw/win_sound.wav', [(440, 0.1), (554, 0.1), (659, 0.3)])

# Melodía de Derrota (Notas descendentes tristes)
make_melody('app/src/main/res/raw/lose_sound.wav', [(440, 0.2), (415, 0.2), (392, 0.4)])

# Sonido de Empate (Tono neutro)
make_melody('app/src/main/res/raw/tie_sound.wav', [(300, 0.3)])

print("Sonidos de fin de juego generados exitosamente.")