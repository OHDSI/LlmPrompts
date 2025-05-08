# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Placeholder for upcoming enhancements, bug fixes, and new features.

### Changed
- Placeholder for any breaking or non-breaking changes in progress.

### Fixed
- Placeholder for bug fixes.

## [0.1.0] – 2025-04-22

### Added
- **`src/llm_prompt_builders/prompts/`**: Out‑of‑the‑box prompt templates (classification, extraction, summarization).  
- **`src/llm_prompt_builders/roles/`**: System‑instruction fragments (generic, lifescience, healthcare).  
- **`src/llm_prompt_builders/contexts/`**: Reusable background and few‑shot contexts.  
- **`src/llm_prompt_builders/templates/`**: Modular prompt snippets for custom assembly.  
- **`src/llm_prompt_builders/accelerators/`**: Composition utilities (`chain`, `parallel`, `retry`).  
- **`src/llm_prompt_builders/evaluators/`**: Output validation helpers (semantic similarity).  
- **`src/llm_prompt_builders/pipelines/`**: Pre‑built end‑to‑end workflows (analysis pipeline).  
- **`src/llm_prompt_builders/connectors/`**: LLM provider adapters (OpenAI stub).  
- **`src/llm_prompt_builders/schemas/`**: Pydantic models for structured task outputs.  
- **`src/llm_prompt_builders/config/`**: Default settings and parameter presets.  
- **`src/llm_prompt_builders/utils/`**: Low‑level functions for stitching and formatting.  
- Comprehensive **pytest** coverage mirroring each subpackage under `tests/`.  
- **Sphinx** documentation under `docs/`, with `index.rst` and per‑module reference pages.  
- **GitHub Wiki** starter content in `wiki/Home.md` with contribution guidelines.  
- Enhanced **pyproject.toml** metadata:  
  - Author/Maintainer set to **Gowtham Rao <rao@ohdsi.org>**  
  - ORCID and project URLs under `[project.urls]`  
  - Setuptools `find` configured for `src/`  

### Changed
- N/A

### Fixed
- N/A

---

*This file was generated as part of the 0.1.0 release.*  
