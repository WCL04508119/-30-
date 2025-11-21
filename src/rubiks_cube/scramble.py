from __future__ import annotations

import random
from typing import List

from .moves import VALID_MOVES


def generate_scramble(length: int = 20, seed: int | None = None) -> List[str]:
    """Create a random scramble avoiding immediate face repeats."""

    if seed is not None:
        random.seed(seed)

    scramble: List[str] = []
    last_face = None
    while len(scramble) < length:
        move = random.choice(VALID_MOVES)
        if last_face and move[0] == last_face:
            continue
        scramble.append(move)
        last_face = move[0]
    return scramble
