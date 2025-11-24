from typing import Iterator, Tuple

import cv2

from interfaces.decoder import Decoder
from utlis.models import ImageBGR



class OpenCVDecoder(Decoder):
    def __init__(self, video_path: str, video_fps: int):
        self._video_path = video_path
        self._video_fps = video_fps
        self._cap = cv2.VideoCapture(self._video_path)
        self._num_frame = 0

    def decode(self) -> Iterator[Tuple[ImageBGR, int, float]]:
        while True:
            ret, frame =  self._cap.read()
            self._num_frame += 1

            if not ret:
                break
            yield frame, self._num_frame, self._num_frame / self._video_fps

        self._cap.release()



