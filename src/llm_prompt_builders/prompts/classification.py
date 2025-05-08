from .base import Prompt

def sentiment_analysis(text: str) -> Prompt:
    template = (
        "Analyze the sentiment of the following text and respond with 'Positive', 'Negative', or 'Neutral'.\n"
        "Text: {text}\n"
        "Sentiment:"
    )
    return Prompt(template, {"text": text})
