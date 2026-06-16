
import numpy as np
from pathlib import Path
 
""" A List of commonly used variables and functions
 
Typical Usecases:
    import commoConstants as cc
    freq = cc.PITCH_MAP["A4"]   # 440.0
    freq = cc.getFrequency("C4")

Notes:
    Repredntation of Sharps and Flats with be shortedn to s and b
    (i.e. C Sharp is represented in strings like C#, but variable name
    can be "Cs" and C flat can be represented like "Cb" as a string,
    which is similar to Cb) 
"""
 
# Directory where the {FOLDERPATH}/ai-music-rec-system project is stored
BASE_DIR = Path(__file__).parent.parent.parent  
 
# ========================= OCTAVE RANGES =========================
#range of hearable octaves from Tools (i.e Garage Band)
__neg1 = -1
__zero = 0
__one = 1
__two = 2
__three = 3
__four = 4
__five = 5
__six = 6
__seven = 7
 
OCTAVE_RANGE = [
    __neg1, __zero, __one, __two, __three,
    __four, __five, __six, __seven
]
 
OCTAVE_RANGE_STR_TO_INT = {
    "-1": -1, "0": 0, "1": 1, "2": 2,
    "3": 3,  "4": 4, "5": 5, "6": 6, "7": 7
}
 
# ========================= NOTE VALUES =========================
__CNoteVal  = 0
__CsNoteVal = 1
__DNoteVal  = 2
__DsNoteVal = 3
__ENoteVal  = 4
__FNoteVal  = 5
__FsNoteVal = 6
__GNoteVal  = 7
__GsNoteVal = 8
__ANoteVal  = 9
__AsNoteVal = 10
__BNoteVal  = 11
 
NOTE_NAMES = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
 
NOTE_INDEX_RANGE = [
    __CNoteVal, __CsNoteVal, __DNoteVal, __DsNoteVal,
    __ENoteVal, __FNoteVal, __FsNoteVal, __GNoteVal,
    __GsNoteVal, __ANoteVal, __AsNoteVal, __BNoteVal
]
 
# ========================= INSTRUMENT NAMES =========================
# instrument shortc to full name
pn    = "piano"
fl    = "flute"
cl     = "clarinet"
vn   = "violin"
vn1   = "violin 1"
vn2   = "violin 2"
va    = "va"
db  = "double bass"
vc = "cello"
bs     = "bass"
cb = "contrabass"
# Map from shorten name to instrument names
INSTRUMENT_NAMES = {
    "pn": pn,
    "fl": fl,
    "cl": cl,
    "vn": vn,
    "va": va,
    "db": db,
    "vc": vc,
    "vlc": vc,
    "bs": bs,
    "b": bs,
    "cb": cb,
}

INSTRUMENT_SHORTCUT = {
    pn: "pn",
    fl: "fl",
    cl: "cl",
    vn: "vn",
    va: "va",
    db: "db",
    vc: "c",
    bs: "b",
    cb: "cb",
}
""" ========================= PITCH NAMES ========================= """
AnegOne = "A-1"             # = 13.75 HZ
ASharpNegOne = "A#-1"       # = HZ
BnegOne = "B-1"             #= HZ
# OCTAVE RANGE 0
CZero = "C0"
CSharpZero = "C#0"          # = HZ
DZero = "D0"
DSharpZero = "D#0"          # = HZ
EZero = "E0"
FZero = "F0"
FSharpZero = "F#0"          # = HZ
GZero = "G0"
GSharpZero = "G#0"          # = HZ
AZero = "A0"
ASharpZero = "A#0"          # = HZ
BZero = "B0"
#---OCTAVE RANGE 1
COne = "C1"
CSharpOne = "C#1"          # = HZ
DOne = "D1"
DSharpOne = "D#1"          # = HZ
EOne = "E1"
FOne = "F1"
FSharpOne = "F#1"          # = HZ
GOne = "G1"
GSharpOne = "G#1"          # = HZ
AOne = "A1"
ASharpOne = "A#1"          # = HZ
BOne = "B1"
#---OCTAVE RANGE 2
CTwo = "C2"
CSharpTwo = "C#2"          # = HZ
DTwo = "D2"
DSharpTwo = "D#2"          # = HZ
ETwo = "E2"
FTwo = "F2"
FSharpTwo = "F#2"          # = HZ
GTwo = "G2"
GSharpTwo = "G#2"          # = HZ
ATwo = "A2"
ASharp = "A#2"              # = HZ
BTwo = "B2"
#---OCTAVE RANGE 3
CThree = "C3"
CSharpThree = "C#3"          # = HZ
DThree = "D3"
DSharpThree = "D#3"          # = HZ
EThree = "E3"
FThree = "F3"
FSharpThree = "F#3"          # = HZ
GThree = "G3"
GSharpThree = "G#3"
AThree = "A3"
ASharpThree = "A#3"          # = HZ
BThree = "B3"
#---OCTAVE RNAGE 4
CFour = "C4"
CSharpFour = "C#4"          # = HZ
DFour = "D4"
DSharpFour = "D#4"          # = HZ
EFour = "E4"
FFour = "F4"
FSharpFour = "F#4"          # = HZ
GFour = "G4"
GSharpFour = "G#4"          # = HZ
AFour = "A4"
ASharpFour = "A#4"          # = HZ
BFour = "B4"
#---OCTAVE RANGE 5
CFive = "C5"
CSharpFive = "C#5"          # = HZ
DFive = "D5"
DSharpFive = "D#5"          # = HZ
EFive = "E5"
FFive = "F5"
FSharpFive = "F#5"          # = HZ
GFive = "G5"
GSharpFive = "G#5"          # = HZ
AFive = "A5"
ASharpFive = "A#5"          # = HZ
BFive = "B5"
#---OCTAVE RANGE 6
CSix = "C"
CSharpSix = "C#6"          # = HZ
DSix = "D6"
DSharpSix = "D#6"          # = HZ
ESix = "E6"
FSix = "F6"
FSharpSix = "F#6"          # = HZ
GSix = "G6"
GSharpSix = "G#6"          # = HZ
ASix = "A6"
ASharpSix = "A#6"           # = HZ
BSix = "B6"                 # = 1975.533205024496 Hz
#---OCTAVE  RANGE 7
CSeven = "C7"               # = 2093.004522404789 Hz


