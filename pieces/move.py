class Move:
    """Move is a dataclass which contains meta info about move"""

    def __init__(self, prev_pos: int, new_pos: int, turn: int):
        self.prev_pos = prev_pos
        self.new_pos = new_pos
        self.turn = turn
