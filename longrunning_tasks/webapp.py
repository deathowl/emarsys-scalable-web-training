from flask import Flask, render_template, request
from werkzeug import secure_filename
import time
import os
from redis import StrictRedis
from rq import Queue

q = Queue(connection=StrictRedis(host=os.getenv("REDIS_HOST"), port=6379))
application = Flask(__name__, static_folder="uploads")


@application.route('/longrunning/<int:amount>', methods=['GET'])
def longrunning(amount=2):
        time.sleep(amount)
        return 'slept %s seconds' % amount

@application.route('/longrunningasync/<int:amount>', methods=['GET'])
def asyncexecution(amount=2):
        q.enqueue(time.sleep, amount)
        return 'slept %s seconds' % amount




if __name__ == '__main__':
    application.run(debug=True)
