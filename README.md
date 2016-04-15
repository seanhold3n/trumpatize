# Trumpatize-me!
*The world's first DTHaaS (Donald Trump Hats as a Service) API and client!*

## Setup
Trumpatize-me is written in Python 2.7 with the help of the following packages:
* **OpenCV** for image processing tasks
* **Flask** for handling API calls

On Linux, you may install these using the following commands:
```bash
sudo apt-get install python-opencv
sudo pip install Flask
```
*Note that apt is the package manager for Debian/Ubuntu Linux.*


## Usage
Trumpatize-me has two parts: the **API** that allows you to upload images to be "trumpatized", and a **client** that trumpatizes your webcam video.

#### Client
1. Make sure that OpenCV is installed and that you have a webcam.  (Flask is only used for the API)
2. Run **main.py**
3. Enjoy!
