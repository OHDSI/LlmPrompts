# -*- coding: utf-8 -*-
"""
Initializes the contexts module, making context-providing functions easily accessible.

This file imports functions from specific context modules (like lifescience, research)
and defines __all__ to control what is exported when using 'from llmprompts.contexts import *'.
"""

# Import functions from the lifescience context module
from .lifescience_context import (
    get_commercialization_concepts,
    get_competitive_intelligence_context,
    get_cross_functional_collaboration_model,
    get_drug_development_overview,
    get_evidence_generation_strategy,
    get_gxp_context,
    get_medical_affairs_function_context,
    get_pharma_stakeholder_overview,
    get_product_lifecycle_management_context,
    get_regulatory_basics,
)

# Import functions from the research context module
from .research import get_research_context

# Define the public API for the contexts module
__all__ = [
    # Lifescience Contexts
    "get_commercialization_concepts",
    "get_competitive_intelligence_context",
    "get_cross_functional_collaboration_model",
    "get_drug_development_overview",
    "get_evidence_generation_strategy",
    "get_gxp_context",
    "get_medical_affairs_function_context",
    "get_pharma_stakeholder_overview",
    "get_product_lifecycle_management_context",
    "get_regulatory_basics",
    # Research Contexts
    "get_research_context",
]

