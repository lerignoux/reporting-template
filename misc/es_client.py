import logging
from opensearchpy import OpenSearch


log = logging.getLogger(__name__)

class EsClient(OpenSearch):

    @classmethod
    def get_geo_coords(cls, x, y):
        return {'lat': x/1000, 'lon': y/1000}
