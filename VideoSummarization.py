import subprocess
import whisper
from summa import summarizer


def Video_summarize(file_path):
    command = f'ffmpeg -i {file_path} -ab 160k -ar 44100 -vn OutputAudioGen.wav'
    completed_process = subprocess.run(command, shell=True, stderr=subprocess.PIPE)

    if completed_process.returncode != 0:
        print("Error:", completed_process.stderr.decode())
    else:
        print("Conversion successful")
        
    model = whisper.load_model('base')
    result = model.transcribe("OutputAudioGen.wav", fp16=False)
    summary = summarizer.summarize(result["text"])
    return summary

print(Video_summarize("Videos/GradientDescent.mkv"))
