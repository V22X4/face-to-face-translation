def syncvideo(video_file, audio_file):

    import requests

    # Define the API endpoint URL
    api_url = "http://3d3d-35-231-33-121.ngrok-free.app/upload"

    # # Load video and audio files
    # video_file = open("video.mp4", "rb")
    # audio_file = open("audio.mp3", "rb")

    # Create a dictionary containing the files
    files = {
    'video': ('video.mp4', video_file),
    'audio': ('audio.mp3', audio_file)
    }

    # Send a POST request
    print("reach")
    response = requests.post(api_url, files=files)
    print("comple")

    # Handle the API response
    if response.status_code == 200:
        print("API request successful")
        print(response.text)
        # return response
    else:
        print("API request failed with status code:", response.status_code)
        # print(response.text)

    # Close the file handles
    # video_file.close()
    # audio_file.close()