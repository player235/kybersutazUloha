"""Flask App Project."""

from flask import Flask, jsonify, make_response, request, redirect, url_for
app = Flask(__name__)

SECRET_KEY = os.environ[‘secret_key’]
ADMIN_ID = os.environ[‘admin_id’]
FLAG = os.environ[‘flag’]

@app.route('/')
def user():
    if request.cookies.get('userID') == ADMIN_ID:
        return redirect(url_for('flag'))
    resp = make_response("<p>Hello user, too sad you're only an user. You can't do anything!</p>")
    resp.set_cookie('userID', "")
    return resp

@app.route('/flag', methods=['GET', 'POST'])
def flag():
    if request.cookies.get('userID') != ADMIN_ID:
        return redirect(url_for('user'))
    if request.method == 'POST':
        if request.form['password'] == SECRET_KEY:
            return "<p>" + FLAG + "</p>"
        else:
            error = 'Invalid username/password'
    return """<form action="/flag" method="POST">
  <label for="fname">User:</label><br>
  <input type="text" id="fname" name="fname" value="Admin"><br>
  <label for="lname">Password:</label><br>
  <input type="text" id="password" name="password"><br><br>
  <input type="submit" value="Submit">
</form> """


if __name__ == '__main__':
    app.run()
