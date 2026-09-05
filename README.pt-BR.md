> 🇬🇧 [Read in English](README.md)

# 🎵 Tocador

Tocador de música aleatória em linha de comando. Sorteia um arquivo `.mp3`
de uma pasta local e o reproduz.

Projeto de aprendizado em Python, desenvolvido de forma incremental:
cada versão introduz um conceito novo da linguagem.

## Estado atual

**v1 — Sorteio simples.** Lê os arquivos `.mp3` da pasta `musicas/`,
sorteia um e toca até o fim.

## Requisitos

- Python 3.11+
- macOS, Linux ou Windows (a reprodução usa o player nativo do sistema)

## Instalação

```bash
git clone git@github.com:rafamsouza1702/tocador.git
cd tocador

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

## Uso

Crie a pasta de músicas e coloque seus arquivos `.mp3` nela:

```bash
mkdir musicas
```

Execute:

```bash
python tocador.py
```

Saída esperada:

```
Tocando Numb_Encore_Linkin_Park_JAY-Z...
Fim.
```

> A pasta `musicas/` não é versionada — arquivos de áudio são grandes e
> têm direitos autorais. Cada usuário usa a própria coleção.

## Estrutura

```
tocador/
├── .venv/              # ambiente virtual (não versionado)
├── .gitignore
├── README.md
├── requirements.txt
├── tocador.py          # ponto de entrada
└── musicas/            # arquivos .mp3 (não versionado)
```

## Dependências

| Pacote | Por quê |
| --- | --- |
| [playsound3](https://pypi.org/project/playsound3/) | Reprodução de áudio em Python puro, sem compilação nativa |

Escolhida em lugar do `pygame` por não exigir compilação: no Python 3.14
o `pygame` ainda não tem *wheel* pré-compilada e a instalação falha por
falta dos headers do SDL.

## Roadmap

- [x] **v1** — Sorteio simples
- [ ] **v2** — Playlist embaralhada (toca todas em ordem aleatória)
- [ ] **v3** — Menu interativo (tocar / próxima / parar)
- [ ] **v3.5** — Controles completos (pausar, retomar, volume)
- [ ] **v4** — Refatoração em funções
- [ ] **v5** — Favoritos e histórico persistidos
- [ ] **v6** — Metadados (artista, álbum, duração)
- [ ] **v7** — Classe `Player`
- [ ] **v8** — Testes automatizados
- [ ] **v9** — Interface gráfica

## Limitações conhecidas

- A reprodução é **bloqueante**: não é possível interromper a música
  antes do fim. Será resolvido na v3.
- Não há tratamento para pasta vazia.

## Licença

MIT