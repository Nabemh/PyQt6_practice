from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Window")
        self.setWindowIcon(QIcon("database-storage.png"))
        #self.setFixedHeight(800)
        #self.setFixedWidth(900)
             
        #this will take x and y coordinates
        self.setGeometry(500, 300, 400, 300)
        stylesheet = (
            'background-color:skyblue'

        )
        self.setStyleSheet(stylesheet)


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())