import logging


class Mode:
    """
    Mode class is used to separate env's for different purposes
    """

    names = {"production": 1, "stage": 2, "experimental": 3}

    def __init__(self, name: str):
        self.logger = logging.getLogger(__name__)

        try:
            self.level = self.names[name]
        except NameError:
            self.logger.error(f"failed to get mode level from '{name}'")
            self.level = 1

    def can_experimental(self) -> bool:
        return self.level >= 3

    def can_stage(self) -> bool:
        return self.level >= 2

    def can_prod(self) -> bool:
        return self.level >= 1
