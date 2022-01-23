from PyQt6.QtWidgets import QLabel, QWidget, QGridLayout, QMainWindow, QApplication, QTextEdit, QPushButton
from PyQt6 import QtCore

import ParametersReader
import sys
import threading
import time


class ProgrammingTycoon(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.main_widget = QWidget()
        self.layout = QGridLayout()
        self.money_count = 1000.0000
        # HTML data
        self.HTML_data = ParametersReader.ParametersReader("HTML").get_data()
        self.HTML_value = float(self.HTML_data["value_per_step"])
        self.HTML_multiplier = float(self.HTML_data["multiplier"])
        self.HTML_level_up_cost = float(self.HTML_data["level_up_cost"])
        self.HTML_level_up_multiplier = float(self.HTML_data["level_up_cost_multiplier"])
        self.HTML_manager_cost = float(self.HTML_data["manager_cost"])
        self.HTML_manager_active = False
        self.HTML_level = 1

    def launch_app(self):
        self.init_graphics()
        self.run_app()

    def init_graphics(self):
        self.layout.addWidget(self.create_money_text_box(), 0, 0, 0, 3)
        self.layout.addWidget(self.create_HTML_button(), 1, 1, 1, 1)
        self.layout.addWidget(self.HTML_level_up_button(), 1, 2, 1, 1)
        self.layout.addWidget(self.HTML_next_level_label(), 1, 3, 1, 1)
        self.layout.addWidget(self.HTML_click_manager(), 1, 0, 1, 1)

        self.main_widget.setLayout(self.layout)
        self.main_widget.setWindowTitle('Programming Tycoon')
        self.main_widget.setMinimumSize(QtCore.QSize(500, 350))
        self.main_widget.show()

    def create_money_text_box(self):
        self.money_display = QLabel(f'Bani: {round(self.money_count, 5)}$ -> {self.HTML_value * self.HTML_multiplier}/s')
        return self.money_display

    def set_money_text_box(self, text):
        self.money_display.setText(text)

    def run_app(self):
        self.app.exec()

    def create_HTML_button(self):
        self.HTML_button = QPushButton()
        self.HTML_button.setText("HTML")
        self.HTML_button.setMaximumSize(QtCore.QSize(100, 50))
        self.HTML_button.clicked.connect(lambda: self.HTML_button_handler())
        return self.HTML_button

    def HTML_button_handler(self):
        self.money_count += self.HTML_value * self.HTML_multiplier
        self.HTML_check_level_update()
        self.set_money_text_box(f'Bani: {round(self.money_count, 5)}$ -> {self.HTML_value * self.HTML_multiplier}/s')
        self.HTML_set_next_level_label(f'Nivelul {self.HTML_level + 1} costa {str(self.HTML_level_up_cost)} $')

    def HTML_level_label(self):
        self.HTML_lvl_label = QLabel(str(self.HTML_level))
        return self.HTML_lvl_label

    def HTML_level_up_button(self):
        self.HTML_lvl_up_btn = QPushButton()
        self.HTML_lvl_up_btn.setText("Level Up")
        self.HTML_lvl_up_btn.setMaximumSize(QtCore.QSize(100, 50))
        self.HTML_lvl_up_btn.clicked.connect(lambda: self.HTML_level_UP_handler())
        self.HTML_check_level_update()
        return self.HTML_lvl_up_btn

    def HTML_level_UP_handler(self):
        if self.money_count > self.HTML_level_up_cost:
            print(self.HTML_level)
            self.money_count -= self.HTML_level_up_cost
            self.set_money_text_box(f'Bani: {round(self.money_count, 5)}$ -> {self.HTML_value * self.HTML_multiplier}/s')
            self.HTML_level_up_cost *= self.HTML_level_up_multiplier
            self.HTML_multiplier += self.HTML_multiplier
            self.HTML_level += 1
            self.HTML_set_next_level_label(f'Nivelul {self.HTML_level + 1} costa {str(self.HTML_level_up_cost)} $')
            self.HTML_check_level_update()
        else:
            money_diff = round(self.HTML_level_up_cost-self.money_count, 5)
            self.HTML_set_next_level_label(f"Mai ai nevoie de {money_diff} $ !")

    def HTML_check_level_update(self):
        if self.money_count > self.HTML_level_up_cost:
            self.HTML_lvl_up_btn.setStyleSheet("background-color: green")
        else:

            self.HTML_lvl_up_btn.setStyleSheet("background-color: red")

    def HTML_next_level_label(self):
        self.next_level_label_text = QLabel(f'Nivelul {self.HTML_level + 1} costa {str(self.HTML_level_up_cost)} $')
        return self.next_level_label_text

    def HTML_set_next_level_label(self, text):
        self.next_level_label_text.setText(text)

    def HTML_click_manager(self):
        self.manager_button = QPushButton()
        self.manager_button.setText("Manager")
        self.manager_button.setMaximumSize(QtCore.QSize(100, 50))
        self.manager_button.clicked.connect(lambda: self.HTML_manager_handler())
        return self.manager_button

    def HTML_manager_handler(self):
        if not self.HTML_manager_active:
            if self.money_count > self.HTML_manager_cost:
                self.HTML_manager_active = True
                self.money_count -= self.HTML_manager_cost
                self.set_money_text_box(f'Bani: {round(self.money_count, 5)}$ -> '
                                        f'{self.HTML_value * self.HTML_multiplier}/s')
                self.manager_button.setStyleSheet("background-color: green")
                HTML_click_thread = threading.Thread(target=self.HTML_clicker)
                HTML_click_thread.start()
        else:
            self.HTML_set_next_level_label("Managerul este deja activ!")

    def HTML_clicker(self):
        while True:
            self.HTML_button_handler()
            time.sleep(0.5)
