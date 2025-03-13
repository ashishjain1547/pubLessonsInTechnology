from flask import Flask, request, jsonify
import os
import uuid
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import librosa

app = Flask(__name__)

# Load the processor and model from Hugging Face
model_name = "openai/whisper-tiny"
processor = WhisperProcessor.from_pretrained(model_name)
model = WhisperForConditionalGeneration.from_pretrained(model_name)

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided."}), 400

    audio_file = request.files["audio"]
    # Save the incoming audio file temporarily
    temp_filename = f"temp_{uuid.uuid4().hex}.wav"
    audio_file.save(temp_filename)

    try:
        # Load the audio using librosa and resample to 16kHz
        audio, sr = librosa.load(temp_filename, sr=16000)
        # Process audio into input features expected by the model
        input_features = processor(audio, sampling_rate=sr, return_tensors="pt").input_features
        # Generate transcription (default generation parameters; adjust if needed)
        predicted_ids = model.generate(input_features)
        transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    except Exception as e:
        transcription = f"Error processing audio: {str(e)}"
    finally:
        os.remove(temp_filename)

    return jsonify({"transcription": transcription})

if __name__ == "__main__":
    # Run the server on port 5000 and listen on all interfaces.
    app.run(host="0.0.0.0", port=5000, debug=True)
