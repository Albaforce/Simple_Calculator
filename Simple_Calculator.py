import math
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                            QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QComboBox, QStackedWidget)

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.first_number = None
        self.operation = None
        self.firstP = ""
        self.prefix_operator = None
        
        
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        
        
        main_widget.setStyleSheet("""
            QWidget {
                background-color: #333333;
            }
        """)
        
        
        self.combo = QComboBox()
        self.combo.addItems(["Standard", "Scientific"])
        self.combo.setStyleSheet("""
            QComboBox {
                padding: 5px;
                border: 1px solid #BBB;
                border-radius: 3px;
                margin-bottom: 10px;
                background-color: white;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)
        main_layout.addWidget(self.combo)
        
        
        self.stack = QStackedWidget()
        main_layout.addWidget(self.stack)
        
        
        self.standard_page = QWidget()
        self.setupStandardCalculator()
        self.stack.addWidget(self.standard_page)
        
        
        self.scientific_page = QWidget()
        self.setupScientificCalculator()
        self.stack.addWidget(self.scientific_page)
        
        
        self.combo.currentIndexChanged.connect(self.stack.setCurrentIndex)

    def setupStandardCalculator(self):
        layout = QVBoxLayout(self.standard_page)
        
       
        self.display = QLineEdit()
        self.display.setStyleSheet("""
            QLineEdit {
                min-height: 30px;
                font-size: 16px;
                padding: 5px;
                background: white; 
                border: 1px solid #89CFF0;
                border-radius: 15px;
            }
        """)
        layout.addWidget(self.display)
        
        
        grid = QGridLayout()
        
        
        calc = [
            [
                {'text': '7', 'func': self.num7},
                {'text': '8', 'func': self.num8},
                {'text': '9', 'func': self.num9},
                {'text': 'x', 'func': self.multiply}
            ],
            [
                {'text': '4', 'func': self.num4},
                {'text': '5', 'func': self.num5},
                {'text': '6', 'func': self.num6},
                {'text': '÷', 'func': self.divide}
            ],
            [
                {'text': '1', 'func': self.num1},
                {'text': '2', 'func': self.num2},
                {'text': '3', 'func': self.num3},
                {'text': '+', 'func': self.add}
            ],
            [
                {'text': 'clear', 'func': self.clear},
                {'text': '0', 'func': self.num0},
                {'text': '=', 'func': self.equals},
                {'text': '-', 'func': self.subtract}
            ]
        ]
        
        self.createButtons(grid, calc)
        layout.addLayout(grid)

    def setupScientificCalculator(self):
        layout = QVBoxLayout(self.scientific_page)
        
        
        self.display2 = QLineEdit()
        self.display2.setStyleSheet("""
            QLineEdit {
                min-height: 30px;
                font-size: 16px;
                padding: 5px;
                background: white; 
                border: 1px solid #89CFF0;
                border-radius: 15px;
            }
        """)
        layout.addWidget(self.display2)
        
        
        grid = QGridLayout()
        
        
        calc = [
            [
                {'text': '^', 'func': self.power},
                {'text': '√', 'func': self.prefix_square_root},
                {'text': 'sin', 'func': self.prefix_sin},
                {'text': 'cos', 'func': self.prefix_cos}
            ],
            [
                {'text': '7', 'func': self.num7},
                {'text': '8', 'func': self.num8},
                {'text': '9', 'func': self.num9},
                {'text': 'x', 'func': self.multiply}
            ],
            [
                {'text': '4', 'func': self.num4},
                {'text': '5', 'func': self.num5},
                {'text': '6', 'func': self.num6},
                {'text': '÷', 'func': self.divide}
            ],
            [
                {'text': '1', 'func': self.num1},
                {'text': '2', 'func': self.num2},
                {'text': '3', 'func': self.num3},
                {'text': '+', 'func': self.add}
            ],
            [
                {'text': 'clear', 'func': self.clear},
                {'text': '0', 'func': self.num0},
                {'text': '=', 'func': self.equals},
                {'text': '-', 'func': self.subtract}
            ]
        ]
        
        self.createButtons(grid, calc)
        layout.addLayout(grid)

    def createButtons(self, grid, calc):
        for row, rowV in enumerate(calc):
            for col, colV in enumerate(rowV):
                button = QPushButton(colV['text'])
                if colV['text'] in ['x', '÷', '+', '-', '=', '^', '√', 'sin', 'cos']:
                    button.setStyleSheet("""
                        QPushButton {
                            min-width: 50px;
                            min-height: 50px;
                            font-size: 16px;
                            background-color: #318CE7;
                            color: white;
                            border-radius: 25px;
                        }
                        QPushButton:hover {
                            background-color: #89CFF0;
                        }
                    """)
                else:
                    button.setStyleSheet("""
                        QPushButton {
                            min-width: 50px;
                            min-height: 50px;
                            font-size: 16px;
                            background-color: #E0E0E0;
                            border-radius: 25px;
                        }
                        QPushButton:hover {
                            background-color: #BDBDBD;
                        }
                    """)
                button.clicked.connect(colV['func'])
                grid.addWidget(button, row, col)
        grid.setSpacing(5)

    def getCurrentDisplay(self):
        return self.display if self.stack.currentIndex() == 0 else self.display2

   
    def num0(self): self.append_number("0")
    def num1(self): self.append_number("1")
    def num2(self): self.append_number("2")
    def num3(self): self.append_number("3")
    def num4(self): self.append_number("4")
    def num5(self): self.append_number("5")
    def num6(self): self.append_number("6")
    def num7(self): self.append_number("7")
    def num8(self): self.append_number("8")
    def num9(self): self.append_number("9")
   
    def append_number(self, number):
        display = self.getCurrentDisplay()
        current = display.text()
        if self.prefix_operation:
            display.setText(current + number)
            self.calculatePrefix()
        else:
            display.setText(current + number)

    def prefix_square_root(self):
        display = self.getCurrentDisplay()
        self.prefix_operation = "√"
        display.setText("√")

    def prefix_sin(self):
        display = self.getCurrentDisplay()
        self.prefix_operation = "sin"
        display.setText("sin")

    def prefix_cos(self):
        display = self.getCurrentDisplay()
        self.prefix_operation = "cos"
        display.setText("cos")

    def calculatePrefix(self):
        display = self.getCurrentDisplay()
        try:
            text = display.text()
            if self.prefix_operation == "√":
                number = float(text[1:])  
                result = math.sqrt(number)
            elif self.prefix_operation == "sin":
                number = float(text[3:])  
                result = math.sin(math.radians(number))
            elif self.prefix_operation == "cos":
                number = float(text[3:])  
                result = math.cos(math.radians(number))
            
           
            if isinstance(result, complex):
                display.setText("Error")
            elif result.is_integer():
                display.setText(str(int(result)))
            else:
                display.setText(f"{result:.2f}")
            
            
            self.prefix_operation = None
            
        except:
            display.setText("Error")
            self.prefix_operation = None


    def add(self): self.store_first_number("+")
    def subtract(self): self.store_first_number("-")
    def multiply(self): self.store_first_number("x")
    def divide(self): self.store_first_number("÷")
    def power(self): self.store_first_number("^")


    def store_first_number(self, operation):
        try:
            display = self.getCurrentDisplay()
            self.first_number = float(display.text())
            self.operation = operation
            current = display.text()
            self.firstP = current
            display.setText(current + operation)
        except ValueError:
            display.setText("Error")

    def equals(self):
        try:
            display = self.getCurrentDisplay()
            second_number = display.text()[len(self.firstP)+1:]
            
            if self.operation in ["sin", "cos", "√"]:
                second_number = "0"
            
            second_number = float(second_number)
            
            if self.operation == "+":
                result = self.first_number + second_number
            elif self.operation == "-":
                result = self.first_number - second_number
            elif self.operation == "x":
                result = self.first_number * second_number
            elif self.operation == "÷":
                if second_number == 0:
                    display.setText("Error")
                    return
                result = self.first_number / second_number
            elif self.operation == "^":
                result = self.first_number ** second_number
            elif self.operation == "√":
                result = math.sqrt(self.first_number)
            elif self.operation == "sin":
                result = math.sin(math.radians(self.first_number))
            elif self.operation == "cos":
                result = math.cos(math.radians(self.first_number))
            else:
                return

            
            if isinstance(result, complex):
                display.setText("Error")
            elif result.is_integer():
                display.setText(str(int(result)))
            else:
                display.setText(f"{result:.2f}")

        except:
            display.setText("Error")

    def clear(self):
        display = self.getCurrentDisplay()
        display.setText("")
        self.first_number = None
        self.operation = None
        self.firstP = ""

def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()