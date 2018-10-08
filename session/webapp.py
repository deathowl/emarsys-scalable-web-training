from flask import Flask, session
from flask_session import Session
import os

app = Flask(__name__)
# Check Configuration section for more details
app.config['SECRET_KEY'] = 'developeracademy'
app.config['SESSION_TYPE'] = 'filesystem'
sess = Session()
sess.init_app(app)

@app.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'

@app.route('/get/')
def get():
    return session.get('key', 'not set')


if __name__ == '__main__':
    app.run('0.0.0.0', 8000, debug=False)

