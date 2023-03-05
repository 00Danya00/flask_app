from flask import Flask
from flask import make_response
app = Flask(__name__)

@app.route('/api/v.1/ping', methods=['GET'])
def index():
    res = make_response("<h3>pong</h3>", 200)
    return res

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == 'main':
    app.run(debug=True)

