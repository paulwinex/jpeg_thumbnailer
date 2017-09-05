from PySide.QtGui import *
from PySide.QtCore import *
import os


class FileList(QListWidget):
    dropedSignal = Signal()

    def __init__(self, parent):
        super(FileList, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropOverwriteMode(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
            urls = []
            for url in event.mimeData().urls():
                urls.append(str(url.toLocalFile()))
            self.dropedSignal.emit()
            self.add_files(urls)

        else:
            event.ignore()

    def add_files(self, urls):
        for url in urls:
            if not os.path.exists(url):
                continue
            if os.path.isfile(url):
                self.create_item(url)
            else:
                for path, dirs, files in  os.walk(url):
                    for f in files:
                        self.create_item(os.path.join(path, f))

    def create_item(self, url):
        if os.path.splitext(url)[-1].strip('.').lower() in ['jpg', 'jpeg']:
            self.addItem(url)