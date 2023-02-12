import os
from pathlib import PurePath

from utils.contants import RESOURCER_PATH


def find_resourcer_path():
    current_dir = os.path.dirname(__file__)
    path = PurePath(current_dir).parent
    return os.path.join(path, RESOURCER_PATH)
