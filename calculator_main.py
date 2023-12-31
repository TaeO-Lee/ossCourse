import sys
from PyQt5.QtWidgets import *


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_button_grid = QGridLayout()
        layout_equation_solution = QFormLayout()

        # 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        label_equation = QLabel("")
        self.equation = QLineEdit("")

        # layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addRow(label_equation, self.equation)

        # 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")
        
        # =, ce, c, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_CE = QPushButton("CE")
        button_C = QPushButton("C")
        button_backspace = QPushButton("Backspace")
        
        # %, 1/x, x^2, 제곱근 버튼 생성
        button_modula = QPushButton("%")
        button_reciprocal = QPushButton("1/x")
        button_multiple = QPushButton("x^2")
        button_root = QPushButton("Root")

        # 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(
            lambda state, operation="+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(
            lambda state, operation="-": self.button_operation_clicked(operation))
        button_product.clicked.connect(
            lambda state, operation="*": self.button_operation_clicked(operation))
        button_division.clicked.connect(
            lambda state, operation="/": self.button_operation_clicked(operation))
        button_modula.clicked.connect(
            lambda state, operation="%": self.button_operation_clicked(operation))
        # 연산 버튼을 layout_button_grid 레이아웃에 추가
        layout_button_grid.addWidget(button_product, 2, 3)
        layout_button_grid.addWidget(button_minus, 3, 3)
        layout_button_grid.addWidget(button_plus, 4, 3)
        layout_button_grid.addWidget(button_equal, 5, 3)
        layout_button_grid.addWidget(button_division, 1,3)
        layout_button_grid.addWidget(button_backspace, 0, 3)
        layout_button_grid.addWidget(button_C, 0,2)
        layout_button_grid.addWidget(button_root, 1, 2)
        layout_button_grid.addWidget(button_CE, 0, 1)
        layout_button_grid.addWidget(button_multiple, 1,1)
        layout_button_grid.addWidget(button_modula, 0, 0)
        layout_button_grid.addWidget(button_reciprocal, 1, 0)

        # =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_CE.clicked.connect(self.button_clear_clicked)
        button_C.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)
        
        # %, 1/x, x^2, 제곱근 버튼 클릭 시 시그널 설정
        button_reciprocal.clicked.connect(self.button_reciprocal_clicked)
        button_multiple.clicked.connect(self.button_multiple_clicked)
        button_root.clicked.connect(self.button_root_clicked)

        # 숫자 버튼 생성하고, layout_button_grid 레이아웃에 추가
        # 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num=number:
                                                       self.number_button_clicked(num))
            if number > 0:
                y = (number-1) % 3
                x = 4 - (number - 1) // 3 
                layout_button_grid.addWidget(
                    number_button_dict[number], x, y)
            elif number == 0:
                layout_button_grid.addWidget(number_button_dict[number], 5, 1)

        # 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(
            lambda state, num=".": self.number_button_clicked(num))
        layout_button_grid.addWidget(button_dot, 5, 2)

        button_turn = QPushButton("+/-")
        button_turn.clicked.connect(self.button_turn_clicked)
        layout_button_grid.addWidget(button_turn, 5, 0)

        # 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_button_grid)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        
    
        equation += str(num)
        self.equation.setText(equation)
        

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation.text()
        solution = eval(equation)
        self.equation.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)
    
    def button_turn_clicked(self):
        equation = self.equation.text()
        
        if equation:
            current_number = float(equation)
            new_number = current_number * -1
            self.equation.setText(str(new_number))

    def button_reciprocal_clicked(self):
        equation = self.equation.text()
        if equation:
            current_number = float(equation)
            new_number = 1/current_number
            self.equation.setText(str(new_number))

    def button_multiple_clicked(self):
        equation = self.equation.text()
        if equation:
            current_number = float(equation)
            new_number = current_number ** 2
            self.equation.setText(str(new_number))

    def button_root_clicked(self):
        equation = self.equation.text()
        if equation:
            current_number = float(equation)
            new_number = current_number ** (1/2)
            self.equation.setText(str(new_number))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())