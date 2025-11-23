from deep_sort_realtime.deepsort_tracker import DeepSort

from interfaces.tracker import Tracker
from utlis.models import Detections, Tracks, Track, Image



class DeepSortTracker(Tracker):
    def __init__(self, max_age: int):
        self._tracker = DeepSort(max_age=max_age)

    def track(self, detections: Detections, image: Image) -> Tracks:
        bbs = self._tracker.update_tracks(frame=image, )