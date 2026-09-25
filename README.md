# Human or AI

A Django web app that classifies a piece of text as **human-written** or **AI-generated**. You paste text into a form; a trained GRU model scores it and returns a label plus a confidence value.

## How it works

1. The home page (`/`) shows a text form.
2. Submitted text is tokenized with a saved Keras tokenizer and padded to length 100 (the same length used in training).
3. A GRU model (`gru_model.keras`) outputs a score between 0 and 1.
4. Scores above `0.5` are labeled **AI-Generated**; otherwise **Human-Written**. The raw score is shown as confidence.

## Project layout

- `manage.py` — Django entry point
- `HumanOrAi/` — project settings and URL config
- `classifier/` — the classification app (form, view, template)
- `gru_model.keras` — trained GRU classifier (keep this in the project root)
- `tokenizer.pkl` — tokenizer used at training time (keep this in the project root)

## Requirements

- Python 3.10+
- [Django 4.2](https://www.djangoproject.com/)
- TensorFlow / Keras

## Setup

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/), enter text, and click **Classify**.

Place `gru_model.keras` and `tokenizer.pkl` in the project root (next to `manage.py`). The app loads them on startup.

## License

This is a university project. Add a license file if you want to specify reuse terms.
