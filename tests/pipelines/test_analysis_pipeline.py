from llm_prompt_builders.pipelines.analysis_pipeline import analyze_and_summarize

def test_analysis_pipeline():
    result = analyze_and_summarize("Hello")
    assert isinstance(result, str)
