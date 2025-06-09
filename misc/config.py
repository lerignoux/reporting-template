import json
import logging

log = logging.getLogger(__name__)

def load_config():
    with open("config.json", 'r') as f:
        return json.load(f)