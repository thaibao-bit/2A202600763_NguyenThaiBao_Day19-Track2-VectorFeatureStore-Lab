from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def _read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def test_seeded_corpus_and_golden_set_have_expected_shape() -> None:
    docs = _read_jsonl(DATA / "corpus_vn.jsonl")
    golden = _read_jsonl(DATA / "golden_set.jsonl")

    assert len(docs) == 1000
    assert len(golden) == 50
    assert {doc["topic"] for doc in docs} == {
        "cloud",
        "ai_ml",
        "security",
        "database",
        "networking",
        "devops",
        "mobile",
        "frontend",
        "backend",
        "data_eng",
    }
    assert {"exact", "paraphrase", "mixed"} <= {query["mode_hint"] for query in golden}
    assert all(query["relevant_doc_ids"] for query in golden)
