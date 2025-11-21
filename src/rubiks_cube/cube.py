from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List

FaceState = List[str]


COLORS = {
    "U": "W",  # White
    "D": "Y",  # Yellow
    "L": "O",  # Orange
    "R": "R",  # Red
    "F": "G",  # Green
    "B": "B",  # Blue
}


@dataclass
class Cube:
    """Representation of a 3x3 Rubik's Cube.

    The cube tracks six faces using a dictionary keyed by face name with a
    simple 3x3 flattened sticker list in reading order.
    """

    faces: Dict[str, FaceState] = field(default_factory=lambda: Cube._solved_state())

    def __post_init__(self) -> None:
        # Ensure each face has its own list instance
        self.faces = {face: stickers[:] for face, stickers in self.faces.items()}

    @staticmethod
    def _solved_state() -> Dict[str, FaceState]:
        return {face: [color] * 9 for face, color in COLORS.items()}

    def reset(self) -> None:
        """Return the cube to a solved state."""

        self.faces = Cube._solved_state()

    def copy(self) -> "Cube":
        return Cube({face: stickers[:] for face, stickers in self.faces.items()})

    def is_solved(self) -> bool:
        """Check whether every face is a single color."""

        return all(len(set(stickers)) == 1 for stickers in self.faces.values())

    def apply_move(self, move: str) -> None:
        """Apply a single move string (e.g., "R", "U'", "F2")."""

        from .moves import apply_move

        apply_move(self, move)

    def apply_moves(self, moves: Iterable[str] | str) -> None:
        """Apply a sequence of moves to the cube.

        Accepts either a whitespace-delimited string or an iterable of moves.
        """

        sequence = moves.split() if isinstance(moves, str) else list(moves)
        for move in sequence:
            if move.strip():
                self.apply_move(move.strip())

    def render_net(self) -> str:
        """Return a human-readable cube net for CLI display."""

        u = self.faces["U"]
        l = self.faces["L"]
        f = self.faces["F"]
        r = self.faces["R"]
        b = self.faces["B"]
        d = self.faces["D"]

        def fmt_row(row: List[str]) -> str:
            return " ".join(row)

        lines = []
        lines.append("      " + fmt_row(u[0:3]))
        lines.append("      " + fmt_row(u[3:6]))
        lines.append("      " + fmt_row(u[6:9]))
        for start in (0, 3, 6):
            lines.append(
                " ".join(
                    [
                        fmt_row(l[start:start + 3]),
                        fmt_row(f[start:start + 3]),
                        fmt_row(r[start:start + 3]),
                        fmt_row(b[start:start + 3]),
                    ]
                )
            )
        lines.append("      " + fmt_row(d[0:3]))
        lines.append("      " + fmt_row(d[3:6]))
        lines.append("      " + fmt_row(d[6:9]))
        return "\n".join(lines)

    def __str__(self) -> str:  # pragma: no cover - string helper
        return self.render_net()
