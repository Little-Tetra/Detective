import pkg_resources

import stix2

from PySide2.QtCore import QAbstractListModel, Qt
from PySide2.QtGui import QIcon


class StixStoreModel(QAbstractListModel):
    def __init__(self, path=None):
        super().__init__()
        self.path = path
        self.store = stix2.MemoryStore()
        self._data = self.store.query()

    def reset(self):
        self.store = stix2.MemoryStore()
        self._data = self.store.query()

    def load_file(self, load_path=None):
        self.reset()
        if load_path is not None:
            self.path = load_path
        self.store.load_from_file(self.path)
        self._data = self.store.query()
        self.dataChanged.emit(
            self.createIndex(0, 0),
            self.createIndex(self.rowCount(), 0)
        )

    def save_file(self, save_path=None):
        self.store.save_to_file(save_path or self.path)

    def rowCount(self, *args, **kwargs):
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
        obj = self._data[index.row()]
        if role == Qt.DisplayRole:
            return obj.get("name", obj.id)
        elif role == Qt.DecorationRole:
            type_icon_path = pkg_resources.resource_filename("detective", f"resources\\{obj.type}.png")
            return QIcon(type_icon_path)
