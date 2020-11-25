from PySide2.QtCore import *
from PySide2.QtWidgets import *


class TheFileMenu(QMenu):

    def __init__(self):
        super().__init__()
        self.setTitle("File")

        new_action = QAction("New", self)
        new_action.triggered.connect(self.new_store)
        self.addAction(new_action)

        load_file_action = QAction("Load File", self)
        load_file_action.triggered.connect(self.ask_load_file)
        self.addAction(load_file_action)

        save_file_action = QAction("Save File", self)
        save_file_action.triggered.connect(self.ask_save_file)
        self.addAction(save_file_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.ask_exit)
        self.addAction(exit_action)

    @Slot()
    def new_store(self):
        QApplication.instance().stix_store_model.reset()

    @Slot()
    def ask_load_file(self):
        load_path = QFileDialog.getOpenFileName(
            caption="Load STIX Bundle File",
            filter="STIX Bundle (*.json)"
        )[0]
        QApplication.instance().stix_store_model.load_file(load_path=load_path)

    @Slot()
    def ask_save_file(self):
        save_path = QFileDialog.getSaveFileName(
            caption="Save STIX Bundle File",
            filter="STIX Bundle (*.json)"
        )
        QApplication.instance().stix_store_model.save_file(save_path=save_path)

    @Slot()
    def ask_exit(self):
        exit_message_box = QMessageBox(
            QMessageBox.Warning,
            "Exit",
            "Are you sure you want to exit?",
            buttons=QMessageBox.Yes | QMessageBox.Cancel
        )
        return_value = exit_message_box.exec_()
        if return_value == QMessageBox.Yes:
            QApplication.quit()


class TheEditMenu(QMenu):
    def __init__(self):
        super().__init__()
        self.setTitle("Edit")

        new_object_action = QAction("New Object", self)
        self.addAction(new_object_action)
