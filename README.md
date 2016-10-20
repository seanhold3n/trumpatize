# Trumpatize-me!
*The world's first DTHaaS (Donald Trump Hats as a Service) API and client!*

## Setup
Trumpatize-me is written in Python 2.7 with the help of the following packages:
* **OpenCV** for image processing tasks
* **Flask** for handling API calls

On Ubuntu/Debian Linux, you may install these using the following commands:
```bash
sudo pip install -r requirements.txt
sudo apt-get install python-opencv
```


## Usage
Trumpatize-me has two parts: the **API** that allows you to upload images to be "trumpatized", and a **client** that trumpatizes your webcam video.

#### Client
1. Make sure that OpenCV is installed and that you have a webcam.  (Flask is only used for the API)
2. Run **main.py**
3. Enjoy!

#### API server
1. Make sure that OpenCV and Flask are installed.
2. Run **api_server.py**.
3. Congrats!  Your computer is now hosting the API!

The API accepts a POST packet with the following parameters:

| parameter | required? | values            |
| ---       | ---       | ---               |
| image     | yes       | (your image)      |
| hat_type  | no        | red, white, camo  |

A sample curl request is as follows:
```bash
curl -o bernie_with_hat.jpg \
    -F hat_type=red \
    -F image=@bernie.jpg \
    http://trumpatize.me/api/
```

NOTE: http://trumpatize.me site does not currently have API support. (coming soon!) 

When the API server runs on your computer, the default port used by Flask is 5000.  Thus, to test the API locally, the url would be *http://localhost:5000/api/*