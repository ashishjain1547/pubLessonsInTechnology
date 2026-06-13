from flask import Flask, request, jsonify
import os
import uuid
import librosa
from transformers import WhisperProcessor, TFAutoModelForConditionalGeneration

app = Flask(__name__)

# Use the TensorFlow version of the model
model_name = "openai/whisper-tiny"
processor = WhisperProcessor.from_pretrained(model_name)
model = TFAutoModelForConditionalGeneration.from_pretrained(model_name)

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided."}), 400

    audio_file = request.files["audio"]
    # Save the audio file temporarily
    temp_filename = f"temp_{uuid.uuid4().hex}.wav"
    audio_file.save(temp_filename)

    try:
        # Load the audio with librosa and ensure a 16kHz sampling rate
        audio, sr = librosa.load(temp_filename, sr=16000)
        # Process the audio and get input features as a TensorFlow tensor
        inputs = processor(audio, sampling_rate=sr, return_tensors="tf")
        input_features = inputs.input_features

        # Generate transcription using the TF model (generate returns a TF tensor)
        predicted_ids = model.generate(input_features)
        # Convert predicted_ids tensor to numpy before decoding
        transcription = processor.batch_decode(predicted_ids.numpy(), skip_special_tokens=True)[0]
    except Exception as e:
        transcription = f"Error processing audio: {str(e)}"
    finally:
        os.remove(temp_filename)

    return jsonify({"transcription": transcription})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
