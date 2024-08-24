import streamlit as st
from utils.transcript_utils import extract_transcript_details
from utils.gemini_utils import generate_gemini_content
from utils.url_utils import get_video_id, is_valid_youtube_url

# Streamlit UI
st.title("YouTube Transcript Summary")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    if is_valid_youtube_url(youtube_link):
        video_id = get_video_id(youtube_link)
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    else:
        st.error("Invalid URL. Please enter a valid YouTube video link.")

if st.button("Get Summary"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text == "Invalid YouTube link.":
        st.error("Invalid URL. Please enter a valid YouTube video link.")
    elif transcript_text == "Transcript not available for this video.":
        st.error("Transcript not available for this video.")
    elif "Error" in transcript_text:
        st.error(transcript_text)  # Display any other errors
    else:
        prompt = """You are a YouTube video summarizer. You will be taking the transcript text
        and summarizing the entire video and providing the important summary in points
        within 250 words. Please provide the summary of the text given here: """
        
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)
