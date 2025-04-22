from typing import Any

def evaluate_semantic(response: str, expected: str) -> float:
    """Dummy semantic similarity evaluator."""
    return 1.0 if response.strip() == expected.strip() else 0.0
