from cProfile import label
from dataclasses import dataclass, field
from os import PathLike
from datetime import datetime
import string
from typing import List, Dict
from venv import create
# from numpy import integer, ndarray
from base64 import b64encode
# from cv2 import imencode
from enum import Enum

@dataclass
class PlateInfo:
    label: str
    score: float

    def asDict(self):
        return vars(self)