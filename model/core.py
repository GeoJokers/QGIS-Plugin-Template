# -*- coding: utf-8 -*-
"""
Core functions
"""

from pathlib import Path

from qgis.core import QgsProject

import processing  # type: ignore reportMissingImports


PATH_DATA = Path(__file__).parent.parent.joinpath("data")
PATH_QML = Path(__file__).parent.parent.joinpath("styles")


def run_algorithm(input_layer):
    """Start processing."""

    # Process the data
    result = processing.run("native:buffer", {
        "INPUT": input_layer,
        "DISTANCE": 1.5,
        "SEGMENTS": 5,
        "END_CAP_STYLE": 0,
        "JOIN_STYLE": 0,
        "MITER_LIMIT": 2,
        "DISSOLVE": False,
        "OUTPUT": "memory:"
    })
    output_layer = result["OUTPUT"]

    # Add the result to the project
    QgsProject.instance().addMapLayer(output_layer)
