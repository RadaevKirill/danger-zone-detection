from abc import ABC
from typing import Optional

from utlis.models import Image, Tracks, Detections

class Painter(ABC):

    def paint(self, image: Image, detections: Detections, danger_detections: Detections, timestamp: float) -> Image:
        raise NotImplementedError