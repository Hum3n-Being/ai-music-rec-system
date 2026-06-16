import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
import sounddevice as sd
import soundfile as sf

import commoConstants as cc
"""

Typical Usage:

"""


class AudioFileInfo:
    """ Class used to seperate Audio Files and contains nessary 
    information to define the spectagram. Use for single audio files

    Public Choices and States:

    Instance Variables:
    """
    def __init__(self, __fileName: str, waveform: np.ndarray, sample_rate: int):
        """ Constructore to intialize a audio file and its information """
        self.__fileName = __fileName
        self.waveform = waveform
        self.sample_rate = sample_rate

        #  Fast Fourier Transform (FFT)
        fft_data = np.fft.rfft(waveform)
        fft_freqs = np.fft.rfftfreq(len(waveform), d=1/sample_rate)

        # Calcuate maximal frequency
        magnitude = np.abs(fft_data)
        peak_index = np.argmax(magnitude)
        self.frequency = fft_freqs[peak_index]
    # --GETTERS---------------------------------------------------
    @property
    def _fileName(self):
        """ The read-only of the file name of the audio file. """
        return self.__fileName
    @property
    def waveform(self):
        """ The read-only of the audio file's . """
        return self.waveform
    @property
    def sample_rate(self):
        """ The read-only of the audio file's . """
        return self.sample_rate
    @property
    def frequency(self):
        """ The read-only of the audio file's . """
        return self.frequency


class Pitch_Classification:
    """
    """
    def __init__(self):
        """ Intilaize a dictionary of pitch notes with an empty list.
        The values are  AudioFileInfo objects
        """
        self._audioFilesList = {
            "A-1" : [],
            "A#-1" : [],
            "B-1" : [],
            "C0" : [],
            "C#0" : [],
            "D0" : [],
            "D#0" : [],
            "E0" : [],
            "F0" : [],
            "F#0" : [],
            "G0" : [],
            "G#0" : [],
            "A0" : [],
            "A#0" : [],
            "B0" : [],
            "C1" : [],
            "C#1" : [],
            "D1" : [],
            "D#1" : [],
            "E1" : [],
            "F1" : [],
            "F#1" : [],
            "G1" : [],
            "G#1" : [],
            "A2" : [],
            "A#2" : [],
            "B2" : [],
            "C2" : [],
            "C#2" : [],
            "D2" : [],
            "D#2" : [],
            "E2" : [],
            "F2" : [],
            "F#2" : [],
            "G2" : [],
            "G#3" : [],
            "A3" : [],
            "A#3" : [],
            "B3" : [],
            "C3" : [],
            "C#3" : [],
            "D3" : [],
            "D#3" : [],
            "E3" : [],
            "F3" : [],
            "F#3" : [],
            "G3" : [],
            "G#3" : [],
            "A4" : [],
            "A#4" : [],
            "B4" : [],
            "C4" : [],
            "C#4" : [],
            "D4" : [],
            "D#4" : [],
            "E4" : [],
            "F4" : [],
            "F#4" : [],
            "G4" : [],
            "G#4" : [],
            "A5" : [],
            "A#6" : [],
            "B6" : [],
            "C6" : [],
            "C#6" : [],
            "D5" : [],
            "D#5" : [],
            "E5" : [],
            "F5" : [],
            "F#5" : [],
            "G5" : [],
            "G#5" : [],
            "A6" : [],
            "A#7" : [],
            "B7" : [],
            "C7" : [],
            "C#6" : [],
            "D6" : [],
            "D#6" : [],
            "E6" : [],
            "F6" : [],
            "F#6" : [],
            "G6" : [],
            "G#6" : [],
            "A7" : [],
            "A#7" : [],
            "B7" : [],
            "C7" : [],
            "MIX" : [],
            "LIVE" : [],
        }
    @property
    def audioFilesList(self) -> dict:
        """The read-only the classification of audio files."""
        return self.__audioFilesList
    
    def addPitchClassification(self, file_name: str, waveform: np.ndarray, 
                                                        sample_rate:int):
        """
        @pre file_name has already been discovered to be an audio file
        """
        start_index = file_name.find("_") + 1
        end_index = file_name.find(".")

        # Slice the string between those positions
        pitchNote = file_name[start_index:end_index]
        fileExtension = file_name[end_index::]

        #Create
        audio_info = AudioFileInfo(file_name, waveform, sample_rate)
        if pitchNote in audioFilesList():
            audioFilesList()[pitchNote].append();
        else:
            audioFilesList()["MIX"].append();
            

        return self.__audioFilesList