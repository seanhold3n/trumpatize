#!flask/bin/python

# Derived from:
# http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

from flask import Flask
from flask import Response
import cv2
import trumpatize

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world!\n'

@app.route('/api')
def api():
    # Get image
    img = cv2.imread("test/img/bern1.jpg", -1)

    # Trumpatize
    img = trumpatize.addhat(img)

    # Return
    [retval, buf] = cv2.imencode(".jpg", img)
    return Response(buf.tobytes(), mimetype='image/jpg')

if __name__ == '__main__':
    app.run(debug=True)
