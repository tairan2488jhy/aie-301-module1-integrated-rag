# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

AIE-301 Module 1 — Integrated RAG: a hands-on RAG engineering project. It builds a Retrieval-Augmented Generation pipeline against a real knowledge source — `docs/raw/Hands-On_Large_Language_Models.md`, a ~300KB markdown book — and evaluates how RAG helps a (local or remote) LLM answer questions about that source.

Guiding principle from the README: *every important RAG concept must be connected to a runnable engineering experiment.* Work loop: build → run → measure → debug → improve → commit → explain.

Intended pipeline:

```
ingestion → chunking → embedding → vector store → retrieval → context construction → LLM → answer
```

Development is experiment-driven (Experiments 1–5 in README): minimal RAG, chunking variants, retrieval-metric evaluation (Recall@K, Precision@K, MRR), dense vs BM25 vs hybrid retrieval, then a fixed developer-question evaluation harness.

## Current implementation state

Early-stage; most of the pipeline is empty scaffolding awaiting implementation.

Implemented:

- `src/chunking/ParagraphLevelChunking.py` — the only working stage so far. Splits the markdown corpus by blank-line paragraph boundaries, counts tokens with tiktoken (`cl100k_base`), and writes JSONL chunks shaped as `{"chunk_index", "text", "token_count", "tag", "version"}` (`TARGET_TOKEN_SIZE = 512`). The file also carries a large self-study Q&A comment block about tokenization.

Empty stubs (0 bytes): `src/rag_pipeline.py`, `evaluation/eval.py`, `evaluation/qa_dataset.json`, plus empty dirs `src/ingestion/`, `src/embeddings/`, `src/retrieval/`. `main.py` is PyCharm hello-world boilerplate, unrelated to the RAG code.

## Running code

No test suite, linter, or build config exists. The venv is a Windows (PyCharm) venv; from WSL invoke it via the Windows interpreter:

```
.venv/Scripts/python.exe src/chunking/FixedSizeChunking.py
```

Chunker notes:

- Paths are hardcoded Windows-relative (`.\docs\raw\...`, inside `main()`), so it only runs under the Windows python from the repo root — not WSL's Linux python.
- Output filename contains a stale typo: `docs/raw/Hands-On_Large_Language_Moeles-FixedSizeChunking.md`.
- On first run tiktoken may download the `cl100k_base` encoder; the offline-cache env vars (`TIKTOKEN_CACHE_DIR`, `TIKTOKEN_DISABLE_MODEL_DOWNLOAD`) are commented out at the top of the file.

## Gotchas

- `.claudeignore` is broken for this repo: it excludes everything (`/**`) and whitelists paths from a different project that don't exist here — Claude Code may be blocked from reading project files until it's rewritten or removed.
- `requirements.txt` is not plain UTF-8 (tokens appear null-padded / UTF-16 mangled), so pip install may choke. Regenerate with `pip freeze > requirements.txt` if the environment needs restoring. Declared stack: langchain, langchain-openai, chromadb, tiktoken, openai. RAGAS and BM25 are cited in the README but not yet installed.