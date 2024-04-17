import os


class Individual:
    def __init__(self) -> None:
        pass


class MatchSystem():
    individuals: list[Individual]

    def __init__(cls, individuals: list[Individual], path: str | os.PathLike):
        if individuals is not None:
            cls.individuals = individuals
        else:
            cls._load_individuals(path)

    @staticmethod
    def _load_individuals(cls, path):
        pass


if __name__ == "__main__":
    matchSystem = MatchSystem()
    # matchSystem.match(target, matchStratety)
