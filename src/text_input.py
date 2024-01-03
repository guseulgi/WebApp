import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QToolButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # Label
        self.label = QLabel()

        # Input 필드
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        self.button = QToolButton()
        self.button.clicked.connect(self.input.clear)  # Label의 내용을 지우는 버튼

        # Vertical 수직 박스 레이아웃
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # 위젯의 레이아웃 지정
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
