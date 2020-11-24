from PySide2.QtCore import *
from PySide2.QtWidgets import *


class TheMenuBar(QMenuBar):
    def __init__(self):
        super().__init__()
        self.file_menu = self.addMenu("File")

        load_action = QAction("Load", self)
        self.file_menu.addAction(load_action)

        save_action = QAction("Save", self)
        self.file_menu.addAction(save_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.exit_app)
        self.file_menu.addAction(exit_action)

    @Slot()
    def exit_app(self):
        QApplication.quit()
