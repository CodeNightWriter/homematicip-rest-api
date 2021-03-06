import requests
import homematicip

import logging

logger = logging.getLogger(__name__)

class HomeMaticIPObject(object):
    """description of class"""
    headers = {}

    def __init__(self):
        self.headers = {'content-type': 'application/json', 'accept': 'application/json', 'VERSION': '8',
                        'AUTHTOKEN': homematicip.get_auth_token()}

    def _restCall(self, path, body = None):
        result = None
        result = requests.post('{}/hmip/{}'.format(homematicip.get_urlREST(), path), data=body, headers=self.headers)
        return result.json() if result.content != "" else ""


    def from_json(self, js):
        pass
