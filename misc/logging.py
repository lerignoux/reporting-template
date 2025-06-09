import logging
import os
import socket
import uuid
from opensearchpy import OpenSearch, helpers
from .config import load_config

log = logging.getLogger("__main__")

config = load_config()
es_client = OpenSearch(
    config.get('elasticsearch').get('host'),
    http_auth=config.get('elasticsearch').get('auth')
)

login = 'unknown'
try:
    login = os.getlogin()
except Exception:
    pass

log.debug(f"starting monitoring of {socket.gethostname()} from {login}")

helpers.bulk(es_client, [{
    'host': socket.gethostname(),
    'login': login,
    '_index': 'metadata',
    '_id': uuid.uuid4()
}])