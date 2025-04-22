# llmprompts Wiki

Welcome to the **llmprompts** project wiki! This space is for collaborative documentation, guides, and examples.

## Home

### Overview
**llmprompts** is a composable prompt-engineering toolkit. It provides:
- **prompts/** – Curated templates for common NLP tasks.
- **roles/** – System instruction fragments that define personas.
- **contexts/** – Reusable background and few-shot examples.
- **templates/** – Modular prompt snippets.
- **accelerators/** – Functions for chaining, parallel execution, and retries.
- **evaluators/** – Utilities to validate and score outputs.
- **pipelines/** – Pre-built end-to-end workflows.
- **connectors/** – Abstraction over various LLM providers.
- **schemas/** – Pydantic models for structured outputs.
- **config/** – Default settings and presets.
- **utils/** – Helper functions for stitching and formatting.

### Getting Started
1. **Clone the repo**  
   ```bash
   git clone https://github.com/Ohdsi/llmPrompts.git
   cd llmPrompts
   ```
2. **Install**  
   ```bash
   pip install .
   ```
3. **Explore the Modules**  
   - Check out `src/llmprompts/prompts` for ready-to-use prompts.
   - See `src/llmprompts/roles` for available personas.
   - Read examples in `examples/`.

### Contributing
We welcome contributions!  
- Create a new branch for your feature.  
- Add tests under `tests/`.  
- Update this wiki with relevant details.  
- Submit a pull request.

### Contact
For questions, reach out to **Gowtham Rao** at rao@ohdsi.org.
