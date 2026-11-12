# Assignment 2: Exploring Fractals through Recursive Geometric Patterns

![Example Fractal](images/example.png)

## Objective

In this assignment you will implement a **recursive generator** and enrich it with **two geometric influences** that shape how the structure grows in space. You will work with geometric primitives (lines, polylines) using **Shapely** and render the results (e.g., with Matplotlib). The core of the assignment is to **couple recursive growth with spatial rules** such as attraction, repulsion, or a geometric stopping condition to produce expressive, controllable patterns.

While the branching or growth approach can be inspired by L-systems, it does not have to be strictly L-system based. You are encouraged to explore recursive generation methods influenced by spatial constraints and geometric rules that govern how the fractal develops and interacts with its environment. This opens opportunities to experiment with recursive branching logic, adaptive scaling, and spatial modulation beyond formal grammar rewriting.

---

## Table of Contents

- [Learning Goals](#learning-goals)
- [Tasks](#tasks)
- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [Instructions](#instructions)
- [Advanced Challenges (Optional)](#advanced-challenges-optional)
- [Submission Guidelines](#submission-guidelines)
- [Evaluation Criteria](#evaluation-criteria)
- [Resources](#resources)
- [Academic Integrity and AI Tool Use](#academic-integrity-and-ai-tool-use)
- [Contact](#contact)

---

### Learning goals

- Design and implement a recursive generator (e.g., L-system or direct branching) and geometric interpretation pipeline.
- Combine **recursive rules** with **spatial reasoning** (distance, intersection, fields).
- Practice recursion, parameterization, and reproducible randomness.
- Communicate methodology and results clearly.
- Develop awareness of how spatial rules (fields, attractors, obstacles) can modulate recursive growth processes.

---

## Tasks

1. **Implement Recursive Generator**

   - Create a Python script (`fractal_generator.py`) that uses recursive functions to generate fractal patterns. This can be based on L-system–style string rewriting or direct recursive branching logic.
   - Design and implement the **baseline generator, stopping conditions and branching rules yourself**, as well as the spatial influences below. The starter supplies function definitions and return contracts, not a completed recursive tree. Explain what one call creates, how children inherit state and why recursion terminates.
   - Use the **Shapely** library to create and manipulate geometric objects, specifically for drawing lines and polylines.
   - Define the parameters of your fractal explicitly in your script. Examples include:
     - **Starting Point**: The initial coordinate from which the pattern generation starts.
     - **Initial Angle**: The starting orientation of the pattern.
     - **Angle Change**: The angle by which the direction changes at each recursive step.
     - **Length**: The initial length of the lines drawn.
     - **Length Scaling Factor**: How the length of lines changes with each recursion.
     - **Recursion Depth**: The generation level along a branch, starting at `0` for the root; `max_depth` is the highest included level.
   - Allow customization of these parameters to enable exploration of different fractal patterns.
   - Incorporate bounded randomness in a geometric parameter and use a fixed seed for reproducibility. Set `params["seed"]` before calling `build_design(params, scene)`. The supplied wrapper creates a fresh local generator and passes it to your generating functions as `rng`; use that argument for random draws. For angular variation, add your own `angle_jitter` setting before using this example:

      ```python
      params["seed"] = 42  # choose and record the seed for this run
      params["angle_jitter"] = 3.0  # example bound in degrees; choose your own
      # Inside your generating functions, use their supplied rng argument:
      variation = rng.uniform(-params["angle_jitter"], params["angle_jitter"])
      ```

2. **Geometric Influences**

   - Integrate **two distinguishable spatial influences** into your recursive generator. Choose influences with different, meaningful roles in your design, such as attraction toward a point and avoidance of an obstacle. Examples include:
     - Attractors and Repulsors: Points or regions that pull or push growth directions.
     - Fields: Scalar or vector fields influencing direction or length.
     - Region-Aware Rules: Growth constrained within or outside specific areas.
     - Obstacles/Clipping: Preventing intersections or pruning branches.
     - Self-Avoidance: Avoiding self-intersections or overlap.
     - Adaptive Recursion: Modulating recursion depth or branching based on spatial context.
   - Both influences should meaningfully affect the fractal's structure and appearance. Explain each query and response, then how they work together. Keep a safe depth limit even when using a geometric stopping condition.

3. **Generate Distinct Outputs**

   - Produce **four related outputs** from one system: **baseline (both influences off), influence A only, influence B only, and influences A + B together**. Keep the scene and other settings fixed. Compare each influence alone with the baseline, then explain their combined effect. The final result may be one of these outputs.
   - Save each output as an image in the `images/` folder with descriptive filenames.
   - Record the parameter sets and random seeds used for each output to ensure reproducibility.

4. **Visualization and Appearance Mapping**

   - Use Matplotlib to plot your fractal patterns.
   - Map visual appearance attributes such as color and stroke thickness to meaningful signals like recursion depth, curvature, or distance to attractors.
   - Enhance your visualizations with custom color schemes or gradients to improve interpretability and aesthetics.
   - When saving, export a clean, tight image (not a full UI figure): hide axes/margins and save tightly.

      ```python
      import matplotlib.pyplot as plt
      fig, ax = plt.subplots()
      # ... draw your geometry on ax ...
      ax.set_aspect('equal', adjustable='box')
      ax.axis('off')
      plt.margins(0)
      plt.savefig('images/output.png', bbox_inches='tight', pad_inches=0, dpi=300)
      plt.close(fig)
      ```

5. **Experiments**

   - Use the four-output comparison to explore how each influence and their combination affect the fractal outcome. Record a prediction, the observed effects and your final selection.
   - Document your observations and insights regarding the interplay between recursive growth and spatial modulation.

6. **Documentation**

   - Write detailed pseudo-code explaining your recursive functions in `README.md` using a similar structure to the template provided in `TEMPLATE.md`.
   - Provide technical explanations of your algorithms and geometric influences.
   - Include a short report discussing the process and the mathematical principles behind the fractals you created.
   - Insert images of your generated fractals into the documentation.
   - Discuss challenges faced and how you addressed them. Include the template’s **Development Record** and **AI Assistance Record**, or an explicit no-AI statement.

---

## Getting Started

### Prerequisites

- **Python 3.x**, using the existing `acd` environment in VS Code
- **Shapely**
- **Matplotlib**
- **NumPy**

From your repository folder:

```sh
conda activate acd
python -m pip install -r requirements.txt
python fractal_generator.py
```

The starter provides setup, an endpoint helper, fresh seeded runs and basic drawing. `generate_fractal()`, `growth_rule()` and `accept_segment()` have **TODOs with input/return contracts**. Running the unfinished starter prints the next TODO and produces no result image. Choose your own generation parameters, bounded randomness, reference geometries and appearance mapping. Implement your recursive baseline with both influence controls set to `False` first, then implement the two spatial influences with independent controls for enabling them individually. An unused hook can explicitly return unchanged growth or accept the candidate.

Once the generating TODOs are completed, the script saves `images/starter_tree.png` and a settings/scene record in `images/starter_tree.json`. **These fixed filenames are overwritten on every run.** Change both output filenames for each case, or rename the exported PNG/JSON pair before running the next case. Keep four distinct pairs, for example `baseline`, `A_only`, `B_only` and `combined`. Embed the four images with explanatory captions in your `README.md`. No Rhino is needed for A2.

### Suggested Structure

- Maintain state variables such as position, heading (angle), current length, and scaling factor.
- Pass position, heading, length and depth to recursive calls; define where children start and how they inherit or change that state.
- Employ Shapely for geometric operations like line creation, intersection tests, attractor distance calculations, and containment queries.
- Structure your code to cleanly separate recursion logic, spatial influence computations, and visualization.

## Repository Structure

```
Assignment2/
├── README.md
├── BRIEF.md
├── TEMPLATE.md
├── fractal_generator.py
├── requirements.txt
├── images/
│   ├── fractal1.png
│   ├── fractal2.png
│   ├── fractal3.png
│   ├── fractal4.png
│   └── (Additional images)
```

Requirements highlight: implement **two spatial influences**, show **baseline / A only / B only / A + B**, record parameters and seeds, and save clean generated images.

---

## Instructions

### From a Recursive Rule to Geometric Influence

Plan a small, unmodified baseline first. In the starter, `depth` counts upward from `0`; a branch is generated when `depth <= max_depth`. Identify the base case and the progress toward it before adding spatial rules.

Separate a **query** (for example, distance to an attractor or intersection with an obstacle) from its **response** (for example, adjusted branch length or rejection of a segment). The `growth_rule` and `accept_segment` function contracts identify the possible responses; you implement and connect them in your own recursion. Place your two influences in either or both hooks as appropriate, and explain their input/output contracts. Two copies of the same query/response at different locations do not automatically establish two distinct roles. The supplied `build_design(params, scene)` validates settings, creates a fresh random generator and calls your generating function.

Use a low depth to predict a few branches. For a binary rule creating one segment per accepted call, with no rejection or length stop, inclusive maximum depths 0, 1 and 2 produce 1, 3 and 7 segments. Predict the corresponding small case for your own rule. The supplied settings wrapper limits `max_depth` to 0–10; you must still implement the actual stopping conditions and progress in your recursion. Compare the four required outputs using common view limits. Pruning can change later random draws; disable jitter for a clean comparison and show seeded variation in a small repeatability check, or explain how you control per-branch random values. These checks do not require extra presentation images.

1. **Clone the Repository**

   - Accept the assignment on GitHub Classroom and clone the repository to your local machine using GitHub Desktop or the command line.

2. **Set Up Your Environment**

   - Ensure all dependencies are installed.
   - Familiarize yourself with the repository structure.

3. **Implement the Recursive Generator**

   - Open `fractal_generator.py`.
   - Define parameters explicitly: starting point, initial angle, angle change, length, length scaling factor, recursion depth.
   - Implement recursive branching logic that creates line segments and updates position and orientation.
   - Use Shapely for geometric operations.
   - Implement two spatial influences with distinct roles. Each query must affect geometry; drawing a reference point or obstacle alone is insufficient.
   - Map visual appearance attributes (color, stroke thickness) to meaningful signals such as recursion depth or distance to attractors.

4. **Generate and Save Outputs**

   - Run your baseline, A-only, B-only and A + B configurations to generate four related results.
   - Save each output image in the `images/` folder with descriptive filenames.
   - Record the parameter sets and random seeds for each output to ensure reproducibility.

5. **Documentation**

   - Write detailed pseudo-code and explanations in `README.md`.
   - Describe your recursive functions, geometric influences, and visualization mappings.
   - Include images of your fractals with commentary.

6. **Version Control with Git**

   - Make regular commits with meaningful messages.
   - Push your commits to the GitHub repository.

7. **Review and Finalize**

   - Ensure your code is well-commented and clean.
   - Verify that all generated images are saved correctly.
   - Double-check your documentation for clarity and completeness.

---

## Advanced Challenges (Optional)

These are optional directions, not additional submission requirements. Keep the core study two-dimensional. Extensions carry no automatic bonus.

### Extending to 3D Space

- **Implement 3D Fractals**:
  - Introduce a Z-axis and modify your recursive function to handle 3D coordinates.
  - Adjust geometric transformations to include rotations around X, Y, and Z axes.
  - Handle position and orientation in 3D space.

- **Visualizing in 3D**:
  - Use `mpl_toolkits.mplot3d` in Matplotlib:

    ```python
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs)
    plt.show()
    ```

  - Or use `plotly` for interactive 3D plots:

    ```python
    import plotly.graph_objects as go

    fig = go.Figure(data=[go.Scatter3d(x=xs, y=ys, z=zs, mode='lines')])
    fig.show()
    ```

### Custom Color Schemes

- **Color Based on Depth**:

  ```python
  import matplotlib.pyplot as plt

  def get_color(depth, max_depth):
      fraction = depth / max_depth if max_depth > 0 else 0.0
      return plt.cm.viridis(fraction)

  # Plot using the color
  color = get_color(current_depth, max_depth)
  ```

- **Color Gradients**:
  - Use color maps to apply gradients along the lines.
  - Consider using libraries like `matplotlib.colors` for advanced color manipulations.

### Advanced Base Cases for Recursion

- Explore alternative termination conditions beyond fixed recursion depth, such as:
  - Proximity to a goal/attractor (terminate when distance < ε).
  - Local density threshold (terminate when nearby segments exceed a count or length per area).
  - Curvature/turn-limit based termination (stop when cumulative bend exceeds a budget).
  - Proximity to obstacles or boundaries (terminate or reroute when within a buffer).

---

## Submission Guidelines

- **What to Submit**:
  - Your `fractal_generator.py` script and any additional scripts.
  - Completed `README.md` with pseudo-code, explanations, and short report: **copy your completed `TEMPLATE.md` content into `README.md`, replacing its current contents**. Remove unused prompts/placeholders and embed all four result images with captions.
  - Generated images saved in the `images/` folder.

- **Submission Checklist**:
  - [ ] Code runs without errors.
  - [ ] Code is well-commented and follows best practices (e.g., consistent naming conventions).
  - [ ] Two meaningful spatial influences are implemented and explained, with safe recursion stopping.
  - [ ] Appearance mapping (color, stroke thickness) is linked to meaningful signals.
  - [ ] Four related outputs (baseline / A only / B only / A + B) are saved, with parameters, active influences and seeds recorded.
  - [ ] `README.md` includes the Development Record, AI Assistance Record or no-AI statement, and source credits.
  - [ ] The completed template has replaced the starter README; prompts/placeholders are removed and all four images display with captions.
  - [ ] All changes are committed with meaningful messages.
  - [ ] All commits are pushed to your GitHub repository.

---

## Evaluation Criteria

- **Implementation of Recursive Functions**
  - Correct use of recursion in generating fractal patterns using geometric transformations with Shapely.
  - Your own implemented baseline, stopping conditions, branching rule and parent-to-child state transfer; explain any adaptation from course examples.
  - Ability to customize parameters and generate different outputs.

- **Geometric Influences**
  - Quality, correctness, and meaningful integration of two spatial influences with distinguishable geometric effects.
  - Demonstrated understanding of how spatial rules modulate growth.

- **Visualization**
  - Clear, informative mapping of color/line width/opacity to signals (depth, curvature, distance to features).
  - Legible composition and export (axes off, tight bounds).

- **Documentation**
  - Detailed pseudo-code and technical explanations.
  - Clear discussion of algorithms, parameters, and geometric influences. Feel free to include diagrams to explain your geometric rules.
  - Inclusion and analysis of generated fractal images.

- **Variety and Control**
  - Control of one system, demonstrated by the four related outputs and an explained geometric effect.
  - Reproducibility ensured by recording parameters and random seeds.

- **Use of Git and Version Control**
  - Regular commits with meaningful messages.
  - Proper repository structure and organization.

Originality means your explained rule and its effect; research-level novelty is not expected. Be ready to trace your recursion and explain your individual portfolio work orally.

---

## Resources

- **Python Official Documentation**: [https://docs.python.org/3/](https://docs.python.org/3/)
- **Shapely Documentation**: [https://shapely.readthedocs.io](https://shapely.readthedocs.io)
- **Matplotlib Documentation**: [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)
- **NumPy Documentation**: [https://numpy.org/doc/](https://numpy.org/doc/)
- **Plotly Documentation**: [https://plotly.com/python/](https://plotly.com/python/)
- **L-Systems**: [https://en.wikipedia.org/wiki/L-system](https://en.wikipedia.org/wiki/L-system)

---

## Academic Integrity and AI Tool Use

AI assistance is optional; no paid service is required. Explanations, feedback, debugging, refactoring, and implementation assistance are permitted. You remain responsible for submitted code, tests, figures, mathematics, and writing, including adapted or manually retyped generated material.

In your **AI Assistance Record**:

1. **Tools and scope:** Name each interface, model/version where known, approximate date, mode (chat, autocomplete, or agent), and affected parts of the submission.
2. **Selected interactions:** Include two or three consequential interactions where available: actual prompts or agent instructions, relevant response/code excerpts, and enough context to interpret them. Report fewer if fewer occurred. Summarize routine autocomplete with a representative accepted change when there was no prompt.
3. **Contribution and decision:** Identify the affected file/block and a before/after excerpt, diff, or commit. Explain what you accepted, adapted, or rejected and why. If assistance was conceptual only, say so. Credit an AI-supplied initial approach and explain how you developed it. An AI error or rejected suggestion is not required.
4. **Checks and learning:** State an expectation you can explain, a result you personally inspected, your conclusion, and what you learned or still question. Distinguish agent-written tests or agent-executed commands from your own interpretation. For agents, identify affected files or the relevant diff and retained changes. Reuse Development Record evidence where relevant.

A complete conversation history is not routinely required. Remove credentials and private personal information from excerpts. If you used no AI, state that explicitly and complete the same Development Record.

Permitted AI use itself attracts no penalty; students using no AI can meet every criterion. Prompt quantity or an AI-generated reflection alone does not establish understanding. Describe the actual development process and credit generated contributions. Cite original sources as well as acknowledging AI, and respect licenses.

Conceptual discussion and feedback are welcome. Your individual submission must represent your decisions and understanding; do not copy another student's solution or share a complete solution for others to submit. The [SDU generative AI rules](https://sdunet.dk/en/undervisning-og-eksamen/uddannelse/vejledning/gai) and course examination rules apply.

---

## Contact

If you have any questions or need assistance, please reach out to the instructor via email or the course forum.

---
