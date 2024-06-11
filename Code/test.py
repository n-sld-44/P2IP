from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import soundfile as sf
import numpy as np

# Charger le processeur et le modèle large de Whisper
processor = WhisperProcessor.from_pretrained("openai/whisper-large")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large")

# Assurez-vous que le modèle est configuré pour la reconnaissance en français
model.config.forced_decoder_ids = processor.get_decoder_prompt_ids(language="fr", task="transcribe")

# Fonction pour rééchantillonner l'audio
def resample_audio(audio, orig_sr, target_sr):
    duration = audio.shape[0] / orig_sr
    new_length = int(duration * target_sr)
    new_audio = np.interp(
        np.linspace(0.0, duration, new_length, endpoint=False),
        np.linspace(0.0, duration, audio.shape[0], endpoint=False),
        audio
    )
    return new_audio

# Charger l'audio (assurez-vous que le fichier audio est au format WAV)
audio_input, sample_rate = sf.read(r"C:\Users\Nath\Desktop\test.wav")

# Si l'audio est en stéréo, le convertir en mono
if len(audio_input.shape) > 1 and audio_input.shape[1] > 1:
    audio_input = np.mean(audio_input, axis=1)  # Convertir en mono

# Rééchantillonner l'audio à 16 kHz si nécessaire
target_sample_rate = 16000
if sample_rate != target_sample_rate:
    audio_input = resample_audio(audio_input, sample_rate, target_sample_rate)

# Préparer l'audio pour le modèle
input_features = processor(audio_input, sampling_rate=target_sample_rate, return_tensors="pt").input_features

# Générer la transcription
with torch.no_grad():
    predicted_ids = model.generate(input_features)

# Convertir les identifiants prévus en texte
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

print("Transcription:", transcription)
