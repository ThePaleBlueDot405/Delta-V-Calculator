import sys
import math
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDesktopWidget, QLineEdit
from PyQt5.QtCore import Qt
from decimal import Decimal

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delta V Calculator")
        self.setFixedSize(1000, 700)
        self.center_window()

        self.exuaste_velocity_input = QLineEdit(self)
        self.initial_mass_input = QLineEdit(self)
        self.final_mass_input = QLineEdit(self)
        self.specific_impulse_input = QLineEdit(self)
        self.initial_mass_input_2 = QLineEdit(self)
        self.final_mass_input_2 = QLineEdit(self)

        self.exauste_velocity_calculate_button = QPushButton("Calculate", self)
        self.specific_impulse_calculate_button = QPushButton("Calculate", self)
        self.intro_question_lab = QLabel("Which way you want to calculate the delta V", self)
        self.exauste_velocity_button = QPushButton("Exhaust velocity", self)
        self.specific_impulse_button = QPushButton("Specific impulse", self)
        self.exauste_velocity_answer_lab = QLabel(self)
        self.specific_impulse_answer_lab = QLabel(self)

        self.exauste_velocity_unit = QLabel("m/s", self)
        self.initial_mass_unit = QLabel("kg", self)
        self.final_mass_unit = QLabel("kg", self)
        self.specific_impulse_unit = QLabel("s", self)
        self.initial_mass_unit_2 = QLabel("kg", self)
        self.final_mass_unit_2 = QLabel("kg", self)

        self.exauste_velocity_button.clicked.connect(self.exauste_velocity_button_clicked)
        self.specific_impulse_button.clicked.connect(self.specific_impulse_button_clicked)
        self.exauste_velocity_calculate_button.clicked.connect(self.exhaust_velocity_calculate)
        self.specific_impulse_calculate_button.clicked.connect(self.specific_impulse_calculate)
        self.initUI()

    def center_window(self):
        window_geometry = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        window_geometry.moveCenter(screen_center)
        self.move(window_geometry.topLeft())

    def initUI(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: hsl(220, 25%, 12%);
            }
        """)

        self.intro_question_lab.setGeometry(
            (self.width() - 500) // 2,
            100,
            500,
            80
        )

        self.intro_question_lab.setStyleSheet("""
            color: white;
            background-color: hsl(316, 61%, 45%);
            font-size: 22px;
            font-family: Arial;
            font-weight: bold;
            padding: 10px;
            border: 2px solid #61dafb;
            border-radius: 10px;
        """)

        self.exauste_velocity_button.setGeometry(
            70,
            550,
            250,
            50
        )

        self.specific_impulse_button.setGeometry(
            680,
            550,
            250,
            50
        )

        self.exauste_velocity_button.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: hsl(252, 61%, 45%);
                font-size: 22px;
                font-family: Arial;
                font-weight: bold;
                padding: 10px;
                border: 2px solid #61dafb;
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: hsl(252, 61%, 55%);
                border: 2px solid white;
            }

            QPushButton:pressed {
                background-color: hsl(252, 61%, 35%);
            }
        """)

        self.specific_impulse_button.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: hsl(180, 61%, 45%);
                font-size: 22px;
                font-family: Arial;
                font-weight: bold;
                padding: 10px;
                border: 2px solid #61dafb;
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: hsl(180, 61%, 55%);
                border: 2px solid white;
            }

            QPushButton:pressed {
                background-color: hsl(180, 61%, 35%);
            }
        """)

        self.exuaste_velocity_input.setGeometry(300, 200, 400, 50)
        self.initial_mass_input.setGeometry(300, 280, 400, 50)
        self.final_mass_input.setGeometry(300, 360, 400, 50)
        self.exauste_velocity_calculate_button.setGeometry(400, 440, 200, 50)

        self.specific_impulse_input.setGeometry(300, 200, 400, 50)
        self.initial_mass_input_2.setGeometry(300, 280, 400, 50)
        self.final_mass_input_2.setGeometry(300, 360, 400, 50)
        self.specific_impulse_calculate_button.setGeometry(400, 440, 200, 50)

        self.exauste_velocity_unit.setGeometry(640, 200, 50, 50)
        self.initial_mass_unit.setGeometry(640, 280, 50, 50)
        self.final_mass_unit.setGeometry(640, 360, 50, 50)
        self.specific_impulse_unit.setGeometry(640, 200, 50, 50)
        self.initial_mass_unit_2.setGeometry(640, 280, 50, 50)
        self.final_mass_unit_2.setGeometry(640, 360, 50, 50)

        self.exuaste_velocity_input.setTextMargins(0, 0, 50, 0)
        self.initial_mass_input.setTextMargins(0, 0, 50, 0)
        self.final_mass_input.setTextMargins(0, 0, 50, 0)
        self.specific_impulse_input.setTextMargins(0, 0, 50, 0)
        self.initial_mass_input_2.setTextMargins(0, 0, 50, 0)
        self.final_mass_input_2.setTextMargins(0, 0, 50, 0)

        self.exuaste_velocity_input.setPlaceholderText("Exhaust velocity")
        self.initial_mass_input.setPlaceholderText("Initial mass")
        self.final_mass_input.setPlaceholderText("Final mass")
        self.specific_impulse_input.setPlaceholderText("Specific impulse")
        self.initial_mass_input_2.setPlaceholderText("Initial mass")
        self.final_mass_input_2.setPlaceholderText("Final mass")

        self.exauste_velocity_unit.setAlignment(Qt.AlignCenter)
        self.initial_mass_unit.setAlignment(Qt.AlignCenter)
        self.final_mass_unit.setAlignment(Qt.AlignCenter)
        self.specific_impulse_unit.setAlignment(Qt.AlignCenter)
        self.initial_mass_unit_2.setAlignment(Qt.AlignCenter)
        self.final_mass_unit_2.setAlignment(Qt.AlignCenter)

        self.exauste_velocity_unit.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.initial_mass_unit.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.final_mass_unit.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.specific_impulse_unit.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.initial_mass_unit_2.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.final_mass_unit_2.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.exauste_velocity_unit.setStyleSheet("""
            color: white;
            font-size: 18px;
            font-family: Arial;
        """)

        self.initial_mass_unit.setStyleSheet("""
            color: white;
            font-size: 18px;
            font-family: Arial;
        """)

        self.final_mass_unit.setStyleSheet("""
            color: white;
            font-size: 18px;
            font-family: Arial;
        """)

        self.specific_impulse_unit.setStyleSheet("""
            color: white;
            font-size: 18px;
            font-family: Arial;
        """)

        self.initial_mass_unit_2.setStyleSheet("""
            color: white;
            font-size: 18px;
            font-family: Arial;
        """)

        self.final_mass_unit_2.setStyleSheet("""
            color: white;
            font-size: 18px;
            font-family: Arial;
        """)

        self.exuaste_velocity_input.setStyleSheet("""
            QLineEdit {
                color: white;
                background-color: hsl(252, 25%, 20%);
                font-size: 20px;
                font-family: Arial;
                padding: 10px;
                border: 2px solid hsl(252, 61%, 45%);
                border-radius: 10px;
            }

            QLineEdit:hover {
                border: 2px solid #61dafb;
            }

            QLineEdit:focus {
                border: 2px solid hsl(252, 61%, 65%);
                background-color: hsl(252, 25%, 23%);
            }
        """)

        self.initial_mass_input.setStyleSheet("""
            QLineEdit {
                color: white;
                background-color: hsl(252, 25%, 20%);
                font-size: 20px;
                font-family: Arial;
                padding: 10px;
                border: 2px solid hsl(252, 61%, 45%);
                border-radius: 10px;
            }

            QLineEdit:hover {
                border: 2px solid #61dafb;
            }

            QLineEdit:focus {
                border: 2px solid hsl(252, 61%, 65%);
                background-color: hsl(252, 25%, 23%);
            }
        """)

        self.final_mass_input.setStyleSheet("""
            QLineEdit {
                color: white;
                background-color: hsl(252, 25%, 20%);
                font-size: 20px;
                font-family: Arial;
                padding: 10px;
                border: 2px solid hsl(252, 61%, 45%);
                border-radius: 10px;
            }

            QLineEdit:hover {
                border: 2px solid #61dafb;
            }

            QLineEdit:focus {
                border: 2px solid hsl(252, 61%, 65%);
                background-color: hsl(252, 25%, 23%);
            }
        """)

        self.specific_impulse_input.setStyleSheet("""
            QLineEdit {
                color: white;
                background-color: hsl(180, 25%, 20%);
                font-size: 20px;
                font-family: Arial;
                padding: 10px;
                border: 2px solid hsl(180, 61%, 45%);
                border-radius: 10px;
            }

            QLineEdit:hover {
                border: 2px solid #61dafb;
            }

            QLineEdit:focus {
                border: 2px solid hsl(180, 61%, 65%);
                background-color: hsl(180, 25%, 23%);
            }
        """)

        self.initial_mass_input_2.setStyleSheet("""
            QLineEdit {
                color: white;
                background-color: hsl(180, 25%, 20%);
                font-size: 20px;
                font-family: Arial;
                padding: 10px;
                border: 2px solid hsl(180, 61%, 45%);
                border-radius: 10px;
            }

            QLineEdit:hover {
                border: 2px solid #61dafb;
            }

            QLineEdit:focus {
                border: 2px solid hsl(180, 61%, 65%);
                background-color: hsl(180, 25%, 23%);
            }
        """)

        self.final_mass_input_2.setStyleSheet("""
            QLineEdit {
                color: white;
                background-color: hsl(180, 25%, 20%);
                font-size: 20px;
                font-family: Arial;
                padding: 10px;
                border: 2px solid hsl(180, 61%, 45%);
                border-radius: 10px;
            }

            QLineEdit:hover {
                border: 2px solid #61dafb;
            }

            QLineEdit:focus {
                border: 2px solid hsl(180, 61%, 65%);
                background-color: hsl(180, 25%, 23%);
            }
        """)

        self.exauste_velocity_calculate_button.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: hsl(252, 61%, 45%);
                font-size: 20px;
                font-family: Arial;
                font-weight: bold;
                padding: 10px;
                border: 2px solid #61dafb;
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: hsl(252, 61%, 55%);
                border: 2px solid white;
            }

            QPushButton:pressed {
                background-color: hsl(252, 61%, 35%);
            }
        """)

        self.specific_impulse_calculate_button.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: hsl(180, 61%, 45%);
                font-size: 20px;
                font-family: Arial;
                font-weight: bold;
                padding: 10px;
                border: 2px solid #61dafb;
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: hsl(180, 61%, 55%);
                border: 2px solid white;
            }

            QPushButton:pressed {
                background-color: hsl(180, 61%, 35%);
            }
        """)

        self.exauste_velocity_answer_lab.setGeometry(
            280,
            520,
            450,
            60
        )

        self.specific_impulse_answer_lab.setGeometry(
            280,
            520,
            450,
            60
        )

        self.exauste_velocity_answer_lab.setStyleSheet("""
            color: white;
            background-color: hsl(252, 61%, 45%);
            font-size: 22px;
            font-family: Arial;
            font-weight: bold;
            padding: 10px;
            border: 2px solid #61dafb;
            border-radius: 10px;
        """)

        self.specific_impulse_answer_lab.setStyleSheet("""
            color: white;
            background-color: hsl(180, 61%, 45%);
            font-size: 22px;
            font-family: Arial;
            font-weight: bold;
            padding: 10px;
            border: 2px solid #61dafb;
            border-radius: 10px;
        """)

        self.exauste_velocity_answer_lab.hide()
        self.specific_impulse_answer_lab.hide()
        self.exuaste_velocity_input.hide()
        self.initial_mass_input.hide()
        self.final_mass_input.hide()
        self.exauste_velocity_calculate_button.hide()
        self.exauste_velocity_unit.hide()
        self.initial_mass_unit.hide()
        self.final_mass_unit.hide()
        self.specific_impulse_input.hide()
        self.initial_mass_input_2.hide()
        self.final_mass_input_2.hide()
        self.specific_impulse_calculate_button.hide()
        self.specific_impulse_unit.hide()
        self.initial_mass_unit_2.hide()
        self.final_mass_unit_2.hide()

    def exauste_velocity_button_clicked(self):
        self.intro_question_lab.hide()
        self.exauste_velocity_button.hide()
        self.specific_impulse_button.hide()
        self.exuaste_velocity_input.show()
        self.initial_mass_input.show()
        self.final_mass_input.show()
        self.exauste_velocity_calculate_button.show()
        self.exauste_velocity_unit.show()
        self.initial_mass_unit.show()
        self.final_mass_unit.show()

    def specific_impulse_button_clicked(self):
        self.intro_question_lab.hide()
        self.exauste_velocity_button.hide()
        self.specific_impulse_button.hide()
        self.specific_impulse_input.show()
        self.initial_mass_input_2.show()
        self.final_mass_input_2.show()
        self.specific_impulse_calculate_button.show()
        self.specific_impulse_unit.show()
        self.initial_mass_unit_2.show()
        self.final_mass_unit_2.show()

    def exhaust_velocity_calculate(self):
        exhaust_velocity = Decimal(self.exuaste_velocity_input.text())
        initial_mass = Decimal(self.initial_mass_input.text())
        final_mass = Decimal(self.final_mass_input.text())

        if exhaust_velocity <= 0 or initial_mass <= 0 or final_mass <= 0:
            raise ValueError("Values must be greater than zero")

        if initial_mass <= final_mass:
            raise ValueError("Initial mass must be greater than final mass")

        delta_v = exhaust_velocity * (initial_mass / final_mass).ln()
        self.exauste_velocity_answer_lab.setText(str(delta_v) + " m/s")
        self.exauste_velocity_answer_lab.show()

    def specific_impulse_calculate(self):
        specific_impulse = Decimal(self.specific_impulse_input.text())
        initial_mass = Decimal(self.initial_mass_input_2.text())
        final_mass = Decimal(self.final_mass_input_2.text())

        if specific_impulse <= 0 or initial_mass <= 0 or final_mass <= 0:
            raise ValueError("Values must be greater than zero")

        if initial_mass <= final_mass:
            raise ValueError("Initial mass must be greater than final mass")

        exhaust_velocity = specific_impulse * Decimal("9.80665")
        delta_v = exhaust_velocity * (initial_mass / final_mass).ln()
        self.specific_impulse_answer_lab.setText(str(delta_v) + " m/s")
        self.specific_impulse_answer_lab.show()


def main():
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()