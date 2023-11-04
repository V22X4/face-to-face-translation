import os
import speech_recognition as sr
from translate import Translator
from gtts import gTTS
from languages import language_codes


def translate_audio(destination_lang):
    # Input audio file path
    # input_audio_path = input("Enter the path to the input audio file: ")
    input_audio_path = "uploads/extracted_audio.wav"

    # Check if the input audio file exists
    if not os.path.isfile(input_audio_path):
        print("Input audio file does not exist.")
        return

    # Initialize the recognizer 
    recognizer = sr.Recognizer()

    # Convert the input audio to text
    with sr.AudioFile(input_audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            input_text = recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
            return
        except sr.RequestError as e:
            print(
                f"Could not request results from Google Speech Recognition service; {e}"
            )
            return

    # print("Available destination languages:")
    # for code, name in language_codes.items():
    #     print(f"{code}: {name}")

    # Translate the text to the destination language
    translator = Translator(to_lang=destination_lang)
    translated_text = translator.translate(input_text)

    # Generate speech from the translated text
    tts = gTTS(translated_text, lang=destination_lang)

    # Save the speech as an audio file
    audio_file_path = "uploads/translated_audio.wav"
    tts.save(audio_file_path)

    print(
        "Text-to-speech conversion completed. You can find the audio in 'output.mp3'."
    )

    # Play the generated audio (optional)
#     play_audio(audio_file_path)


# def play_audio(audio_file_path):
#     try:
#         os.system(f"start {audio_file_path}")
#     except Exception as e:
#         print(f"Failed to play audio: {str(e)}")


