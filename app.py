import os
APP_NAME  = os.environ.get("APP_NAME", "")
APP_HOST  = os.environ.get("APP_HOST", "0.0.0.0")
APP_PORT  = int(os.environ.get("APP_PORT", 80))
DEBUG  = [True, False][int(os.environ.get("DEBUG", 0))]

try:
    from local_settings import *
except:
    pass

from flask import Flask, request, abort, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html",
        title = 'Home',
        app_name = APP_NAME)


if __name__ == "__main__":
    app.debug = DEBUG
    app.run(host=APP_HOST, port=APP_PORT)