from functools import lru_cache
import csv


@lru_cache
def read(path: str):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, "r", encoding="utf8") as file:
        return list(csv.DictReader(file, delimiter=",", quotechar='"'))
