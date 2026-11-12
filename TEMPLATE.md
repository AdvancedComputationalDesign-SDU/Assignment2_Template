# Assignment 2: Fractal Generation Documentation

> Use this as the structure for your write-up. While developing, document here; **before submitting, copy the completed content into `README.md`, replacing its current contents.** Remove unused prompts/placeholders and embed all four result images with captions.

## Table of Contents

- [Pseudo-Code](#pseudo-code)
- [Technical Explanation](#technical-explanation)
- [Geometric Influences](#geometric-influences)
- [Parameters & Seeds](#parameters--seeds)
- [Appearance Mapping](#appearance-mapping)
- [Experiments](#experiments)
- [Challenges and Solutions](#challenges-and-solutions)
- [Development Record](#development-record)
- [AI Assistance Record](#ai-assistance-record)
- [References](#references)

---

## Pseudo-Code

### Algorithm Specification

Use these prompts to shape your existing pseudo-code and explanation; they are not a separate submission:

- **Intention:** What should the design do, and why?
- **Inputs and representation:** What values, array shapes, units, or coordinate systems do you use?
- **Rules:** What is calculated, selected, repeated, or updated, and in what order?
- **Constraints:** What must remain true, including at boundaries or invalid inputs?
- **Evidence:** What small test or comparison would show that the result matches your intention?

*(Provide detailed pseudo-code explaining the logic of your program. This should clearly outline your recursive functions, parameter definitions, and how they contribute to the final fractal pattern.)*

Use the starter's function definitions as contracts, then write **your own pseudo-code** for the generating logic:

| Function | Inputs | Expected return |
| --- | --- | --- |
| `generate_fractal` | Position, heading, length, depth, settings, scene and shared random generator | A fresh list of `{"geometry": LineString, "depth": int}` records; `[]` when nothing is produced |
| `growth_rule` | Current growth state, settings and scene | Finite `(angle, length)` after your spatial response |
| `accept_segment` | Candidate LineString, depth, settings and scene | Boolean accepting or rejecting the candidate |
| `build_design` (supplied) | Settings and scene | A fresh seeded run of your generator |
| `draw_result` (supplied) | Axes, records and scene | Draws the returned geometry |

Specify what one recursive call creates, your stopping conditions and progress, how children derive their state from the parent, and how returned records are combined. Explain where your two influences are queried and applied and how their controls produce the four comparison cases. Do not substitute an unexplained copy of the class tree for these decisions.

---

## Technical Explanation

*(Provide a concise explanation of your code, focusing on recursion and geometric manipulations. Discuss how your approach generates the final fractal pattern and the mathematical principles involved.)*

Explain your own baseline, termination and branching choices. What state is passed to a child, what changes at each generation, and why does the process stop? Describe how the spatial rules modify this baseline and credit any starting approach you adapted.

---

## Geometric Influences

For each of your two influences, name the query, its input and output, the rule that uses it, and a small expected result. State whether it changes growth parameters or accepts/rejects a proposed segment, and explain their distinct roles and combined effect. Use the same upward-counting depth convention as the starter, or explicitly document and consistently apply an alternative.

*(Describe the two spatial influences you chose, such as attraction and obstacle avoidance. Explain each query, geometric response and position in the recursive process.)*

---

## Parameters & Seeds

| Figure | Axiom/Init | Depth | Angle Δ | Length L | Scale s | Active influences | Seed | Notes |
|---|---|---:|---:|---:|---:|---|---|---|
| Baseline | ... | ... | ... | ... | ... | None | 42 | ... |
| A only | ... | ... | ... | ... | ... | A | 42 | ... |
| B only | ... | ... | ... | ... | ... | B | 42 | ... |
| A + B | ... | ... | ... | ... | ... | A and B | 42 | ... |

Record every figure’s parameter set and SEED. You may also print a small run dictionary for traceability:
```python
RUN = dict(seed=SEED, max_depth=DEPTH, angle=ANGLE, influence_a_on=True, influence_b_on=True)
# Include your own generation and randomness settings as well.
print('Run:', RUN)
```

---

## Appearance Mapping

*(Explain how you map visual properties such as color, line width, or opacity to meaningful signals like recursion depth, curvature, or distance to attractors. Justify your choices and how they enhance the visualization.)*

---

## Experiments

*(Include four related outputs: baseline (both off) / A only / B only / A + B, with parameters, active influences and seed recorded. Use common view limits.)*

- Keep other settings fixed: compare A only and B only with the baseline, then explain their interaction in A + B. Explain how random draws are controlled; a separate small repeatability check can demonstrate seeded variation.
- Discuss sensitivity of the fractal pattern to parameter changes and geometric influences.

---

## Challenges and Solutions

*(Discuss any challenges you faced during the assignment and how you overcame them.)*

Example:

- **Challenge**: Managing the growing number of line segments and ensuring they are correctly plotted.
  - **Solution**: Stored all line segments in a list and plotted them after the recursion completed.

- **Challenge**: Implementing randomness without losing the overall structure.
  - **Solution**: Introduced randomness within controlled bounds for angles and lengths.

- **Challenge**: Ensuring stochastic variation remained reproducible.
  - **Solution**: Controlled randomness via ranges and a fresh `random.Random(seed)` per run.

---

## Development Record

Every student completes this compact record; reuse your experiment figures and checks.

- **Intention and prediction:** What recursive and spatial relationship did you investigate, and what did you expect? Credit your starting approach and identify your own baseline/rule decisions.
- **Meaningful revision:** Show a before/after rule, excerpt, diff, or commit and explain the decision and effect.
- **Checks:** Trace a small recursive case, check each spatial query at a known location/boundary, and repeat a seeded run. State expectations, observations and conclusions.
- **Study conclusion:** What did baseline / A only / B only / A + B reveal about each influence and their combination, and which settings did you select?
- **Learning and limitations:** What do you understand better, and what remains uncertain about your recursive and spatial rules?

---

## AI Assistance Record

Follow the [AI policy](BRIEF.md#academic-integrity-and-ai-tool-use). If you used no AI, write **“I did not use AI tools for this assignment.”** and omit the tool/interaction prompts below. Retain the Development Record.

A recursion trace, known Shapely query or controlled comparison can support both records.

### Tools and Scope

Name each interface, model/version where known, approximate date, mode (chat, autocomplete, or agent), purpose, and affected parts of the submission. Unknown details can be stated as unknown.

### Selected Interactions

Select **two or three consequential interactions where available**, or fewer if fewer occurred. For each:

1. **Request and response:** Include the actual prompt or agent instructions and a relevant response/code excerpt. For routine autocomplete without a prompt, identify a representative accepted change.
2. **Contribution:** Identify the affected file/block and a before/after excerpt, diff, or commit. If assistance was conceptual only, state that. Credit an AI-supplied initial approach.
3. **Decision:** Explain what you accepted, adapted, or rejected and why. An AI error or rejection is not required.
4. **Check and learning:** State your expectation, the result you personally inspected, your conclusion, and what you learned or still question. Distinguish agent-created tests or executed commands from your own interpretation. Refer to existing development evidence where relevant.

For coding agents, identify affected files or relevant changes and what you retained. A full transcript is not routinely required. Remove credentials and private personal information from excerpts.

---

## References

*(List any resources you used or found helpful during the assignment.)*

- **Shapely Manual**: [https://shapely.readthedocs.io/en/stable/manual.html](https://shapely.readthedocs.io/en/stable/manual.html)
- **Matplotlib Pyplot Tutorial**: [https://matplotlib.org/stable/tutorials/introductory/pyplot.html](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)

---

*(Feel free to expand upon these sections to fully capture your work and learning process.)*
