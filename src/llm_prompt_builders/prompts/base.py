from typing import Dict

class Prompt:
    """Represents a parameterized prompt template."""
    def __init__(self, template: str, variables: Dict[str, str]):
        self.template = template
        self.variables = variables

    def render(self) -> str:
        """Renders the prompt with given variables."""
        return self.template.format(**self.variables)
