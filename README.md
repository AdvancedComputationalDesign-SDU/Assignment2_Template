# Assignment 2: Exploring Fractals through Recursive Geometric Patterns

This repository contains the starter materials for **Assignment 2: Exploring Fractals through Recursive Geometric Patterns**.

---

## Documents

-  **Assignment Brief:** See [BRIEF.md](BRIEF.md) for the full description, tasks, evaluation, and resources.
-  **Write-up Template:** Use [TEMPLATE.md](TEMPLATE.md) to structure your final `README.md` in your submission (pseudo-code, technical explanation, results, references).

---

## Repository structure

```
Assignment2/
├── README.md                 ← your project documentation (this file)
├── BRIEF.md                  ← assignment specification (DO NOT EDIT)
├── TEMPLATE.md               ← write-up structure to follow (Draft here; copy to README.md before submission)
├── fractal_generator.py      ← your code implementation
├── requirements.txt          ← Shapely dependency for the acd environment
└── images/
    ├── fractal1.png
    ├── fractal2.png
    ├── fractal3.png
    └── fractal4.png
```

---

## Working with This Template

**Before submitting, copy your completed `TEMPLATE.md` content into `README.md`, replacing this file's current contents.** Remove unused prompts/placeholders and embed all four result images with captions.

Use [BRIEF.md](BRIEF.md) for the requirements and [TEMPLATE.md](TEMPLATE.md) for your report. Follow the shared [Academic Integrity and AI Tool Use policy](BRIEF.md#academic-integrity-and-ai-tool-use) and include the template's **AI Assistance Record** section in your completed `README.md`.

Develop your recursive baseline, stopping and branching rules, then two spatial influences. Show baseline (both off) / A only / B only / A + B. Use VS Code and the `acd` environment; install `requirements.txt`, then run `python fractal_generator.py`.

The starter supplies function definitions and return contracts, setup, an endpoint helper and basic drawing. Its generating functions are **TODOs**; an unfinished run prints the next TODO without creating an image. Choose your own generation parameters, bounded randomness, reference geometries and appearance mapping. Begin with both influence controls set to `False` for your baseline, then implement and connect the influence hooks with independent controls for enabling each influence.

Once completed, the starter overwrites `images/starter_tree.png` and `images/starter_tree.json` on each run. Use separate PNG/JSON filenames for baseline, A only, B only and A + B, or rename each pair before the next run.
