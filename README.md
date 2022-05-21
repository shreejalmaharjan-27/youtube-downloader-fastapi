# Installation
You need [Python 3](https://www.python.org/downloads/) to run this.


### Install Dependencies
Install needed YTDL and FastAPI Libraries with pip by executing following command into your terminal or command line: `pip install youtube-dl "fastapi[all]"`

### Clone the Repository
`git clone https://github.com/shreejalmaharjan-27/youtube-downloader-django.git`

### Get to the repository directory
`$ cd youtube-downloader-django/`

### Run
Execute `python3 main.py` from your terminal and the app should be running at port `10111`.

### Usage
Make requests to the app with `url` parameter
For eg: `curl localhost:10111?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ`