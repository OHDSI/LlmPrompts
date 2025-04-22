from .base import Prompt

def entity_extraction(text: str) -> Prompt:
    template = (
        "Extract all named entities from the following text and return as JSON.\n"
        "Text: {text}\n"
        "Entities:"
    )
    return Prompt(template, {"text": text})
