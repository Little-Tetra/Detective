from PySide2.QtWidgets import *

from .components import TheFileMenu, TheEditMenu
from .models import StixStoreModel
from .views import MainView


class Detective(QApplication):
    def __init__(self):
        super().__init__()

        self.stix_store_model = StixStoreModel()

        self.main_window = QMainWindow()
        self.main_window.setWindowTitle("Detective")
        self.main_window.resize(1280, 720)

        menu_bar = QMenuBar()
        file_menu = TheFileMenu()
        menu_bar.addMenu(file_menu)
        edit_menu = TheEditMenu()
        menu_bar.addMenu(edit_menu)
        self.main_window.setMenuBar(menu_bar)

        main_view = MainView()
        self.main_window.setCentralWidget(main_view)

    def run(self):
        self.main_window.show()
        self.exec_()
