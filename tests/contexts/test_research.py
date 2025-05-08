from llm_prompt_builders.contexts.research import get_research_context

def test_research_context():
    ctx = get_research_context()
    assert "latest scientific literature" in ctx
