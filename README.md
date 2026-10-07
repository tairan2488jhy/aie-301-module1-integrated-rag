# AIE-301 Module 1 — Integrated RAG

A hands-on RAG engineering project for **AIE-301 Production RAG Engineering**.

This project builds a Retrieval-Augmented Generation (RAG) system using a real software-development project as the knowledge source.

The goal is not to build a toy RAG demo, but to understand and evaluate how RAG can help a local LLM work with a real software project.

## Project Goal

Build a practical pipeline:

```text
Software Project
      ↓
Document / Code Ingestion
      ↓
Chunking
      ↓
Embedding
      ↓
Vector Store
      ↓
Retrieval
      ↓
Context Construction
      ↓
Local / Remote LLM
      ↓
Developer Answer
```

The system should help answer questions such as:

* Where is a particular feature implemented?
* How does a request flow through the application?
* Where is an exception handled?
* Which files are related to a specific component?
* What code or documentation should be inspected before making a change?

## Learning Objectives

Through this project, I will practice:

* Document and source-code ingestion
* Chunking strategies
* Embedding
* Vector search
* Top-K retrieval
* Retrieval evaluation
* Metadata filtering
* Hybrid retrieval
* RAG failure analysis
* RAG pipeline engineering
* Production-oriented design decisions

The main learning loop is:

```text
Build
  ↓
Run
  ↓
Measure
  ↓
Debug
  ↓
Improve
  ↓
Commit
  ↓
Explain in English
```

## Technology Stack

* Python
* LangChain
* OpenAI-compatible Embedding API
* Chroma
* tiktoken
* RAGAS
* BM25

The stack may evolve as the experiments progress.

## Project Structure

```text
AIE_301_Module_1_Integrated_RAG/
│
├── README.md
│
├── src/
│   ├── ingestion/
│   ├── chunking/
│   ├── embeddings/
│   ├── retrieval/
│   └── rag_pipeline.py
│
├── evaluation/
│   ├── qa_dataset.json
│   └── eval.py
│
├── experiments/
│
├── docs/
│
└── requirements.txt
```

## Experiments

The project will gradually compare different RAG approaches.

### Experiment 1 — Minimal RAG

```text
Project Files
    ↓
Recursive Chunking
    ↓
Embedding
    ↓
Chroma
    ↓
Top-K Retrieval
```

### Experiment 2 — Chunking

Compare different chunk sizes and overlap settings.

### Experiment 3 — Retrieval

Measure retrieval quality using metrics such as:

* Recall@K
* Precision@K
* MRR

### Experiment 4 — Hybrid Retrieval

Compare:

```text
Dense Retrieval
      vs
BM25
      vs
Hybrid Retrieval
```

### Experiment 5 — Evaluation

Build a fixed developer-question dataset and evaluate retrieval quality systematically.

## Engineering Principle

This project follows one important rule:

> Every important RAG concept should be connected to a runnable engineering experiment.

The objective is not to memorize RAG terminology.

The objective is to build, measure, debug, and explain a working RAG system.

## Current Status

**Module 1 — Integrated Engineering Lab**

Status:

> 🚧 In Progress

Completed:

* RAG fundamentals
* Document processing
* Chunking
* Embedding
* Retrieval

Current focus:

> Build the first runnable Developer Knowledge RAG pipeline.

## Future Extensions

Potential future work includes:

* Code-aware chunking
* AST / Tree-sitter based retrieval
* Git history retrieval
* Parent-child retrieval
* Reranking
* Query rewriting
* Agentic retrieval
* Software architecture / dependency-aware retrieval

These are intentionally outside the first minimal implementation.

## Learning Context

This repository is part of:

**AIE — AI Agent Engineering**

Course:

**AIE-301 Production RAG Engineering**

Module:

**Module 1 — RAG Fundamentals & Knowledge Pipeline**

The project is designed to become a practical portfolio artifact while developing production-oriented RAG engineering skills.
