import pytest

@pytest.mark.parametrize(
    "dotted_path",
    [
        "llm_prompt_builders.roles.generic.get_scientific_editor",
        "llm_prompt_builders.contexts.research.get_research_context",
        "llm_prompt_builders.templates.question_template.create_question_prompt",
        "llm_prompt_builders.accelerators.chain.chain",
    ],
)
def test_can_import(dotted_path):
    module_path, func_name = dotted_path.rsplit(".", 1)
    mod = __import__(module_path, fromlist=[func_name])
    assert hasattr(mod, func_name), f"{dotted_path} missing"


def test_chain_happy_path():
    from llm_prompt_builders.roles.generic import get_scientific_editor
    from llm_prompt_builders.contexts.research import get_research_context
    from llm_prompt_builders.templates.question_template import create_question_prompt
    from llm_prompt_builders.accelerators.chain import chain

    prompt = chain(
        [
            get_scientific_editor(),
            get_research_context(),
            create_question_prompt("What are the study limitations?"),
        ]
    )

    # basic smoke checks
    assert isinstance(prompt, str) and prompt.strip()
    # each piece should appear somewhere in the output
    for fragment in ("scientific", "limitations"):
        assert fragment.lower() in prompt.lower()
