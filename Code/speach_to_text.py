import os
import whisper
import subprocess


def main():
    video_path = os.path.abspath("./Speech to Text/video.mp4")
    audio_path = os.path.splitext(video_path)[0] + ".wav"


    def extract_audio(video_path, audio_path):
        command = ['ffmpeg', '-i', video_path, '-q:a', '0', '-map', 'a', audio_path]
        subprocess.run(command, check=True)

    extract_audio(video_path, audio_path)
    
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)

    transcription_path = os.path.splitext(video_path)[0] + "_transcription.txt"
    with open(transcription_path, "w") as f:
        f.write(result["text"])

if __name__ == "__main__":
    main()
