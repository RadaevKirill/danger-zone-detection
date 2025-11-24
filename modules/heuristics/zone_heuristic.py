import json
from typing import List

from shapely import Point, Polygon

from utlis.models import Detections
from interfaces.heuristics import Heuristic


class ZoneHeuristic(Heuristic):
    def __init__(self, zone_configs_path: str):
        self._zone_configs_path = zone_configs_path

        with open(self._zone_configs_path, 'r') as file:
            self._zones = json.load(file)
            self._polygon = Polygon([[p['x'], p['y']] for p in self._zones])

    def analyze(self, detections: Detections) -> Detections:
        in_zone = []
        
        for det in detections:
            if self._polygon.contains(Point(det.absolute_box.center.as_tuple)):
                in_zone.append(det)

        return in_zone

    def get_zone(self) -> List[List[int]]:
        return [[p['x'], p['y']] for p in self._zones]