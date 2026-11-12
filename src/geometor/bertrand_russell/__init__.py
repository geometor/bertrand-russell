"""Scholarly Book Codex and cross-corpus concordance for Bertrand Russell's treatises on geometry."""

from geometor.bertrand_russell.compile_codex import compile_all
from geometor.bertrand_russell.concordance import (
    ConcordanceEntry,
    ExternalLocus,
    RussellLocus,
    apparatus_slug,
    find_concordance_by_corpus,
    find_concordance_by_section,
    get_repo_root,
    load_apparatus_registries,
    load_concordance,
    load_sources_manifest,
    verify_source_checksums,
)
from geometor.bertrand_russell.diagrams import generate_all_diagrams

__version__ = "0.1.0"

__all__ = [
    "ConcordanceEntry",
    "ExternalLocus",
    "RussellLocus",
    "__version__",
    "apparatus_slug",
    "compile_all",
    "find_concordance_by_corpus",
    "find_concordance_by_section",
    "generate_all_diagrams",
    "get_repo_root",
    "load_apparatus_registries",
    "load_concordance",
    "load_sources_manifest",
    "verify_source_checksums",
]