""" ===================== PITCH FREQUENCIES ====================== """
#Frequnies mesaudeed in Hertz correspoing to its Pitch class/Note value
# Using the 12-Tone E,
# The formulas to caluate each are:
#
def __CalculateFrequency(octave: int, note_index:int):
    """
    """
    octave = np.asarray(octave, dtype=np.int32)
    note_index = np.asarray(note_index, dtype=np.int32)
    AFour = 440.0
    
    # Calculate distance in semitones from A4
    A4_OCTAVE = four
    octave_diff = octave - A4_OCTAVE
    note_diff = note_index - __ANoteVal
    n = (octave_diff * 12) + note_diff
            
    # Apply the equal temperament frequency formula using NumPy's power function
    # explicitly using float64 for precision
    exponent = np.power(2.0, n / 12.0, dtype=np.float64)
    frequency = AFour * exponent
    
    return frequency

#  MAPS
PITCH_MAP = {}

# Handle the special partial octave (-1) which only has A, A#, B
for note_idx in [9, 10, 11]:  # A, A#, B
    note_name = f"{NOTE_NAMES[note_idx]}-1"
    PITCH_MAP[note_name] = __CalculateFrequency(neg1, note_idx)

# Handle octaves 0 through 6 (Full chromatic scales)
for octave in range(0, 7):
    for note_idx, name in enumerate(NOTE_NAMES):
        note_name = f"{name}{octave}"
        
        # Hardcode A4 to exactly 440.0 as per your original requirement
        if octave == 4 and name == "A":
            PITCH_MAP[note_name] = 440.0
        else:
            PITCH_MAP[note_name] = __CalculateFrequency(octave, note_idx)

# Handle the final octave (7) which only needs C7
PITCH_MAP["C7"] = __CalculateFrequency(__seven, 0)

def _getFreceny(pitch):
    """
    """
    if pitch in PITCH_MAP:
        return PITCH_MAP[pitch]
    return None

def frequencyToNote(frequency: float, tolerance: float = 1.0) -> str | None:
    """Find the closest note name for a given frequency (Hz).
    Returns None if no note is within tolerance semitones.
    """
    if frequency <= 0:
        return None
    closest_note = None
    closest_diff = float("inf")
    for note_name, freq in PITCH_MAP.items():
        diff = abs(freq - frequency)
        if diff < closest_diff:
            closest_diff = diff
            closest_note = note_name
    return closest_note
 

""" ============================== TEST ============================== """

def main():
    print("\t\t\t NUMPY EQUAL TEMPERAMENT FREQUENCY CALUCATION\n")

    # Grouping the notes by octave so it looks clean in the terminal
    octaves_to_print = ["-1", "0", "1", "2", "3", "4", "5", "6", "7"]

    for octave in octaves_to_print:
        print(f"\n--- OCTAVE RANGE {octave} ---")

        for note_name, frequency in PITCH_MAP.items():
            # Cleanly handle negative one vs positive one
            if octave == "-1" and note_name.endswith("-1"):
                print(f"{note_name:<5} = {frequency} Hz")
            elif octave != "-1" and note_name.endswith(octave) and "-" not in note_name:
                print(f"{note_name:<5} = {frequency} Hz")


