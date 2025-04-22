from .base import Prompt

def bullet_summary(text: str) -> Prompt:
    template = (
        "Summarize the following text into concise bullet points.\n"
        "Text: {text}\n"
        "Summary:"
    )
    return Prompt(template, {"text": text})
