# Rubik's Cube CLI

A lightweight Python project with modules for representing a Rubik's Cube, applying moves, generating scrambles, and offering quick solving hints. Launch the CLI to play from your terminal.

## Project structure

- `src/rubiks_cube/cube.py` – Cube representation, rendering, and helpers.
- `src/rubiks_cube/moves.py` – Face rotations and move parsing logic.
- `src/rubiks_cube/scramble.py` – Random scramble generator.
- `src/rubiks_cube/solver.py` – Simple solving helpers (inverse of scramble).
- `src/rubiks_cube/game.py` – Interactive CLI loop.
- `main.py` – Entry point for starting the game.

## Getting started

1. Ensure you have Python 3.11+ available.
2. Run the game from the repository root:

   ```bash
   python -m main
   ```

   Or launch via the package path:

   ```bash
   python -m rubiks_cube.game
   ```

## CLI commands

- `scramble [len]` – Apply a random scramble (default 20 moves).
- `move <sequence>` – Apply space-separated moves (supports `U/D/L/R/F/B`, `2`, and `'`).
- `show` – Print the cube net.
- `reset` – Return to a solved cube.
- `solve` – Show the inverse of the last scramble as a quick hint.
- `help` – Display available commands.
- `quit` – Exit the game.
