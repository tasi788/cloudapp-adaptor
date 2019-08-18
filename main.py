import os
import logging
import coloredlogs
from configparser import ConfigParser
from flask import Flask, escape, request, jsonify
import redis as redis_

from cloudapp import cloudapp
logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO')
config = ConfigParser()
config.read('config.cfg')
app = Flask(__name__)
redis = redis_.from_url(config.get('database', 'redis'))
cloud = cloudapp(config.get('cloudapp', 'acc'),
                 config.get('cloudapp', 'passwd'))


def get_auth(auth_key):
    result = list(redis.scan_iter('*'))
    collect = []
    collect_auth = []
    for data in result:
        collect.append(data.decode())
        # data.decode()
    for d in collect:
        collect_auth.append(redis.get(d).decode())

    logger.info(collect_auth)

    if auth_key in collect_auth:
        return True
    else:
        return False


@app.route('/', methods=['POST', 'GET'])
def handle():
    full = False
    if request.method == 'POST':
        if 'tdc' in request.form.keys():
            if request.form['tdc'] == config.get('tdc', 'auth'):
                try:
                    name = request.form['name']
                    auth = request.form['auth']
                    redis.set(name, auth)
                    return jsonify(status=True, result='added.')
                except Exception as e:
                    raise
                    return jsonify(status=False, reason='ERROR')
            else:
                return jsonify(status=False, reason='who are you :(')
        if dict(request.files) == {}:
            return jsonify(status=False, reason='no file upload.')
        if dict(request.form) == {}:
            return jsonify(status=False, reason='no auth.')
        if 'auth' not in request.form.keys():
            return jsonify(status=False, reason='no auth.')
        #auth = redis.get(request.form['auth'])

        if get_auth == False:
            return jsonify(status=False, reason='auth failed.')
        if 'output' in request.form.keys():
            if request.form['output'].lower() == 'full':
                full = True

        file = request.files['file']
        result = cloud.upload_file(file)
        if result == False:
            return jsonify(status=False, result='unknown')
        if full:
            return jsonify(status=True, result=result)
        else:
            url = result['content_url'].replace('http', 'https')
            return jsonify(status=True, result=url)
    else:
        return jsonify(status=False, reason='bro you are not cool :(')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, threaded=True, debug=True)
