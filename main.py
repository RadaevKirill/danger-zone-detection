from interfaces.decoder import Decoder
from interfaces.detector import Detector
from interfaces.heuristics import Heuristic
from interfaces.painter import Painter
from interfaces.tracker import Tracker
from interfaces.visualizer import Visualizer

import hydra
from omegaconf import DictConfig, OmegaConf


class Controller:
    def __init__(
            self,
            decoder: Decoder,
            detector: Detector,
            heuristic: Heuristic,
            painter: Painter,
            visualizer: Visualizer
    ):
        self._decoder = decoder
        self._detector = detector
        self._heuristic = heuristic
        self._painter = painter
        self._visualizer = visualizer

    def run(self):
        for image, num_frame, timestamp in self._decoder.decode():
            detections = self._detector.detect(image)
            in_zone = self._heuristic.analyze(detections)
            image = self._painter.paint(image, detections, in_zone, timestamp)
            self._visualizer.visualize(image)


@hydra.main(config_path='assets', config_name='config', version_base='1.3.2')
def main(cfg : DictConfig) -> None:
    analytics = hydra.utils.instantiate(cfg.analytics)
    analytics.run()


if __name__ == '__main__':
    main()