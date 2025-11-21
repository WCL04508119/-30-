from __future__ import annotations

import shlex
from typing import List

from .cube import Cube
from .scramble import generate_scramble
from .solver import quick_solve_hint


def _print_help() -> None:
    print(
        "Commands:\n"
        "  scramble [len]  - Scramble the cube with optional length (default 20).\n"
        "  move <seq>      - Apply space-separated moves (e.g., R U R' U').\n"
        "  show            - Render the cube net.\n"
        "  reset           - Return to a solved cube.\n"
        "  solve           - Show inverse of last scramble as a quick hint.\n"
        "  help            - Show this message.\n"
        "  quit            - Exit the game."
    )


def run_cli() -> None:
    """Start a lightweight interactive CLI loop."""

    cube = Cube()
    scramble_history: List[str] = []
    print("Welcome to the Rubik's Cube CLI! Type 'help' for commands.")
    while True:
        try:
            raw = input("cube> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if not raw:
            continue

        parts = shlex.split(raw)
        command = parts[0].lower()

        if command == "help":
            _print_help()
        elif command == "quit":
            break
        elif command == "show":
            print(cube.render_net())
        elif command == "reset":
            cube.reset()
            scramble_history = []
            print("Cube reset to solved state.")
        elif command == "scramble":
            length = int(parts[1]) if len(parts) > 1 else 20
            scramble_history = generate_scramble(length)
            cube.apply_moves(scramble_history)
            print(f"Scramble: {' '.join(scramble_history)}")
            print(cube.render_net())
        elif command == "move":
            if len(parts) == 1:
                print("Please provide moves. Example: move R U R' U'")
                continue
            sequence = parts[1:]
            try:
                cube.apply_moves(sequence)
            except ValueError as exc:  # pragma: no cover - CLI guard
                print(exc)
                continue
            print(cube.render_net())
            if cube.is_solved():
                print("🎉 Cube solved!")
        elif command == "solve":
            if not scramble_history:
                print("No scramble history available. Scramble first for a hint.")
                continue
            solution = quick_solve_hint(scramble_history)
            print("Try undoing the scramble:", " ".join(solution))
        else:
            print("Unknown command. Type 'help' for a list of options.")


if __name__ == "__main__":  # pragma: no cover - CLI entry
    run_cli()
