"""Assignment 2: Recursive Spatial Systems with Shapely.

This is a function scaffold, not a completed recursive generator.
TODO: design the baseline, stopping and branching rules in generate_fractal(),
then implement two spatial influences in growth_rule() and/or accept_segment().
Setup, endpoint calculation, seeded run creation and drawing are supplied.

Coordinates are planar (x, y), headings are degrees counterclockwise from +x,
and depth counts upward: max_depth=0 includes the root segment.
Each record contains a Shapely LineString and its recursion depth.
"""

from pathlib import Path
import json
import math
import random

import matplotlib.pyplot as plt
from shapely.affinity import rotate, translate
from shapely.geometry import LineString, Point


def growth_rule(start_point, angle, length, depth, params, scene):
    """Return (angle, length) after reading the local environment.

    Inputs: start_point (XY), angle (degrees), length (units), depth (integer),
    params (your settings) and scene (your named Shapely reference geometries).
    Return: two finite numbers. If unused, return (angle, length) unchanged.

    TODO: Choose a spatial query and how its result changes growth.
    You may implement either or both influences here or use accept_segment().
    """
    raise NotImplementedError("TODO: return the heading and length after your spatial response.")


def accept_segment(candidate, depth, params, scene):
    """Return True to keep this candidate segment.

    Inputs: candidate (LineString), depth (integer), params (your settings)
    and scene (your named Shapely reference geometries).
    Return: a Boolean. If unused, explicitly return True.

    TODO: Decide whether a spatial rule should accept or reject the candidate.
    Explain what rejection means for subsequent growth in your generator.
    """
    raise NotImplementedError("TODO: return whether the candidate is accepted.")


def endpoint(start_point, angle, length):
    """Return an XY tuple using Shapely rotation and translation (degrees)."""
    step = rotate(Point(length, 0), angle, origin=(0, 0))
    return translate(step, xoff=start_point[0], yoff=start_point[1]).coords[0]


def generate_fractal(start_point, angle, length, depth, params, scene, rng):
    """Return a NEW list of generated segment/depth records.

    Inputs
    ------
    start_point : XY coordinate tuple
    angle : heading in degrees counterclockwise from +x
    length : current nominal segment length
    depth : current level, starting at 0; max_depth is inclusive
    params : settings dictionary, including your rule/influence controls
    scene : dictionary of reference Shapely geometry
    rng : local random.Random instance, shared within this run

    Return
    ------
    list of dicts: {"geometry": a Shapely LineString, "depth": an integer}
    Return [] when this call produces no accepted geometry.

    TODO: Design your baseline, stopping conditions, branching and state transfer.
    Connect two distinguishable spatial influences with independent on/off controls.
    Do not draw here or use a shared global output list.
    """
    raise NotImplementedError("TODO: implement your baseline, stopping and branching rules.")


def build_design(params, scene):
    """Start a fresh reproducible run; importing this file does not run it."""
    if type(params["max_depth"]) is not int or not 0 <= params["max_depth"] <= 10:
        raise ValueError("Use integer max_depth from 0 to 10 (start small).")
    if not all(math.isfinite(params[key]) for key in ("angle", "length")):
        raise ValueError("Initial angle and length must be finite.")
    if len(params["start_point"]) != 2 or not all(
            math.isfinite(value) for value in params["start_point"]):
        raise ValueError("start_point must contain two finite coordinates.")
    if params["length"] <= 0:
        raise ValueError("Use a positive initial length.")
    rng = random.Random(params["seed"])
    return generate_fractal(params["start_point"], params["angle"],
                            params["length"], 0, params, scene, rng)


def draw_result(ax, records, scene):
    """Draw segment records on ax; scene holds your references. Return None."""
    # TODO: Map appearance to a meaningful signal and explain the mapping.
    for record in records:
        x, y = record["geometry"].xy
        ax.plot(x, y, color="#244b43", linewidth=1)

    # TODO: Draw your chosen reference geometries here if useful for interpretation.
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")


def main():
    params = {
        "start_point": (0.0, 0.0),
        "angle": 90.0,
        "length": 40.0,
        "max_depth": 5,
        "seed": 26,
        "influence_a_on": False,
        "influence_b_on": False,
        # TODO: Add your generation rules and bounded-randomness settings.
    }
    scene = {}  # TODO: Choose and name the Shapely geometries your influences read.
    try:
        records = build_design(params, scene)
    except NotImplementedError as error:
        print(error)
        print("Complete the generating TODOs before exporting the four study cases.")
        return None
    fig, ax = plt.subplots(figsize=(6, 6))
    draw_result(ax, records, scene)
    output_dir = Path(__file__).resolve().parent / "images"
    output_dir.mkdir(exist_ok=True)
    # These paths are overwritten on each run. Change both filenames per case,
    # or rename the exported PNG/JSON pair before running the next comparison.
    fig.savefig(output_dir / "starter_tree.png", dpi=180,
                bbox_inches="tight", pad_inches=0.1)
    metadata = {
        "parameters": params,
        "scene_wkt": {name: geometry.wkt for name, geometry in scene.items()},
        "segments": len(records),
        "status": "Record your implemented recursive rules and the active influences for this output.",
    }
    (output_dir / "starter_tree.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(metadata)
    plt.show()
    plt.close(fig)


if __name__ == "__main__":
    main()
