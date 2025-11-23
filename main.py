from interfaces.decoder import Decoder
from interfaces.detector import Detector
from interfaces.heuristics import Heuristic
from interfaces.painter import Painter
from interfaces.tracker import Tracker
from interfaces.visualizer import Visualizer


class Controller:
    def __init__(
            self,
            decoder: Decoder,
            detector: Detector,
            heuristic: Heuristic,
            painter: Painter,
            tracker: Tracker,
            visualizer: Visualizer
    ):
        self._decoder = decoder
        self._detector = detector
        self._heuristic = heuristic
        self._painter = painter
        self._tracker = tracker
        self._visualizer = visualizer

    def run(self):
        for image in self._decoder.decode():
            detections = self._detector.detect(image)
            tracks = self._tracker.track(detections)
            inzone = self._heuristic.analyze(detections)
            image = self._painter.paint(image, tracks, inzone)
