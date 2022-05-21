import youtube_dl
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = ["*"] # 👈 add domains as an array to allow only specified domains to access api

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET"],
    allow_headers=["*"],
)

def isAV(s):
    if str(s).lower() == 'none':
        return False
    else:
        return True
        
def getInfo(url):

    with youtube_dl.YoutubeDL() as ydl:

        try:
            info = ydl.extract_info(url, download = False)
        except:
            return None

        result = []

        for item in info['formats']:
            result.append({
                "url": item['url'],
                "audio": isAV(item['acodec']),
                "video": isAV(item['vcodec']),
                "height": item['height'],
                "width": item['width'],
                "fps": item['fps'],
                "format": item['format_note'],
                "format_id": item['format_id'],
                "audio_codec": item['acodec'],
                "video_codec": item['vcodec']
            })

        return result


@app.get("/")
async def root(url: str = None):
    realDeal = None
    if url:
        realDeal = getInfo(url)
    data = {
        "data" : realDeal if realDeal else None,
        "status": "success" if realDeal else "check your url parameters",
        "error": False if realDeal else True
    }
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10111)