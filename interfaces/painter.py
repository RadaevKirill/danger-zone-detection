from abc import ABC

from utlis.models import Image, Detections

class Painter(ABC):

    def paint(self, image: Image, detections: Detections, danger_detections: Detections, timestamp: float) -> Image:
        raise NotImplementedError