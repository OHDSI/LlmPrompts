from llmprompts.schemas.models import EntitiesResponse, Entity

def test_entities_response():
    er = EntitiesResponse(entities=[{"text":"a","label":"L"}])
    assert er.entities[0].text == "a"
