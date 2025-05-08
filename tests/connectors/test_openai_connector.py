from llmprompts.connectors.openai_connector import OpenAIConnector

def test_openai_connector():
    conn = OpenAIConnector("key")
    assert conn.call("prompt") == "model response"
