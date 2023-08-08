from gtts import gTTS, lang
from io import BytesIO
from playsound import playsound
import os

def get_supported_languages():
    return ", ".join(lang.tts_langs().keys())

def text_to_speech(text, lang='en', save_to_file=True, output_file='output.mp3'):
    try:
        tts = gTTS(text=text, lang=lang)
        if save_to_file:
            tts.save(output_file)
            print(f"Audio saved to '{output_file}'")
        else:
            mp3_fp = BytesIO()
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            playsound(mp3_fp)
    except AssertionError:
        print("Error: Text to speech conversion failed. Please check the input text.")
    except ValueError:
        print(f"Error: Unsupported language '{lang}'. Supported languages: {get_supported_languages()}")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")

if __name__ == "__main__":
    text_input = input("Enter the text you want to convert to speech: ")

    while True:
        lang_input = input(f"Enter the language code (default: en). Supported languages: {get_supported_languages()}: ")
        lang_input = lang_input.strip() if lang_input.strip() else 'en'
        if lang_input in lang.tts_langs():
            break
        print(f"Error: Unsupported language '{lang_input}'. Please try again.")

    save_to_file = input("Do you want to save the audio to a file? (yes/no): ").lower() == 'yes'

    if save_to_file:
        output_file = input("Enter the output file name (default: output.mp3): ")
        if not output_file.endswith('.mp3'):
            output_file += 'output.mp3'
    else:
        output_file = None

    text_to_speech(text_input, lang=lang_input, save_to_file=save_to_file, output_file=output_file)