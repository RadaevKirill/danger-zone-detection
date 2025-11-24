import json

import cv2


class ZoneConfigurator:
    def __init__(self, video_path: str):
        self._video_path = video_path
        self._frame = None
        self._points = []

    def configure(self):
        cap = cv2.VideoCapture(self._video_path)

        ret, self._frame = cap.read()

        if not ret:
            raise RuntimeError("Video not found.")

        while True:
            cv2.imshow('Drawing', self._frame)
            cv2.setMouseCallback('Drawing', self.mouse_callback)
            key = cv2.waitKey(0)
            if key == ord('q'):
                break
            self.update_image()

        with open('assets/restricted_zones.json', 'w') as f:
            f.write(json.dumps([{'x': p[0], 'y': p[1]}for p in self._points]))

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self._points.append([x, y])

    def update_image(self):
        if len(self._points) > 1:
            for pt1, pt2 in zip(self._points[:-1], self._points[1:]):
                self._frame = cv2.line(self._frame, pt1, pt2, (0, 255, 0), 2)
            self._frame = cv2.line(self._frame, self._points[-1], self._points[0], (0, 255, 0), 2)

if __name__ == "__main__":
    ZoneConfigurator('./assets/test.mp4').configure()