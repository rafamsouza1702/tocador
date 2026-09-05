# Projeto tocador

from pathlib import Path
from playsound3 import playsound
import random

pasta=Path(__file__).parent / 'musicas'
library=list(pasta.glob('*.mp3'))
tocar=random.choice(library)

print(f'Tocando {tocar.stem}...')
playsound(tocar)
print('Fim.')