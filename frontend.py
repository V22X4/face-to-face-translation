import streamlit as st
import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from translation import translate_audio
from languages import language_codes
from wav2lip import syncvideo

# Create a Streamlit app
st.title("Video Processor")

audio_path = os.path.abspath("uploads/extracted_audio.wav")
mp3_audio_path = os.path.abspath("uploads/extracted_audio.mp3")
temp_path = os.path.abspath("uploads/temp.mp4")
processed_video_path = os.path.abspath("uploads/finalvideo.mp4")

# Define the filename for the uploaded video
uploaded_video_filename = "uploaded-video.mp4"

# File upload widget for the video
video_file = st.file_uploader("Upload Video", type=["mp4"])

# Dropdown to select the destination language
destination_lang = st.selectbox(
    "Select the destination language",
    list(language_codes.values()),  # Use language names as options
)

# Reverse the dictionary to map the selected language back to its code
destination_lang_code = {v: k for k, v in language_codes.items()}[destination_lang]

# Button to start processing
if st.button("Process"):
    if video_file is None:
        st.error("Please upload a video file.")
    else:
        # Save the uploaded video file with the specified name
        video_path = os.path.join("uploads", uploaded_video_filename)
        os.makedirs("uploads", exist_ok=True)
        with open(video_path, "wb") as vfile:
            vfile.write(video_file.read())

        # Extract audio from the video and save it as .wav
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(audio_path)
        
        video_clip.write_videofile(temp_path, codec="libx264")

        # Read the content of the temporary video file as bytes
        with open(temp_path, "rb") as file:
            video_bytes = file.read()

        # Now you can use the video_bytes in your application
        # os.remove(temp_path)
        
        audio_bytes = audio_clip.to_soundarray().tobytes()


        finalvideo = syncvideo(video_file=video_bytes, audio_file=audio_bytes)

        # # Save the processed video to the specified path
        # os.makedirs("uploads", exist_ok=True)
        # processed_video_path = os.path.join("uploads", "processed_video.mp4")
        # finalvideo.write_videofile(processed_video_path, codec="libx264")

        # # Display the processed video for playback
        # st.video(processed_video_path)
        # # Display the processed video for playback
        # # processed_video_path = "uploads/processed_video.mp4"
        # # st.video(processed_video_path)

        # # Translate and process the audio
        # translate_audio(destination_lang_code)

# Display the uploaded video for playback immediately after uploading
if video_file is not None:
    st.video(video_file)

# Button to download processed video
if st.button("Download Processed Video"):
    if os.path.exists(processed_video_path):
        with open(processed_video_path, "rb") as pfile:
            processed_video_data = pfile.read()
            st.download_button(
                label="Download Processed Video",
                data=processed_video_data,
                key="processed_video.mp4",
                on_click=None,
            )
    else:
        st.warning("Processed video not found. Please process the video first.")

# Define a directory to save processed videos
os.makedirs("uploads", exist_ok=True)

# Define an empty processed video path (will be updated after processing)
processed_video_path = ""
