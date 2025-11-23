from abc import ABC

from utlis.models import Image, Detections

class Detector(ABC):

    def detect(self, image: Image) -> Detections:
        raise NotImplementedError