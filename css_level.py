from PyQt6.QtWidgets import QLabel, QWidget, QGridLayout, QMainWindow, QApplication, QTextEdit, QPushButton
from PyQt6 import QtCore

import ProgrammingTycoon


class CSS(ProgrammingTycoon):
    def __init__(self):
        super.__init__()

    def create_CSS_button(self):
        self.CSS_button = QPushButton()
        self.CSS_button.setText("HTML")
        self.CSS_button.setMaximumSize(QtCore.QSize(100, 50))
        self.CSS_button.clicked.connect(lambda: self.HTML_button_handler())
        return self.HTML_button

