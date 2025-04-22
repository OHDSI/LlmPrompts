from llmprompts.utils.stitcher import stitch

def test_stitch():
    assert stitch("r","c","t").startswith("r")
