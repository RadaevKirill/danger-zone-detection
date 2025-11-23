import cv2 

from interfaces.tracker import Tracker
from utlis.models import Detections, Tracks, Track


class OpenCVVisualizer(Tracker):

    def track(self, detections: Detections) -> Tracks:
        raise NotImplementedError
