from PySide2.QtWidgets import *


class MainView(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()

        self.store_list = QListView()
        self.store_list.setModel(QApplication.instance().stix_store_model)
        self.layout.addWidget(self.store_list)

        self.setLayout(self.layout)
