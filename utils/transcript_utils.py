from youtube_transcript_api import YouTubeTranscriptApi, CouldNotRetrieveTranscript
from utils.url_utils import get_video_id

def extract_transcript_details(youtube_video_url):
    try:
        # Extract the video ID
        video_id = get_video_id(youtube_video_url)
        if not video_id:
            return "Invalid YouTube link."

        # Get the transcript
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([item["text"] for item in transcript_text])
        return transcript

    except CouldNotRetrieveTranscript:
        return "Transcript not available for this video."
    except Exception as e:
        return f"Error: {str(e)}"
