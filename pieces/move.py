from dataclasses import dataclass

@dataclass
class Move:
    """Move is a dataclass which contains meta info about move"""

    prev_pos: int
    new_pos: int
    turn: int