if __name__ == "__main__":
    main()

"""REDULT


--- OCTAVE RANGE -1 ---
A-1   = 13.75 Hz
A#-1  = 14.567617547440307 Hz
B-1   = 15.433853164253883 Hz

--- OCTAVE RANGE 0 ---
C0    = 16.351597831287414 Hz
C#0   = 17.323914436054505 Hz
D0    = 18.354047994837977 Hz
D#0   = 19.445436482630058 Hz
E0    = 20.601722307054366 Hz
F0    = 21.826764464562746 Hz
F#0   = 23.12465141947715 Hz
G0    = 24.499714748859326 Hz
G#0   = 25.956543598746574 Hz
A0    = 27.5 Hz
A#0   = 29.13523509488062 Hz
B0    = 30.86770632850775 Hz

--- OCTAVE RANGE 1 ---
C1    = 32.70319566257483 Hz
C#1   = 34.64782887210901 Hz
D1    = 36.70809598967594 Hz
D#1   = 38.890872965260115 Hz
E1    = 41.20344461410875 Hz
F1    = 43.653528929125486 Hz
F#1   = 46.2493028389543 Hz
G1    = 48.999429497718666 Hz
G#1   = 51.91308719749314 Hz
A1    = 55.0 Hz
A#1   = 58.27047018976124 Hz
B1    = 61.7354126570155 Hz

--- OCTAVE RANGE 2 ---
C2    = 65.40639132514966 Hz
C#2   = 69.29565774421802 Hz
D2    = 73.41619197935188 Hz
D#2   = 77.78174593052023 Hz
E2    = 82.4068892282175 Hz
F2    = 87.30705785825097 Hz
F#2   = 92.4986056779086 Hz
G2    = 97.99885899543733 Hz
G#2   = 103.82617439498628 Hz
A2    = 110.0 Hz
A#2   = 116.54094037952248 Hz
B2    = 123.47082531403103 Hz

--- OCTAVE RANGE 3 ---
C3    = 130.8127826502993 Hz
C#3   = 138.59131548843604 Hz
D3    = 146.8323839587038 Hz
D#3   = 155.56349186104046 Hz
E3    = 164.81377845643496 Hz
F3    = 174.61411571650194 Hz
F#3   = 184.9972113558172 Hz
G3    = 195.99771799087463 Hz
G#3   = 207.65234878997256 Hz
A3    = 220.0 Hz
A#3   = 233.08188075904496 Hz
B3    = 246.94165062806206 Hz

--- OCTAVE RANGE 4 ---
C4    = 261.6255653005986 Hz
C#4   = 277.1826309768721 Hz
D4    = 293.6647679174076 Hz
D#4   = 311.1269837220809 Hz
E4    = 329.6275569128699 Hz
F4    = 349.2282314330039 Hz
F#4   = 369.9944227116344 Hz
G4    = 391.99543598174927 Hz
G#4   = 415.3046975799451 Hz
A4    = 440.0 Hz
A#4   = 466.1637615180899 Hz
B4    = 493.8833012561241 Hz

--- OCTAVE RANGE 5 ---
C5    = 523.2511306011972 Hz
C#5   = 554.3652619537442 Hz
D5    = 587.3295358348151 Hz
D#5   = 622.2539674441618 Hz
E5    = 659.2551138257398 Hz
F5    = 698.4564628660078 Hz
F#5   = 739.9888454232688 Hz
G5    = 783.9908719634985 Hz
G#5   = 830.6093951598903 Hz
A5    = 880.0 Hz
A#5   = 932.3275230361799 Hz
B5    = 987.7666025122483 Hz

--- OCTAVE RANGE 6 ---
C6    = 1046.5022612023945 Hz
C#6   = 1108.7305239074883 Hz
D6    = 1174.6590716696303 Hz
D#6   = 1244.5079348883237 Hz
E6    = 1318.5102276514797 Hz
F6    = 1396.9129257320155 Hz
F#6   = 1479.9776908465376 Hz
G6    = 1567.981743926997 Hz
G#6   = 1661.2187903197805 Hz
A6    = 1760.0 Hz
A#6   = 1864.6550460723597 Hz
B6    = 1975.533205024496 Hz

--- OCTAVE RANGE 7 ---
C7    = 2093.004522404789 Hz
    
"""