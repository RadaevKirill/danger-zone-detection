from abc import ABC

from utlis.models import Detections, Tracks

class Tracker(ABC):

    def track(self, detections: Detections) -> Tracks:
        raise NotImplementedError