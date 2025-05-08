# in llm_prompt_builders/cli/build_site.py
import json, inspect, importlib, pkgutil, pathlib, jinja2, sys
from importlib import resources

ROOT = pathlib.Path(__file__).resolve().parents[2]      # repo root
DOCS = ROOT / "docs"
DATA = DOCS / "assets" / "prompts.json"

def catalog():
    out = {}
    for mod in pkgutil.walk_packages(
            importlib.import_module("llm_prompt_builders").__path__,
            "llm_prompt_builders."
    ):
        m = importlib.import_module(mod.name)
        funcs = {
            n: getattr(m, n)()
            for n, obj in inspect.getmembers(m, inspect.isfunction)
            if not n.startswith("_") and obj.__module__.startswith("llm_prompt_builders")
        }
        if funcs:
            out[mod.name.split(".")[-1]] = funcs
    return out

def render():
    env = jinja2.Environment(loader=jinja2.PackageLoader(__package__, "templates"))
    (DOCS / "assets").mkdir(parents=True, exist_ok=True)
    DATA.write_text(json.dumps(catalog(), indent=2))

    tpl = env.get_template("index.html.j2")
    (DOCS / "index.html").write_text(tpl.render(json_path="assets/prompts.json"))

if __name__ == "__main__":
    render()
    print("Static site written to /docs – ready for gh-pages.")
