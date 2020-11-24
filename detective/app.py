from PySide2.QtWidgets import *

from .components import TheMenuBar
from .models import Workspace
from .views import MainView


class TheMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Detective")
        self.resize(1280, 720)
        self.setMenuBar(TheMenuBar())

        main_view = MainView()
        self.setCentralWidget(main_view)


class DetectiveApp(QApplication):
    def __init__(self):
        super().__init__()
        self.workspace = Workspace()
        self.main_window = QMainWindow()

    def run(self):
        self.main_window.show()
        self.exec_()
