# 🎵 Tocador

> 🇧🇷 [Leia em português](README.pt-BR.md)

A command-line random music player. Picks a random `.mp3` file from a
local folder and plays it.

A Python learning project, built incrementally: each version introduces
a new language concept.

## Current state

**v1 — Simple shuffle.** Reads the `.mp3` files from the `musicas/`
folder, picks one at random and plays it through to the end.

## Requirements

- Python 3.11+
- macOS, Linux or Windows (playback uses the native system player)

## Installation

```bash
git clone git@github.com:rafamsouza1702/tocador.git
cd tocador

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

## Usage

Create the music folder and drop your `.mp3` files into it:

```bash
mkdir music
```

Run it:

```bash
python tocador.py
```

Expected output:

```
Tocando Numb_Encore_Linkin_Park_JAY-Z...
Fim.
```

> The `music/` folder is not version-controlled — audio files are large
> and copyrighted. Each user brings their own collection.

## Project structure

```
tocador/
├── .venv/              # virtual environment (not tracked)
├── .gitignore
├── README.md
├── requirements.txt
├── tocador.py          # entry point
└── music/            # .mp3 files (not tracked)
```

## Dependencies

| Package | Why |
| --- | --- |
| [playsound3](https://pypi.org/project/playsound3/) | Pure-Python audio playback, no native compilation required |

Chosen over `pygame` because it requires no compilation: on Python 3.14
`pygame` has no prebuilt wheel yet, and installing it fails for lack of
the SDL headers.

## Roadmap

- [x] **v1** — Simple shuffle
- [ ] **v2** — Shuffled playlist (plays every track in random order)
- [ ] **v3** — Interactive menu (play / next / stop)
- [ ] **v3.5** — Full playback controls (pause, resume, volume)
- [ ] **v4** — Refactor into functions
- [ ] **v5** — Persistent favourites and play history
- [ ] **v6** — Metadata (artist, album, duration)
- [ ] **v7** — `Player` class
- [ ] **v8** — Automated tests
- [ ] **v9** — Graphical interface

## Known limitations

- Playback is **blocking**: the track cannot be interrupted before it
  ends. To be addressed in v3.
- No handling for an empty music folder.

## Licence

MIT