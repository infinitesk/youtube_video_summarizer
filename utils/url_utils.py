from urllib.parse import urlparse, parse_qs

def get_video_id(youtube_video_url):
    parsed_url = urlparse(youtube_video_url)

    # Extract video ID based on the URL format
    if parsed_url.netloc in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed_url.query).get("v", [None])[0]
    elif parsed_url.netloc == "youtu.be":
        return parsed_url.path[1:]
    return None

def is_valid_youtube_url(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc in ["www.youtube.com", "youtube.com", "youtu.be"]
