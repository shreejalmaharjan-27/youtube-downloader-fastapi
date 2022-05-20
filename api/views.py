from django.http import JsonResponse
import youtube_dl

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

def index(request):
    realDeal = None
    url = request.GET.get("url")
    if(url == ''):
        status = "you haven't specified a url"
    elif(url):
        realDeal = getInfo(url)
    data = {
        "data" : realDeal if realDeal else None,
        "status": "success" if realDeal else "check your url parameters",
        "error": False if realDeal else True
    }
    return JsonResponse(data)