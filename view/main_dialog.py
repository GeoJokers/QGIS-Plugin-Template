# -*- coding: utf-8 -*-
"""
MainDialog
"""

from pathlib import Path

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

from ..model.core import run_algorithm


# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(Path(__file__).parent.joinpath("main_dialog.ui"))


class MainDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, iface, plugin_name, parent=None):
        """Constructor."""
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.iface = iface

        # Set the window title
        self.setWindowTitle(plugin_name)

        # Connect button actions
        self.button_start.clicked.connect(self.start)

    def start(self):
        """Clicked start button."""
        # Get the input layer
        self.input_layer = self.combo_input_layer.currentText()

        # Run the algorithm
        run_algorithm(self.input_layer)
