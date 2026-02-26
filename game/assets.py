import os
from pieces.piece import Piece


class ThemeDoesNotExists(Exception):
    pass


class Asset:
    def __init__(self, name: str, piece_assets_folder=os.path.abspath("assets")):
        self.name = name
        self.piece_assets_folder = piece_assets_folder

    def get_piece_image(self, piece: Piece):
        c = piece.get_color()
        name = piece.get_name()

        return self.piece_assets_folder + "/{}.png".format(c + name)


class Assets:
    def __init__(self, piece_assets_folder=os.path.abspath("assets")):
        self.piece_assets_folder = piece_assets_folder

    def available_themes(self) -> list[str]:
        available_themes = []

        asset_folder_contents = os.listdir(self.piece_assets_folder)

        for entry in asset_folder_contents:
            if not os.path.isfile(os.path.join(self.piece_assets_folder, entry)):
                available_themes.append(entry)

        return available_themes

    def load(self, name: str) -> Asset:
        if name not in self.available_themes():
            raise ThemeDoesNotExists(f"theme {name} does not exists")

        return Asset()
