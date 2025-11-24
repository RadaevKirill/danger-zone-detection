import json

import cv2

from utlis.models import Detections, Image
from interfaces.painter import Painter


class OpenCVPainter(Painter):
    def __init__(self, zone_configs_path: str, time_to_hide: int):
        self._zone_configs_path = zone_configs_path
        self._time_to_hide = time_to_hide
        self._last_alarm = -self._time_to_hide

        with open(self._zone_configs_path, 'r') as file:
            self._zones = [[p['x'], p['y']] for p in json.load(file)]

    def paint(self, image: Image, detections: Detections, danger_detections: Detections, timestamp: float) -> Image:
        for det in detections:
            x1, y1, x2, y2 = det.absolute_box.as_ltrb
            image = cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)

        for pt1, pt2 in zip(self._zones[:-1], self._zones[1:]):
            image = cv2.line(image, pt1, pt2, (0, 255, 0), 2)
        image = cv2.line(image, self._zones[-1], self._zones[0], (0, 255, 0), 2)

        if danger_detections:
            self._last_alarm = timestamp

        if timestamp - self._last_alarm <= 3:
            cv2.putText(image, 'alarm!', (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

        return image