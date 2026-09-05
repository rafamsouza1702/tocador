# Projeto tocador

from pathlib import Path
from playsound3 import playsound
import random

folder = Path(__file__).parent / 'music'
library = list(folder.glob('*.mp3'))
random.shuffle(library)
number_of_songs=len(library)

if number_of_songs == 0:
    print('Sorry, no songs available in the folder music :(')
else:
    for song in library:
        counter=int(1)
        print(f'\nPlaying {counter} of {number_of_songs} ...\n{song.stem.replace('_',' ')}')
        playsound(song)
        counter=counter+1
    print('End.')