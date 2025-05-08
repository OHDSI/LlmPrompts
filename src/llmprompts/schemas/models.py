from pydantic import BaseModel
from typing import List

class Entity(BaseModel):
    text: str
    label: str

class EntitiesResponse(BaseModel):
    entities: List[Entity]
