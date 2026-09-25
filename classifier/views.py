from pathlib import Path

from django.shortcuts import render
from .forms import TextInputForm
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / 'gru_model.keras'
TOKENIZER_PATH = BASE_DIR / 'tokenizer.pkl'

# Load model and tokenizer
model = tf.keras.models.load_model(MODEL_PATH)
with open(TOKENIZER_PATH, 'rb') as handle:
    tokenizer = pickle.load(handle)

MAX_LEN = 100  # Same as used during training

def classify_text(request):
    number = 0
    result = None  # Default result
    if request.method == "POST":
        form = TextInputForm(request.POST)
        if form.is_valid():
            # Get user input
            user_text = form.cleaned_data['text']

            # Tokenize and pad the input
            sequences = tokenizer.texts_to_sequences([user_text])
            padded_sequence = pad_sequences(sequences, maxlen=MAX_LEN, padding='post')

            # Make a prediction
            prediction = model.predict(padded_sequence)
            number = prediction[0][0]
            result = "AI-Generated" if prediction[0][0] > 0.5 else "Human-Written"
    else:
        form = TextInputForm()

    return render(request, 'classifier/classify_text.html', {'form': form, 'result': result ,'number': number})
