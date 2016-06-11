from flask import Flask, render_template, session, request, abort, g

import os


app = Flask(__name__)


@app.route('/')
def index():
    """Just a generic index page to show."""
    app_name = os.environ.get('FLASK_APP_NAME', 'Nothing Set')
    instance_name = os.environ.get('FLASK_INSTANCE_NAME', '')
    return render_template('index.html', app_name = app_name, instance_name = instance_name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)