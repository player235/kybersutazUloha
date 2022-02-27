"""Flask App Project."""

from flask import Flask, jsonify
app = Flask(__name__)

FLAG = os.environ[‘flag’]

@app.route('/')
def flag():
    return "<p>" + FLAG + "</p>"
       


if __name__ == '__main__':
    app.run()