#!flask/bin/python

# Derived from:
# http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

from flask import Flask
from flask import Response
from flask import request, redirect, url_for
import cv2
import trumpatize

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world!\n'


@app.route('/api/', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        return redirect(url_for('api_about'))
    else:
        # Get image
        img = cv2.imread("test/img/bern1.jpg", -1)

        # Trumpatize
        img = trumpatize.addhat(img)

        # Return
        [retval, buf] = cv2.imencode(".jpg", img)
        return Response(buf.tobytes(), mimetype='image/jpg')


@app.route('/api/about.html')
def api_about():
    return 'This is our API!'


if __name__ == '__main__':
    app.run(debug=True)
