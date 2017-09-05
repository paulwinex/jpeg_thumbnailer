from PySide.QtGui import *
from PySide.QtCore import *
from widgets import dialog_UIs, file_list
import os, json
import imageprocess


class ResizeDialog(QMainWindow, dialog_UIs.Ui_resizer):
    prefs_file = os.path.expanduser('~/.compressor_prefs.json')

    def __init__(self):
        super(ResizeDialog, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.clear_btn.hide()
        self.list = file_list.FileList(self)
        self.list_ly.addWidget(self.list)
        self.clear_btn.clicked.connect(self.list.clear)
        self.list.dropedSignal.connect(lambda :QTimer.singleShot(200, self.next_file))
        self.is_active = False

    def compute_size(self, file):
        self.thread = QThread(self)
        self.w = Worker(file, [self.resize_w_spb.value(), self.resize_h_spb.value()],
                        self.quality_spb.value())
        self.w.moveToThread(self.thread)
        self.thread.started.connect(self.w.process)
        self.w.finished.connect(self.thread.quit)
        self.w.finished.connect(self.convert_complete)
        self.thread.start()
        self.is_active = True

    def next_file(self):
        if self.list.count():
            file = self.list.item(0).text()
            self.compute_size(file)

    def convert_complete(self):
        self.list.takeItem(0)
        self.is_active = False
        self.next_file()

    def showEvent(self, *args, **kwargs):
        data = None
        if os.path.exists(self.prefs_file):
            try:
                data = json.load(open(self.prefs_file))
            except:
                pass
            if data:
                self.resize_w_spb.setValue(data.get('w', self.resize_w_spb.value()))
                self.resize_h_spb.setValue(data.get('h', self.resize_h_spb.value()))
                self.quality_spb.setValue(data.get('q', self.quality_spb.value()))

        super(ResizeDialog, self).showEvent(*args, **kwargs)

    def closeEvent(self, *args, **kwargs):
        prefs = dict(
            w=self.resize_w_spb.value(),
            h=self.resize_h_spb.value(),
            q=self.quality_spb.value()
        )
        json.dump(prefs, open(self.prefs_file, 'w'), indent=2)
        super(ResizeDialog, self).closeEvent(*args, **kwargs)

    def hideEvent(self, *args, **kwargs):
        super(ResizeDialog, self).hideEvent(*args, **kwargs)
        self.close()


class Worker(QObject):
    message = Signal(int)
    finished = Signal()

    def __init__(self, file, size, quality):
        super(Worker, self).__init__()
        self.file = file
        self.size = size
        self.quality = quality

    def process(self):
        imageprocess.compress(self.file, size_h=self.size[0],
                              size_w=self.size[1], quality=self.quality)
        self.finished.emit()


if __name__ == '__main__':
    app = QApplication([])
    w = ResizeDialog()
    w.show()
    app.exec_()
