import os
import whisper
import subprocess

def extract_audio(video_path, audio_path):
        command = ['ffmpeg', '-i', video_path, '-q:a', '0', '-map', 'a', audio_path]
        subprocess.run(command, check=True)


def speach_to_text():
    #video_path = os.path.abspath("./Speech to Text/video.mp4")
    video_path = os.path.abspath(r"./Files/video/video.mp4")
    audio_path = os.path.splitext(video_path)[0] + ".wav"

    extract_audio(video_path, audio_path)
    
    model = whisper.load_model("medium")
    result = model.transcribe(audio_path)
    
    return result["text"]

