from abc import ABC
from pathlib import Path
from typing import Optional

from utlis.models import Image, Detections

class Detector(ABC):

    def detect(self, image: Image) -> Detections:
        raise NotImplementedError