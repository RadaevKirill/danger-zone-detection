from dataclasses import dataclass
from typing import Dict, Generic, List, Optional, Tuple, TypeVar, Union

from nptyping import NDArray, Shape, UInt8


ImageRGB = NDArray[Shape['* height, * width, 3 rgb'], UInt8]
ImageBGR = NDArray[Shape['* height, * width, 3 bgr'], UInt8]
Image = Union[ImageRGB, ImageBGR]

Coordinate = TypeVar('Coordinate', int, float)


@dataclass
class Point(Generic[Coordinate]):
    x: Coordinate
    y: Coordinate

    @property
    def as_tuple(self) -> Tuple[Coordinate, Coordinate]:
        return self.x, self.y

@dataclass
class Box(Generic[Coordinate]):
    left_top: Point[Coordinate]
    right_bottom: Point[Coordinate]

    @property
    def as_ltrb(self) -> Tuple[Coordinate, Coordinate, Coordinate, Coordinate]:
        return self.left_top.x, self.left_top.y, self.right_bottom.x, self.right_bottom.y

    @property
    def as_ltwh(self) -> Tuple[Coordinate, Coordinate, Coordinate, Coordinate]:
        return *self.left_top.as_tuple, self.width, self.height

    @property
    def center(self) -> Point[Coordinate]:
        return Point(
            type(self.left_top.x)((self.left_top.x + self.right_bottom.x) / 2),
            type(self.left_top.x)((self.left_top.y + self.right_bottom.y) / 2),
        )

    @property
    def height(self) -> Coordinate:
        return max(type(self.left_top.y)(0), self.right_bottom.y - self.left_top.y)

    @property
    def width(self) -> Coordinate:
        return max(type(self.left_top.x)(0), self.right_bottom.x - self.left_top.x)


@dataclass
class Detection:
    absolute_box: Box[int]
    relative_box: Box[float]
    score: float
    label_as_int: int
    label_as_str: str
    crop: Optional[Image] = None

TrackId = int
Points = List[Point[Coordinate]]
Boxes = List[Box]
Detections = List[Detection]
Track = List[Detection]
Tracks = Dict[TrackId, Track]