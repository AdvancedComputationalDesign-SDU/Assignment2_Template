# Assignment 2: Fractal Generation Documentation

> Use this as the structure for your write-up. While developing, document here; **before submitting, copy the completed content into `README.md`.**

## Table of Contents

- [Pseudo-Code](#pseudo-code)
- [Technical Explanation](#technical-explanation)
- [Geometric Influences](#geometric-influences)
- [Parameters & Seeds](#parameters--seeds)
- [Appearance Mapping](#appearance-mapping)
- [Experiments](#experiments)
- [Challenges and Solutions](#challenges-and-solutions)
- [References](#references)

---

## Pseudo-Code

*(Provide detailed pseudo-code explaining the logic of your program. This should clearly outline your recursive functions, parameter definitions, and how they contribute to the final fractal pattern.)*

Example:

1. **Define Main Function `generate_fractal(start_point, angle, length, depth)`**
   - **Inputs**:
     - `start_point`: Tuple of coordinates (x, y).
     - `angle`: Current angle in degrees.
     - `length`: Length of the current line segment.
     - `depth`: Current recursion depth.
   - **Process**:
     - **If** `(depth == 0) or (distance_to_goal < ε) or (local_density > τ) or (curvature_budget <= 0)`:
       - **Return** (End recursion).
     - **Else**:
       - Calculate `end_point` using trigonometry:
         - `end_x = start_x + length * cos(radians(angle))`
         - `end_y = start_y + length * sin(radians(angle))`
       - Create a line from `start_point` to `end_point` using Shapely.
       - **For** each branch (e.g., left and right):
         - **Calculate** new angle:
           - Left branch: `new_angle = angle + angle_change`
           - Right branch: `new_angle = angle - angle_change`
         - **Calculate** new length:
           - `new_length = length * length_scaling_factor`
         - **Recursive Call**:
           - `generate_fractal(end_point, new_angle, new_length, depth - 1)`
     - **Return** (After recursive calls).

2. **Initialize Parameters**
   - Set `start_point`, `initial_angle`, `initial_length`, `recursion_depth`, `angle_change`, `length_scaling_factor`.
   - ```python
     import random
     random.seed(SEED)  # record SEED in the report
     ```

3. **Call `generate_fractal` Function**
   - Begin the fractal generation by calling `generate_fractal(start_point, initial_angle, initial_length, recursion_depth)`.

4. **Visualization**
   - Collect all the lines generated.
   - Use Matplotlib to plot the lines.
   - Apply any visualization enhancements (colors, line widths).

---

## Technical Explanation

*(Provide a concise explanation of your code, focusing on recursion and geometric manipulations. Discuss how your approach generates the final fractal pattern and the mathematical principles involved.)*

Example:

In my implementation, the `generate_fractal` function recursively draws line segments representing branches of a fractal tree. The function calculates the end point of each line using trigonometric functions based on the current angle and length.

At each recursion step, the function:

- Decreases the `length` by multiplying it with `length_scaling_factor`.
- Adjusts the `angle` by adding or subtracting `angle_change` to create branching.
- Calls itself recursively for each branch until the `recursion_depth` reaches zero.

This approach creates a self-similar pattern characteristic of fractals, where each branch splits into smaller branches in a consistent manner.

---

## Geometric Influences

*(Describe at least two geometric influences you chose to incorporate, such as attractors/repulsors, fields, region-aware rules, obstacles/clipping, self-avoidance, adaptive recursion, multi-scale scaling. Explain how these influences are computed and where in the recursion or growth process they modulate the fractal growth.)*

---

## Parameters & Seeds

| Figure | Axiom/Init | Depth | Angle Δ | Length L | Scale s | Influences | Seed | Notes |
|---|---|---:|---:|---:|---:|---|---|---|
| 1 | ... | ... | ... | ... | ... | ... | 42 | ... |

Record every figure’s parameter set and SEED. You may also print a small run dictionary for traceability:
```python
RUN = dict(seed=SEED, depth=DEPTH, angle=ANGLE, scale=S, influences=['attractor','obstacle'])
print('Run:', RUN)
```

---

## Appearance Mapping

*(Explain how you map visual properties such as color, line width, or opacity to meaningful signals like recursion depth, curvature, or distance to attractors. Justify your choices and how they enhance the visualization.)*

---

## Experiments

*(Include minimum four distinct outputs, each with parameters and random seed recorded.)*

- Compare runs with the same parameters but different seeds to observe stochastic variation.
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
  - **Solution**: Controlled randomness via ranges and fixed `random.seed` per run.

---

## References

*(List any resources you used or found helpful during the assignment.)*

- **Shapely Manual**: [https://shapely.readthedocs.io/en/stable/manual.html](https://shapely.readthedocs.io/en/stable/manual.html)
- **Matplotlib Pyplot Tutorial**: [https://matplotlib.org/stable/tutorials/introductory/pyplot.html](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)

---

*(Feel free to expand upon these sections to fully capture your work and learning process.)*