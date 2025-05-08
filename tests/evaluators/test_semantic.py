from llm_prompt_builders.evaluators.semantic import evaluate_semantic

def test_evaluate_semantic():
    assert evaluate_semantic("x", "x") == 1.0
