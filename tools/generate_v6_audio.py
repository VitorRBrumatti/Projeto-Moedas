"""Original short military march and weapon reports, synthesized locally without APIs."""
from pathlib import Path
import math
import random
import struct
import wave

RATE = 22050
OUT = Path(__file__).resolve().parents[1] / 'assets/v6'


def write(name, samples):
    peak = max(1, max(abs(s) for s in samples))
    with wave.open(str(OUT / (name + '.wav')), 'wb') as stream:
        stream.setparams((1, 2, RATE, 0, 'NONE', 'not compressed'))
        stream.writeframes(b''.join(struct.pack('<h', int(s / peak * 26000)) for s in samples))


def main():
    rng = random.Random(601)
    melody = [62, 62, 69, 69, 67, 66, 64, 62, 66, 66, 71, 69, 67, 66, 64, 62,
              62, 66, 69, 74, 73, 71, 69, 66, 67, 71, 69, 66, 64, 61, 62, 62]
    samples = []
    for i in range(RATE * 16):
        t = i / RATE
        beat = t % .5
        sub = t % .125
        note = melody[min(31, int(t * 2))]
        f = 440 * 2 ** ((note - 69) / 12)
        envelope = min(1, beat * 55) * min(1, (.5 - beat) * 14)
        brass = sum(math.sin(math.tau * f * h * t) / h for h in (1, 2, 3, 4)) * .22 * envelope
        snare = rng.uniform(-1, 1) * math.exp(-sub * 55) * (.28 if int(t * 8) % 4 == 2 else .08)
        drum = math.sin(math.tau * (65 * beat - 22 * beat * beat)) * math.exp(-beat * 16) * .4
        samples.append(brass + snare + drum)
    write('menu-march', samples)
    for name, hz, duration in [('shot-glock', 150, .1), ('shot-minigun', 95, .07)]:
        samples = [(rng.uniform(-1, 1) * .6 + math.sin(math.tau * hz * i/RATE) * .4)
                   * math.exp(-i/RATE * 50) for i in range(int(RATE*duration))]
        write(name, samples)


if __name__ == '__main__':
    main()
