import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# 커스텀 윈도우


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("My First App")
        self.setMinimumSize(QSize(500, 800))

        # 버튼 생성
        button = QPushButton("Press Me")
        button.setCheckable(True)
        button.clicked.connect(self.clickHandler)

        # 윈도우 중앙에 위치할 Widget 설정
        self.setCentralWidget(button)

    def clickHandler(self):
        print('클릭')


app = QApplication(sys.argv)
# window = QMainWindow() 기본 윈도우
window = MainWindow()
window.show()
app.exec_()
