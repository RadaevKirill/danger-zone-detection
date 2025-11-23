from ultralytics import YOLO

from utlis.models import Image, Detection, Detections, Box, Point
from interfaces.detector import Detector


class YoloDetector(Detector):
    def __init__(self, model_path, threshold):
        self._model = YOLO(model_path, task='detect')
        self._threshold = threshold

    def detect(self, image: Image) -> Detections:
        detections = []
        results = self._model.predict(image, classes=[0], verbose=False, conf=self._threshold)
        
        for result in results:
            boxes = result.boxes
            if boxes is not None:
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0].tolist()
                    rx1, ry1, rx2, ry2 = x1 / image.shape[1], y1 / image.shape[0], x2 / image.shape[1], y2 / image.shape[0]
                    
                    detections.append(
                        Detection(
                            absolute_box=Box(left_top=Point(x=x1, y=y1), right_bottom=Point(x=x2, y=y2)),
                            relative_box=Box(left_top=Point(x=rx1, y=ry1), right_bottom=Point(x=rx2, y=ry2)),
                            score=box.conf[0].item(),
                            label_as_int=0,
                            label_as_str='person',
                        )
                    )
                    
        return detections
