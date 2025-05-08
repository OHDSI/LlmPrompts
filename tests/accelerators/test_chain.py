from llmprompts.accelerators.chain import chain

def test_chain():
    assert chain(["a", "b"]) == "a\nb"
