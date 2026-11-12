"""Data loaders, integrity verifiers, and concordance queries for Russell's geometric treatises."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


def get_repo_root() -> Path:
    """Return the root directory of the ``geometor/bertrand-russell`` repository."""
    return Path(__file__).resolve().parents[3]


def apparatus_slug(key: str) -> str:
    """Convert an apparatus key into the deterministic anchor slug used by ``publish``."""
    return re.sub(r"[^a-z0-9]+", "-", (key or "").lower()).strip("-")


@dataclass(frozen=True)
class RussellLocus:
    """Locus reference inside one of Russell's geometric treatises (1897 or 1903)."""

    chapter: str
    sections: tuple[str, ...]
    pages: str
    anchor: str
    verbatim_excerpt: str = ""


@dataclass(frozen=True)
class ExternalLocus:
    """Cross-corpus locus connecting Russell to Hoenen, Heath's Euclid, Pappus, Hilbert, or Wildberger."""

    corpus: str
    work: str
    locus: str
    relation: str


@dataclass(frozen=True)
class ConcordanceEntry:
    """Structured bidirectional concordance entry across Russell's 1897/1903 treatises and GEOMETOR."""

    id: str
    theme: str
    russell_1903: RussellLocus
    russell_1897: RussellLocus
    external_loci: tuple[ExternalLocus, ...]


def load_sources_manifest(repo_root: Path | None = None) -> dict[str, Any]:
    """Load ``resources/bertrand_russell/sources_manifest.json``."""
    root = repo_root or get_repo_root()
    path = root / "resources" / "bertrand_russell" / "sources_manifest.json"
    return json.loads(path.read_text(encoding="utf-8"))


def verify_source_checksums(repo_root: Path | None = None) -> list[tuple[str, bool]]:
    """Verify SHA-256 digests and byte lengths of all archived primary source files."""
    root = repo_root or get_repo_root()
    manifest = load_sources_manifest(root)
    results: list[tuple[str, bool]] = []
    for work in manifest.get("works", []):
        for file_entry in work.get("files", []):
            rel_path = file_entry["path"]
            fpath = root / rel_path
            if not fpath.is_file():
                results.append((rel_path, False))
                continue
            data = fpath.read_bytes()
            digest = hashlib.sha256(data).hexdigest()
            ok = len(data) == file_entry["bytes"] and digest == file_entry["sha256"]
            results.append((rel_path, ok))
    return results


def load_concordance(repo_root: Path | None = None) -> list[ConcordanceEntry]:
    """Load and parse all entries from ``resources/bertrand_russell/concordance.json``."""
    root = repo_root or get_repo_root()
    path = root / "resources" / "bertrand_russell" / "concordance.json"
    raw = json.loads(path.read_text(encoding="utf-8"))
    entries: list[ConcordanceEntry] = []
    for item in raw.get("entries", []):
        r1903 = item["russell_1903"]
        r1897 = item["russell_1897"]
        entries.append(
            ConcordanceEntry(
                id=item["id"],
                theme=item["theme"],
                russell_1903=RussellLocus(
                    chapter=r1903["chapter"],
                    sections=tuple(str(s) for s in r1903["sections"]),
                    pages=r1903["pages"],
                    anchor=r1903["anchor"],
                    verbatim_excerpt=r1903.get("verbatim_excerpt", ""),
                ),
                russell_1897=RussellLocus(
                    chapter=r1897["chapter"],
                    sections=tuple(str(s) for s in r1897["sections"]),
                    pages=r1897["pages"],
                    anchor=r1897["anchor"],
                    verbatim_excerpt=r1897.get("verbatim_excerpt", ""),
                ),
                external_loci=tuple(
                    ExternalLocus(
                        corpus=ext["corpus"],
                        work=ext["work"],
                        locus=ext["locus"],
                        relation=ext["relation"],
                    )
                    for ext in item.get("external_loci", [])
                ),
            )
        )
    return entries


def find_concordance_by_corpus(
    corpus_query: str, repo_root: Path | None = None
) -> list[ConcordanceEntry]:
    """Return concordance entries referencing a given corpus substring (e.g. ``'hoenen'``, ``'euclid'``)."""
    needle = corpus_query.strip().lower()
    return [
        entry
        for entry in load_concordance(repo_root)
        if any(needle in ext.corpus.lower() for ext in entry.external_loci)
    ]


def find_concordance_by_section(
    work: str, section: int | str, repo_root: Path | None = None
) -> list[ConcordanceEntry]:
    """Return concordance entries linked to a numbered section in ``'1903'`` or ``'1897'``."""
    sec_str = str(section).strip()
    out: list[ConcordanceEntry] = []
    for entry in load_concordance(repo_root):
        locus = entry.russell_1903 if "1903" in work or "pom" in work.lower() else entry.russell_1897
        if sec_str in locus.sections:
            out.append(entry)
    return out


def load_apparatus_registries(repo_root: Path | None = None) -> dict[str, dict[str, Any]]:
    """Load ``citations.json``, ``persons.json``, and ``glossary.json`` from ``resources/``."""
    root = repo_root or get_repo_root()
    res = root / "resources"
    return {
        "citations": json.loads((res / "citations.json").read_text(encoding="utf-8")),
        "persons": json.loads((res / "persons.json").read_text(encoding="utf-8")),
        "glossary": json.loads((res / "glossary.json").read_text(encoding="utf-8")),
    }
