# Projeto tocador

from pathlib import Path
from playsound3 import playsound
import random

folder=Path(__file__).parent / 'music'
library=list(folder.glob('*.mp3'))
song=random.choice(library)

print(f'Playing {song.stem} ...')
playsound(song)
print('End.')