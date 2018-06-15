import wl_to_rgb as wl
import wave
from numpy import fft

#LOOP
#1. Create a function to get an audio spectrum from some kind of noise snippet (FFT)

#2. Map audio spectrum onto visible light spectrum

#3. Get RGB values for each wavelength.

#4. Show color spectrum of music
#END LOOP

audioFile = "http://www.moviewavs.com/0093677609/WAVS/TV_Shows/Simpsons/flanders__donefor.wav"
audio = wave.open(audioFile,'r')


#rgb = wl.wavelength_to_rgb()

print('End.')