# Projeto tocador

from pathlib import Path
from playsound3 import playsound
import random

folder = Path(__file__).parent / 'music'
library = list(folder.glob('*.mp3'))

if len(library) == 0:
    print('Sorry, no songs available in the folder music :(')
else:
    song = random.choice(library)
    print(f'Playing {song.stem.replace('_',' ')} ...')
    playsound(song)
    print('End.')