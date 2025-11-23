from abc import ABC

from utlis.models import Image

class Visualizer(ABC):

    def visualize(self, image: Image) -> None:
        raise NotImplementedError