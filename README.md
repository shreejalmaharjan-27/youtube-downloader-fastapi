# Installation
You need [Python 3](https://www.python.org/downloads/) to run this.


### Install Dependencies
Install needed YTDL and FastAPI Libraries with pip by executing following command into your terminal or command line: `pip install youtube-dl "fastapi[all]"`

### Clone the Repository
`git clone https://github.com/shreejalmaharjan-27/youtube-downloader-fastapi.git`

### Get to the repository directory
`$ cd youtube-downloader-fastapi/`

### Run
Execute `python3 main.py` from your terminal and the api should be running at port `10111`.

### Usage
Make requests to the api with `url` parameter
For eg: `curl http://localhost:10111?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ`

### Play signed YouTube videos (eg: from YouTube Music & so on.)
Make request to `/stream` endpoint with `url` parameter with urlencoded googlevideo url and it will return video/audio stream

For eg: `curl http://localhost:10111/stream?url=https%3A%2F%2Frr1---sn-cvh76ner.googlevideo.com%2Fvideoplayback%3Fexpire%3D1653153965%26ei%3DTcyIYu_BNMfKgAPMkIewBw%26ip%...`