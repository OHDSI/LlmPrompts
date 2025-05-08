"""Basic unit tests for llm_prompt_builders helpers.
Run with `pytest -q` from repo root.
"""

import pytest

from llm_prompt_builders.accelerators.chain import chain
from llm_prompt_builders.roles.generic import get_scientific_editor
from llm_prompt_builders.templates.question_template import create_question_prompt


def test_chain_concatenates_with_newlines():
    fragments = ["first", "second", "third"]
    assert chain(fragments) == "first\nsecond\nthird"


def test_get_scientific_editor_contains_role_phrase():
    role_text = get_scientific_editor()
    assert isinstance(role_text, str)
    assert "scientific editor" in role_text.lower()


def test_create_question_prompt_includes_question():
    question = "What are the study limitations?"
    prompt = create_question_prompt(question)

    # The helper should echo the question text somewhere in the prompt
    assert question in prompt

    # Ensure a question mark is preserved
    assert "?" in prompt


@pytest.mark.parametrize(
    "fragments, expected",
    [
        ([], ""),
        (["only"], "only"),
        (["a", "b"], "a\nb"),
    ],
)
def test_chain_various_lengths(fragments, expected):
    assert chain(fragments) == expected


def test_end_to_end_chain_with_role_and_question():
    role = get_scientific_editor()
    question_prompt = create_question_prompt("Explain your methods.")

    combined = chain([role, question_prompt])

    # Both fragments should appear in the chained prompt
    assert role in combined
    assert "Explain your methods." in combined
