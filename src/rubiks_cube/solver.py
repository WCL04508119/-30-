from __future__ import annotations

from typing import Iterable, List

from .moves import apply_move


def invert_move(move: str) -> str:
    """Return the inverse of a single move string."""

    move = move.strip()
    if not move:
        return ""
    face = move[0]
    modifier = move[1:] if len(move) > 1 else ""
    if modifier == "'":
        return face
    if modifier == "2":
        return move
    return face + "'"


def invert_sequence(moves: Iterable[str]) -> List[str]:
    """Return a reversed sequence that undoes the provided moves."""

    sequence = [m for m in moves if m.strip()]
    return [invert_move(move) for move in reversed(sequence)]


def apply_solution(cube, moves: Iterable[str]) -> None:
    """Apply a list of solution moves to a cube."""

    for move in moves:
        apply_move(cube, move)


def quick_solve_hint(scramble_history: List[str]) -> List[str]:
    """Provide a quick solution suggestion using inverse scramble history.

    This is not a full solver but serves as a teaching aid for newcomers.
    """

    return invert_sequence(scramble_history)
