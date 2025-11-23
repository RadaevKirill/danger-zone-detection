from abc import ABC
from typing import Iterator, Tuple

from utlis.models import ImageBGR

class Decoder(ABC):

    def decode(self) -> Iterator[Tuple[ImageBGR, int, float]]:
        raise NotImplementedError