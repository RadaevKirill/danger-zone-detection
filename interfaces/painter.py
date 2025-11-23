from abc import ABC

from utlis.models import Image, Tracks, Detections

class Painter(ABC):

    def paint(self, image: Image, tracks: Tracks, detections: Detections) -> Image:
        raise NotImplementedError