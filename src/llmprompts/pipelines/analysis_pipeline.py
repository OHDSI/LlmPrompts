from llmprompts.accelerators.chain import chain
from llmprompts.prompts.summarization import bullet_summary

def analyze_and_summarize(text: str) -> str:
    fragments = [bullet_summary(text).render()]
    return chain(fragments)
