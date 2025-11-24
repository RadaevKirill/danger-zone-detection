import cv2 

from interfaces.visualizer import Visualizer
from utlis.models import Image


class OpenCVVisualizer(Visualizer):
    def visualize(self, image: Image) -> None:
        cv2.imshow('Detecting', image)
        cv2.waitKey(1)
