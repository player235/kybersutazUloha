"""Flask App Project."""

from flask import Flask, jsonify, make_response, request, redirect, url_for
app = Flask(__name__)

SECRET_KEY = os.environ[‘secret_key’]
FLAG = os.environ[‘flag’]

@app.route('/', methods=['GET', 'POST'])
def flag():
    if request.method == 'POST':
        if request.form['password'] == SECRET_KEY:
            return "<p>" + FLAG + "</p>"
        else:
            error = 'Invalid username/password'
    return """<form action="/" method="POST">
  <label for="fname">User:</label><br>
  <input type="text" id="fname" name="fname" value="Admin"><br>
  <label for="lname">Password:</label><br>
  <input type="text" id="password" name="password"><br><br>
  <input type="submit" value="Submit">
</form> """


if __name__ == '__main__':
    app.run()
