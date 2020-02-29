from __future__ import unicode_literals

import login
import json

from flask import Flask, request
app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)

sessionStorage = {}


@app.route('/post', methods=['POST'])
def main():
    logging.info('Request: %r', request.json)

    response = {
            'session': request.json['session'],
            'version': request.json['version'],
            'response': {
                    'end_session': False
                }
        }

    handle_dialog(response, request.json)
    return json.dumps(response,
                      ensure_ascii=False,
                      indent=2
            )


def handle_dialog(res, req):
    if req['response']['original_utterance']:
        res['response']['text'] = req['response']['original_utterance']
    else:
        res['response']['text'] = "EHO-bot, repeate)"


if __name__ == '__main__':
    main()
