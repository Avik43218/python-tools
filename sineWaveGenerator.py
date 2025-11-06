import math
import numpy
import sounddevice as sd

class sineWaveGenerator:

    def __init__(self, amplitude, baseFrequency, duration, sampleRate=44100):
        self.amplitude = amplitude
        self.baseFrequency = baseFrequency
        self.duration = duration
        self.sampleRate = sampleRate
        self.pi = math.pi

    def generateWave(self, phase, freqDeviation, modFrequency):
        timeValues = numpy.linspace(0, self.duration, int(self.sampleRate * self.duration), endpoint=False)
        
        if freqDeviation > 0 and modFrequency > 0:
            instantaneousFreq = self.baseFrequency + freqDeviation * numpy.sin(2 * self.pi * modFrequency * timeValues)
        else:
            instantaneousFreq = numpy.full_like(timeValues, self.baseFrequency)

        phase_over_time = 2 * numpy.pi * numpy.cumsum(instantaneousFreq) / self.sampleRate
        
        wave = self.amplitude * numpy.sin(phase_over_time + phase)
        return wave.astype(numpy.float32)
        
    def __repr__(self):
        return f"Representing a sine wave with amplitude: {self.amplitude}, and frequency: {self.frequency}"
    

if __name__ == "__main__":

    amplitude = float(input("Enter amplitude of the wave: "))
    base_frequency = float(input("Enter base frequency of the wave (in Hz): "))
    frequency_deviation = float(input("Enter frequency deviation (+/- Hz): "))
    mod_frequency = float(input("Enter modulation frequency (Hz): "))
    duration = float(input("Enter duration (in s): "))

    phase1 = 0
    phase2 = math.radians(60)
    phase3 = math.radians(120)

    generator = sineWaveGenerator(amplitude, base_frequency, duration)

    wave1 = generator.generateWave(phase1, frequency_deviation, mod_frequency)
    wave2 = generator.generateWave(phase2, frequency_deviation + 5, mod_frequency + 1)
    wave3 = generator.generateWave(phase3, frequency_deviation + 8, mod_frequency + 2)

    combined_wave = wave1 + wave2 + wave3 / 3.0

    print("Playing Sound...")
    sd.play(combined_wave, samplerate=generator.sampleRate)
    sd.wait()
    print("Done!")
