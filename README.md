# llmprompts

A **composable** prompt-engineering toolkit:

- **prompts/** – production-ready templates  
- **roles/** – system instruction fragments  
- **contexts/** – reusable background or few-shot examples  
- **templates/** – granular snippet templates  
- **accelerators/** – orchestration functions (chain, parallel, retry)  
- **evaluators/** – output validation utilities  
- **pipelines/** – end-to-end workflow constructs  
- **connectors/** – LLM provider adapters  
- **schemas/** – Pydantic models for structured outputs  
- **config/** – default settings and presets  
- **utils/** – helper functions  

## Installation

```bash
pip install llmprompts
```

## Quick Start

```python
from llmprompts.roles.generic import get_scientific_editor
from llmprompts.contexts.research import get_research_context
from llmprompts.templates.question_template import create_question_prompt
from llmprompts.accelerators.chain import chain

role = get_scientific_editor()
context = get_research_context()
template = create_question_prompt("What are the study limitations?")
prompt = chain([role, context, template])
print(prompt)
```
