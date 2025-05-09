#!/usr/bin/env python3
"""
Generate docs/index.html listing every callable, no‑arg function in the
`llm_prompt_builders` package together with the string it returns.

Run this from the project root **after** the package has been installed in the
current environment (e.g. `pip install -e .`).  The file it produces can be
served directly by GitHub Pages when the repository is configured to publish
the **docs/** folder.
"""
from __future__ import annotations

import html
import importlib
import inspect
import pkgutil
import sys
from pathlib import Path

# -------- configurable paths -------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parent            # repo root
SRC_DIR = ROOT_DIR / "src"                            # python sources (PEP 621)
PACKAGE_NAME = "llm_prompt_builders"                 # top‑level package
DOCS_DIR = ROOT_DIR / "docs"                         # output folder
OUTPUT_FILE = DOCS_DIR / "index.html"                # final html path
# ----------------------------------------------------------------------------


def iter_modules(pkg_name: str):
    """Yield *fully‑qualified* module names inside *pkg_name* recursively."""
    pkg = importlib.import_module(pkg_name)
    yield pkg.__name__  # include the root module itself
    for module_info in pkgutil.walk_packages(pkg.__path__, prefix=pkg.__name__ + "."):
        yield module_info.name


def public_functions(mod):
    """Return a list of (name, obj) for *mod*'s public functions with **no required params**."""
    for name, obj in inspect.getmembers(mod, inspect.isfunction):
        if obj.__module__ != mod.__name__ or name.startswith("_"):
            continue  # skip re‑exports and private helpers
        sig = inspect.signature(obj)
        if all(
            p.default is not inspect.Parameter.empty or p.kind in (
                inspect.Parameter.VAR_POSITIONAL,
                inspect.Parameter.VAR_KEYWORD,
            )
            for p in sig.parameters.values()
        ):
            yield name, obj, sig


def safe_call(fn):
    """Safely call *fn* without arguments, returning the string result or the error text."""
    try:
        result = fn()
        return str(result)
    except Exception as exc:  # noqa: BLE001
        return f"[ERROR] {exc}"


def build_html(pkg_name: str) -> str:
    """Generate a complete HTML document as a single string."""
    parts: list[str] = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head><meta charset='utf‑8' />",
        "<title>Function outputs – {}</title>".format(pkg_name),
        "<style>body{font-family:sans-serif;max-width:900px;margin:2rem auto;}",
        "h2{border-bottom:1px solid #ddd;padding-bottom:.25rem;}pre{background:#f7f7f7;padding:0.75rem;border-radius:4px;white-space:pre-wrap;}</style>",
        "</head><body>",
        f"<h1>Auto‑generated outputs from <code>{pkg_name}</code></h1>",
        "<p>Only functions that can be executed <em>without arguments</em> are included.</p>",
    ]

    for module_name in sorted(iter_modules(pkg_name)):
        try:
            mod = importlib.import_module(module_name)
        except Exception as exc:  # noqa: BLE001
            print(f"Skipping {module_name}: cannot import ({exc})", file=sys.stderr)
            continue

        funcs = list(public_functions(mod))
        if not funcs:
            continue  # nothing to show

        parts.append(f"<h2>{html.escape(module_name)}</h2>")
        for fname, fobj, sig in funcs:
            result = safe_call(fobj)
            parts.append(f"<h3>{html.escape(fname+str(sig))}</h3>")
            parts.append(f"<pre>{html.escape(result)}</pre>")

    parts.append("</body></html>")
    return "\n".join(parts)


def main() -> None:  # noqa: D401 – imperative mood
    html_doc = build_html(PACKAGE_NAME)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(html_doc, encoding="utf‑8")
    print(f"✔ Wrote {OUTPUT_FILE.relative_to(ROOT_DIR)} (open in browser or commit & push)")


if __name__ == "__main__":
    main()
