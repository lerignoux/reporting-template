import uuid
import time
import json
import logging
from random import randint, uniform
from opensearchpy import helpers

log = logging.getLogger(__name__)


class WorldManager(object):

    def __init__(self, config, performance_reporting, es_logger):
        log.debug("Initializing world")
        self.config = config
        self.performance_reporting = performance_reporting
        self.es_logger = es_logger
        self.setup_world()
        self.load_animals()

    @property
    def height(self):
        return self.config.get('height', 254)

    @property
    def width(self):
        return self.config.get('width', 254)

    def setup_world(self):
        self.world  = [[[] for i in range(self.width)] for j in range(self.height)]

    def load_animals(self):
        log.debug("Loading map animals")
        to_log = []
        for animal, count in self.config.get('population', {}).items():
            for i in range(count):
                x = randint(0, self.height-1)
                y = randint(0, self.width-1)
                try:
                    self.world[y][x].append(animal)
                except Exception as e:
                    log.info(x)
                    log.info(y)
                log.debug(f"found {animal} in {x},{y}")
                to_log.append({
                    'animal': animal,
                    'position': self.es_logger.get_geo_coords(x, y)
                })
        self.log_animals_spawns(to_log)

    def log_animals_spawns(self, spawns):
        log.debug("Bulk inserting spawns")
        extended = ({
            'animal': spawn['animal'],
            'position': spawn['position'],
            '_index': 'population',
            '_id': uuid.uuid4()
            } for spawn in spawns)
        helpers.bulk(self.es_logger, extended)

    def run(self):
        for column in self.world:
            for cell in column:
                for animal in cell:
                    log.debug(f"Running Animal {animal} frame")
                    # Processing time in ms
                    animal_processing_time = uniform(0.00, 0.16)
                    time.sleep(animal_processing_time/1000)
        self.performance_reporting.log_frame()