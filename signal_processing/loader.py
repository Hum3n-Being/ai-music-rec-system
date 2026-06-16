import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
import sounddevice as sd
import soundfile as sf

from Pitch_Classification import audioFileData

import commoConstants as cc
"""

Typical Usage:

"""

pClass = audioFileData()


# Points to your audio directory reliably on any machine
AUDIO_DIR = c.BASE_DIR / "audioriectory"
class AudioDirectory:
    """Class to deal with Aduio Files in a set directory and
    """
    def __init__(self):
        self.__audio_file_path = pClass.AUDIO_DIR
        self.__audioFilesList = pClass.Pitch_Classification()

    @property
    def _audio_file_path(self) -> str:
        """The read-only name of the audio directory."""
        return self.__audio_file_path
    @property
    def _audioFilesList(self) -> list:
        """The read-only list of tracked audio file data."""
        return self.__audioFilesList
    
    # Adds file name and infor to the 
    def _addAudioFile(self, file_name: str, waveform: np.ndarray, 
                                                        sample_rate:int):
        audioFilesList().addFile(file_name, waveform, sample_rate)
    #
    def load_file():
        a = None        #TODO


##TODO INPERATE
# defualt 22,050 HZ --. help spead up 
# no
# orignla files without reworking to mono
waveform, sample_rate = librosa.load(file_name, sr=None, mono=False)

# calculate the Short-Time Fourier Transform
stft = librosa.stft (waveform)

# Convert the amplitude values to decbels
spectrogram = librosa.amplitude_to_db(np.abs (stft))

# Create a window
plt.figure(figsize=(10, 4))

# display the spectrogram as an image
librosa.display.specshow(spectrogram, sr=sample_rate, x_axis='time', y_axis='log')

# Add a colorbar
plt.colorbar()

# Add title
plt.title("Spectogram")

#Adjust layout
plt.tight_layout()

#Display the plot
plt.show()


""" Main Fuction

"""
if __name__ == "__main__":
    #TODO
    a = None