from __future__ import annotations

from typing import Iterable, List, Tuple

from .cube import Cube

MoveGroup = Tuple[str, List[int]]


def rotate_face(face: List[str], turns: int = 1) -> None:
    """Rotate a face clockwise for the given number of quarter turns."""

    turns = turns % 4
    for _ in range(turns):
        face[:] = [
            face[6],
            face[3],
            face[0],
            face[7],
            face[4],
            face[1],
            face[8],
            face[5],
            face[2],
        ]


def _cycle_groups(cube: Cube, groups: Iterable[MoveGroup]) -> None:
    values = [[cube.faces[face][i] for i in indices] for face, indices in groups]
    for (face, indices), incoming in zip(groups, values[-1:] + values[:-1]):
        for idx, value in zip(indices, incoming):
            cube.faces[face][idx] = value


def _u_turn(cube: Cube) -> None:
    rotate_face(cube.faces["U"], 1)
    _cycle_groups(
        cube,
        [
            ("F", [0, 1, 2]),
            ("R", [0, 1, 2]),
            ("B", [0, 1, 2]),
            ("L", [0, 1, 2]),
        ],
    )


def _d_turn(cube: Cube) -> None:
    rotate_face(cube.faces["D"], 1)
    _cycle_groups(
        cube,
        [
            ("F", [6, 7, 8]),
            ("L", [6, 7, 8]),
            ("B", [6, 7, 8]),
            ("R", [6, 7, 8]),
        ],
    )


def _l_turn(cube: Cube) -> None:
    rotate_face(cube.faces["L"], 1)
    _cycle_groups(
        cube,
        [
            ("U", [0, 3, 6]),
            ("F", [0, 3, 6]),
            ("D", [0, 3, 6]),
            ("B", [8, 5, 2]),
        ],
    )


def _r_turn(cube: Cube) -> None:
    rotate_face(cube.faces["R"], 1)
    _cycle_groups(
        cube,
        [
            ("U", [2, 5, 8]),
            ("B", [6, 3, 0]),
            ("D", [2, 5, 8]),
            ("F", [2, 5, 8]),
        ],
    )


def _f_turn(cube: Cube) -> None:
    rotate_face(cube.faces["F"], 1)
    _cycle_groups(
        cube,
        [
            ("U", [6, 7, 8]),
            ("R", [0, 3, 6]),
            ("D", [2, 1, 0]),
            ("L", [8, 5, 2]),
        ],
    )


def _b_turn(cube: Cube) -> None:
    rotate_face(cube.faces["B"], 1)
    _cycle_groups(
        cube,
        [
            ("U", [0, 1, 2]),
            ("L", [0, 3, 6]),
            ("D", [8, 7, 6]),
            ("R", [2, 5, 8]),
        ],
    )


MOVE_HANDLERS = {
    "U": _u_turn,
    "D": _d_turn,
    "L": _l_turn,
    "R": _r_turn,
    "F": _f_turn,
    "B": _b_turn,
}

VALID_MOVES = [
    face + suffix for face in MOVE_HANDLERS for suffix in ("", "'", "2")
]


def apply_move(cube: Cube, move: str) -> None:
    """Parse and apply a single move to the cube."""

    move = move.strip()
    if not move:
        return

    face = move[0].upper()
    modifier = move[1:] if len(move) > 1 else ""
    if face not in MOVE_HANDLERS or modifier not in ("", "'", "2"):
        raise ValueError(f"Unsupported move: {move}")

    turns = {"": 1, "'": 3, "2": 2}[modifier]
    for _ in range(turns):
        MOVE_HANDLERS[face](cube)
