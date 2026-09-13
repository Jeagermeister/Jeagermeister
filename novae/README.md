# NOVAE (MVP)

**NOVAE** stands for **Natural Operations Voice Assistant Engine**.

This repository is the **first-phase Python MVP** for a voice-controlled assistant interface. The goal is to validate the flow and boundaries before evolving toward a more structured **C++ implementation**.

## Long-term direction

- Primary integration target: **Hermit** (Jeagermeister's C++ AI supervisor)
- Short-term objective: prove command capture, parsing, and routing flow
- Future objective: migrate validated design patterns into a production C++ codebase

## MVP scope in this repo

- microphone/audio input capture scaffolding
- speech-to-text (STT) module scaffolding
- simple command parsing and command routing scaffolding
- Hermit adapter interface stub
- basic logging/console output flow
- minimal tests as placeholders for iterative development

## Project structure

```text
novae/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── main.py
│   ├── audio/
│   ├── stt/
│   ├── commands/
│   └── hermit_adapter/
└── tests/
```

## Quick start

1. Create a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the MVP pipeline:
   ```bash
   python -m src.main
   ```
4. Run tests:
   ```bash
   pytest -q
   ```

## Next steps

- Replace audio stub with actual microphone streaming/capture implementation
- Replace STT stub with a concrete local or API-backed model integration
- Expand command grammar and routing
- Connect Hermit adapter to real transport/protocol
- Add stronger test coverage around parsing and adapter contract behavior
