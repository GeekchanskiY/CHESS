from .assets import Assets


def test_assets_list_available_aseets():
    "test checks that assets display correct available themes"
    asset = Assets()

    themes = asset.available_themes()

    real_themes = [
        "kosal",
        "magnetic",
        "maya",
        "tournament_metal",
        "marble",
        "graffiti",
        "symmetric",
        "riohacha",
        "kingdom",
        "wikipedia",
        "cardinal",
        "mediaeval",
        "maestro",
        "adventurer",
        "fresca",
        "tournament",
        "cases",
        "letter",
        "shapes",
        "symbol",
        "metro",
        "staunty",
        "dubrovny",
        "glass",
        "chesscom",
        "tatiana",
        "pixel",
        "merida",
        "chessnut",
        "dilena",
        "reilly",
        "leipzig",
        "lucena",
        "dash",
        "chess7",
        "chess24",
        "condal",
        "berlin",
        "pirouetti",
        "spatial",
        "cheq",
        "uscf",
        "alpha",
        "chess_samara",
        "graffiti_light",
        "fantasy",
        "companion",
    ]

    assert len(themes) == len(real_themes)

    assert themes == real_themes
