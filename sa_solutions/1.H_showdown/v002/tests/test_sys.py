from pprint import pprint
from pathlib import Path

from showdown import game


def test_path():
    print("")
    import sys
    pprint(sys.path)


def test_filepath():
    print("")
    pprint(Path(__file__).parent)
