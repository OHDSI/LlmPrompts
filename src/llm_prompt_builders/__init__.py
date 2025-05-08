"""OHDSI llm_prompt_builders package root."""

# ---- static string so Hatchling can read the version -----------------------
__version__ = "0.1.3"               # ⬅️  bump for each release
# ---------------------------------------------------------------------------

from importlib.metadata import version, PackageNotFoundError

# Overwrite the placeholder when the package is installed normally;
# keep the static string during editable/dev installs where the metadata
# isn’t yet available.
try:
    __version__ = version(__name__)
except PackageNotFoundError:
    pass
