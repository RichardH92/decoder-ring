#!/usr/bin/python3

from slack_ip_resolver import SlackIpResolver
from flask import Flask

app = Flask(__name__)
slackIpResolver = SlackIpResolver()

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():

    print(slackIpResolver.resolveIp())

    return 'Test123'

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=105)