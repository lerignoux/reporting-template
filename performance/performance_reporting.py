import logging
import time

log = logging.getLogger(__name__)


class PerformanceReporting(object):

    def __init__(self, config):
        self.config = config
        self.last_frame = time.time()
        self.frame_max_time = 1 / self.config.get('FPS', 60)

    def log_frame(self):
        new_frame = time.time()
        if new_frame - self.last_frame > self.frame_max_time:
            log.warning(f"Slow frame detected: {new_frame - self.last_frame} seconds")
        self.last_frame = new_frame