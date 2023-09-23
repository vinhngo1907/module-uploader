from dataclasses import dataclass
@dataclass
class PlateInfo:
    label: str
    score: float

    def asDict(self):
        return vars(self)