# Assignment 2: Exploring Fractals through Recursive Geometric Patterns

![Example Fractal](images/example.png)

## Objective

In this assignment you will implement an **L‑system–based recursive generator** and enrich it with **geometric influences** that shape how the structure grows in space. You will work with geometric primitives (lines, polylines) using **Shapely** and render the results (e.g., with Matplotlib). The core of the assignment is to **couple formal grammar growth with spatial rules** such as attractor/repulsor points, fields, and collision constraints to produce expressive, controllable patterns.

---

## Table of Contents

- [Learning Goals](#learning-goals)
- [Tasks](#tasks)
- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [Instructions](#instructions)
- [Advanced Challenges (Optional for Extra Points)](#advanced-challenges-optional-for-extra-points)
- [Submission Guidelines](#submission-guidelines)
- [Evaluation Criteria](#evaluation-criteria)
- [Resources](#resources)
- [Contact](#contact)

---

### Learning goals

- Design and implement an L‑system expansion and geometric interpretation pipeline.
- Combine **symbolic rules** with **spatial reasoning** (distance, intersection, fields).
- Practice recursion, parameterization, and reproducible randomness.
- Communicate methodology and results clearly.

---

## Tasks

1. **Implement Recursive Geometric Script**

   - Create a Python script (`fractal_generator.py`) that uses recursive functions to generate fractal patterns based on geometric transformations.
   - Use the **Shapely** library to create and manipulate geometric objects, specifically for drawing lines and polylines.
   - Define the parameters of your fractal explicitly in your script such as:
     - **Starting Point**: The initial coordinate from which the pattern generation starts.
     - **Initial Angle**: The starting orientation of the pattern.
     - **Angle Change**: The angle by which the direction changes at each recursive step.
     - **Length**: The initial length of the lines drawn.
     - **Length Scaling Factor**: How the length of lines changes with each recursion.
     - **Recursion Depth**: The number of times the recursive function calls itself.
   - Allow customization of these parameters to enable exploration of different fractal patterns.
   - **Optional:** Incorporate random module to achieve greater visual complexity.


2. **Generate Distinct Outputs**

   - Use your script to produce at least **five distinctly different fractal patterns** by varying the parameters or the geometric rules.
   - Save each output as an image in the `images/` folder with descriptive filenames.

3. **Visualization**

   - Use appropriate visualization libraries (e.g., Matplotlib) to plot your fractal patterns.
   - Utilize Shapely's integration with Matplotlib for plotting geometric objects.
   - **Optional:** Enhance your visualizations with custom color schemes.
   - Consider line thickness, color gradients, or other visual effects to improve the aesthetic appeal.

4. **Explore Advanced Concepts**

   - **Extend to 3D Space**:
     - Modify your script to generate fractals in 3D using libraries such as `matplotlib` with `mpl_toolkits.mplot3d` or `plotly`.
     - Handle 3D coordinates manually or use appropriate interactive 3D visualization libraries.
   - **Modify Geometric Rules**:
     - Experiment with different geometric transformations beyond simple branching.
     - Incorporate randomness or use different geometric shapes.

5. **Documentation**

   - Write detailed pseudo-code explaining your recursive functions in `README.md` using a similar structure to the template provided in `TEMPLATE.md`.
   - Provide technical explanations of your algorithms.
   - Include a short report discussing the process and the mathematical principles behind the fractals you created.
   - Insert images of your generated fractals into the documentation.

---

## Getting Started

### Prerequisites

- **Python 3.x**
- **Shapely**
- **Matplotlib**
- **NumPy**

For 3D visualization or advanced features, you may also need:

- **mpl_toolkits.mplot3d** (comes with Matplotlib)
- **Plotly** (for interactive 3D plots)

## Repository Structure

```
Assignment2/
├── README.md
├── BRIEF.md
├── TEMPLATE.md
├── fractal_generator.py
├── images/
│   ├── fractal1.png
│   ├── fractal2.png
│   ├── fractal3.png
│   ├── fractal4.png
│   ├── fractal5.png
│   └── (Additional images)
```

- `BRIEF.md`: This file, containing an overview and instructions.
- `TEMPLATE.md`: Minimal documentation template for your project repository.
- `README.md`: Your pseudo-code, technical explanations, and short report.
- `code/`: Python script for fractal generation.
- `images/`: Directory to save your generated images.
- `docs/`: Additional documentation or resources.

---

## Instructions

1. **Clone the Repository**

   - Accept the assignment on GitHub Classroom and clone the repository to your local machine using GitHub Desktop or the command line.

2. **Set Up Your Environment**

   - Ensure all dependencies are installed.
   - Familiarize yourself with the repository structure.

3. **Implement the Geometric Recursive Script with Shapely**

   - Open `fractal_generator.py`.
   - **Define the Parameters** explicitly in your script:
     - **Starting Point** (`tuple`): The initial coordinate (e.g., `(0, 0)`).
     - **Initial Angle** (`float`): The starting orientation in degrees (e.g., `90` for upwards).
     - **Angle Change** (`float`): The angle by which the direction changes at each recursive step (e.g., `25` degrees).
     - **Length** (`float`): The initial length of the lines drawn.
     - **Length Scaling Factor** (`float`): The factor by which the line length decreases with each recursion (e.g., `0.7`).
     - **Recursion Depth** (`int`): The maximum depth of recursion.
   - **Implement the Recursive Function**:
     - Write a function that:
       - Draws a line segment from the current point in the current direction.
       - Updates the current position based on the length and angle.
       - Recursively calls itself to create branches.
     - Use geometric transformations to calculate new positions and orientations.
     - Use **Shapely** to create and manage line geometries.
   - **Visualization with Matplotlib**:
     - Use Matplotlib to plot the Shapely geometric objects.
     - Ensure the axes are properly set to display the fractal correctly.

4. **Customize Parameters**

   - Allow users to customize the parameters.
   - Provide examples of different parameter sets in your script or in separate configuration sections.
   - Encourage exploration by making it easy to adjust parameters.

5. **Generate and Save Outputs**

   - Run your script with different parameter sets to generate at least five distinct fractal patterns.
   - Save each output image in the `images/` folder with descriptive filenames (e.g., `tree_fractal.png`, `spiral_fractal.png`).

8. **Advanced Challenges (Optional for Extra Points)**

   - **Extending to 3D Space**:
     - Introduce a Z-coordinate and modify your function to handle 3D positions.
     - Use libraries like `mpl_toolkits.mplot3d` or `plotly` to visualize 3D fractals.
     - Handle rotations around multiple axes.
   - **Modify Geometric Rules**:
     - Incorporate randomness in angles or lengths using random module.
     - Use different geometric shapes, such as circles or polygons, at recursion steps.

9. **Documentation**

   - Write detailed pseudo-code explaining your recursive functions in `README.md`.
   - Introduce parameters, provide technical explanations and discuss the mathematical principles you employed.
   - Include images and explanations of each of your five fractal outputs.
   - Discuss any challenges faced and how you overcame them.

10. **Version Control with Git**

    - Make regular commits with meaningful messages.
    - Push your commits to the GitHub repository.

11. **Review and Finalize**

    - Ensure your code is well-commented and clean.
    - Verify that all generated images are saved in the correct folder.
    - Double-check your documentation for clarity and completeness.

---

## Advanced Challenges (Optional for Extra Points)

### Extending to 3D Space

- **Implement 3D Fractals**:
  - Introduce a Z-axis and modify your recursive function to handle 3D coordinates.
  - Adjust your geometric transformations to include rotations around the X, Y, and Z axes.
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
      return plt.cm.viridis(depth / max_depth)

  # Plot using the color
  color = get_color(current_depth, max_depth)
  ```

- **Color Gradients**:
  - Use color maps to apply gradients along the lines.
  - Consider using libraries like `matplotlib.colors` for advanced color manipulations.

### Modify Geometric Rules

- **Incorporate Randomness**:
  - Introduce randomness in angles or lengths to create more natural-looking patterns.
  - Example:

    ```python
    import random

    angle_change = random.uniform(20, 40)
    length_scaling = random.uniform(0.6, 0.8)
    ```

---

## Submission Guidelines

- **What to Submit**:
  - Your `fractal_generator.py` script and any additional scripts in the `code/` directory.
  - Completed `README.md` with pseudo-code, explanations, and short report.
  - Generated images saved in the `images/` folder.
  - Any additional documentation in the `docs/` folder.

- **Submission Checklist**:
  - [ ] Code runs without errors.
  - [ ] Code is well-commented and follows best practices (e.g. consistent naming conventions).
  - [ ] `README.md` is complete and thorough.
  - [ ] At least five distinct fractal images are saved and referenced in your documentation.
  - [ ] All changes are committed with meaningful messages.
  - [ ] All commits are pushed to your GitHub repository.

---

## Evaluation Criteria

- **Implementation of Recursive Functions**
  - Correct use of recursion in generating fractal patterns using geometric transformations with Shapely.
  - Ability to customize parameters and generate different outputs.

- **Technical Understanding**
  - Demonstrated understanding of recursion, functional programming, and geometric manipulations.
  - Clear explanations in code comments and documentation.

- **Code Quality**
  - Clean, readable, and well-organized code.
  - Use of meaningful variable names and proper formatting.

- **Documentation**
  - Detailed pseudo-code and technical explanations.
  - Short report discussing the process, parameters, and mathematical principles.
  - Inclusion and discussion of generated fractal images.

- **Use of Git and Version Control**
  - Regular commits with meaningful messages.
  - Proper repository structure and organization.

---

## Resources

- **Python Official Documentation**: [https://docs.python.org/3/](https://docs.python.org/3/)
- **Shapely Documentation**: [https://shapely.readthedocs.io](https://shapely.readthedocs.io)
- **Matplotlib Documentation**: [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)
- **NumPy Documentation**: [https://numpy.org/doc/](https://numpy.org/doc/)
- **Plotly Documentation**: [https://plotly.com/python/](https://plotly.com/python/)
- **L-Systems**: [https://en.wikipedia.org/wiki/L-system](https://en.wikipedia.org/wiki/L-system)

---

## Contact

If you have any questions or need assistance, please reach out to the instructor via email or the course forum.

---