import logging
from elasticsearch import Elasticsearch

from misc import load_config, EsClient
from performance.performance_reporting import PerformanceReporting
from world.world_manager import WorldManager

logging.basicConfig(
    format='%(levelname)s:%(message)s',
    level=logging.INFO,
    handlers=[logging.StreamHandler()]
)
log = logging.getLogger(__name__)


if __name__ == '__main__':
    config = load_config()
    log.debug("Starting project.")

    es_client = EsClient(
        config.get('elasticsearch').get('host'),
        http_auth=config.get('elasticsearch').get('auth')
    )
    performance_reporting = PerformanceReporting(config.get('performance'))
    world = WorldManager(config.get('world'), performance_reporting, es_client)
    try:
        while True:
            world.run()
    except Exception as e:
        log.exception(f"Stopping: {e}")