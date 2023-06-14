import sys
from datetime import datetime

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton

class AgeCalculator(QWidget):  #inherit from qwidget, because it creates windows
    def __init__(self):
        super().__init__()   #returns parent of a class being called
        self.setWindowTitle('Age Calculator')
        grid = QGridLayout()

        #creates widgets
        name_label = QLabel('Name:')
        name_line_edit = QLineEdit()

        date_birth_label = QLabel('D.O.B:')
        self.date_birth_line_edit = QLineEdit()

        calculate_button = QPushButton('Calculate Age')
        calculate_button.clicked.connect(self.calculate_age)
       # calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel('')


        #add widgets to grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(name_line_edit, 0, 1)
        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        #add grid to class instance
        self.setLayout(grid)


    def calculate_age(self):
        current_year = datetime.now().year
        birth_year = self.date_birth_line_edit.text()
        year_birth = datetime.strptime(birth_year, "%m/%d/%Y").date().year

        age = current_year - year_birth
        self.output_label.setText(str(age))



app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())

