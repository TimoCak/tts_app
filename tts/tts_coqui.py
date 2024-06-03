import torch 
from TTS.api import TTS

context = {
    "model": "",
    "emotion": "",
    "speed": 2.0,
    "text": "",
}

def do_voicing(model, emotion, speed, text):
    # Get device
    device = "cuda" if torch.cuda.is_available() else "cpu"

    print(TTS().list_models())

    # Init TTS
    tts = TTS(model).to(device)

    context['model'] = model
    context['emotion'] = emotion
    context['speed'] = speed
    context['text'] = text

    tts.tts_to_file(text=text, file_path="static/audio.wav", emotion=emotion, speed=speed)