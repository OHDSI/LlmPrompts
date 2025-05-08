from llm_prompt_builders.utils.stitcher import stitch

def test_stitch():
    assert stitch("r","c","t").startswith("r")
