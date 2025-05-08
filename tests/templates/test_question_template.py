from llm_prompt_builders.templates.question_template import create_question_prompt

def test_question_prompt():
    q = create_question_prompt("Why?")
    assert "Question: Why?" in q
