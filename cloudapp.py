import logging
import coloredlogs
import os.path
import requests
import json
from requests.auth import HTTPDigestAuth

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')


class cloudapp(object):
    req = requests.Session()

    def __init__(self, username, password):
        self.req.auth = requests.auth.HTTPDigestAuth(username, password)
        self.req.headers.update({'Accept': 'application/json'})

    def get_upload_param(self, fileName):
        payload = {'name': fileName}
        r = self.req.post('https://my.cl.ly/v3/items',
                          data=json.dumps(payload))
        if r.status_code not in [200, 201]:
            return False
        else:
            res = json.loads(r.text)
            return res

    def upload_file(self, file):
        res = self.get_upload_param(file.filename)
        if res == False:
            return False
        res['s3']['key'] = res['s3']['key'].replace(
            '${filename}', file.filename)
        data = res['s3']
        files = {'file': file.read()}
        r = requests.post(res['url'], data=data,
                          files=files, allow_redirects=False)
        confirmUrl = r.headers['Location']
        r = self.req.get(confirmUrl)
        if r.status_code == 200:
            return r.json()
        else:
            return r.text
