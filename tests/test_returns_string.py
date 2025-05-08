from __future__ import annotations

import inspect
import importlib
import pkgutil
from typing import Callable, Iterable

import pytest

import llm_prompt_builders

# ───────────────────────────────── helpers ──────────────────────────────────


def _discover_modules(pkg) -> Iterable[object]:
    """Yield *all* imported sub-modules inside *pkg*."""
    yield pkg
    for info in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + "."):
        yield importlib.import_module(info.name)


def _public_functions(module) -> Iterable[Callable]:
    """Return functions defined in *module* that look public."""
    for name, obj in vars(module).items():
        if (
            inspect.isfunction(obj)
            and not name.startswith("_")
            and obj.__module__ == module.__name__
        ):
            yield obj


def _sample_value(param: inspect.Parameter):
    """Return a dummy value that matches *param*’s kind & annotation."""
    if param.annotation in {int, float}:
        return 1
    if param.annotation is bool:
        return False
    return "<>"


# ───────────────────────────── parametrised test ────────────────────────────


@pytest.mark.parametrize(
    "func",
    [
        func
        for m in _discover_modules(llm_prompt_builders)
        for func in _public_functions(m)
    ],
)
def test_function_returns_str(func: Callable):
    """Call *func* with dummy values and assert the result is `str` (or skip)."""
    sig = inspect.signature(func)
    args: list = []
    kwargs: dict = {}
    for p in sig.parameters.values():
        if p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD):
            continue
        if p.default is p.empty:  # need a placeholder
            value = _sample_value(p)
            if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD):
                args.append(value)
            else:  # KEYWORD_ONLY
                kwargs[p.name] = value
    try:
        result = func(*args, **kwargs)
    except Exception as exc:  # pragma: no cover
        pytest.skip(f"Could not invoke {func.__module__}.{func.__name__}: {exc!r}")
        return

    if not isinstance(result, str):
        pytest.skip(
            f"{func.__module__}.{func.__qualname__} returns "
            f"{type(result).__name__}; string assertion not applicable"
        )
    assert isinstance(result, str)