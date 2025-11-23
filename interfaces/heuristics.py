from abc import ABC

from utlis.models import Detections

class Heuristic(ABC):

    def analyze(self, decetctions: Detections) -> Detections:
        raise NotImplementedError