from llmprompts.prompts.classification import sentiment_analysis

def test_sentiment_analysis():
    prompt = sentiment_analysis("Test")
    assert "Text: Test" in prompt.render()
