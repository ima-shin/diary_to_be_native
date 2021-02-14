from PyQt5.QtCore import QThread, pyqtSignal

from repository.repository import DiariesRepository


class AutoSaveWorker(QThread):
    """日記自動保存"""
    repository = DiariesRepository()

    signal = pyqtSignal()
    finished = pyqtSignal()

    """文字数カウントスレッド"""
    def __init__(self, *args, **kwargs):
        QThread.__init__(self, *args, **kwargs)

    def run(self):
        pass


class LoadDiaryWorker(QThread):
    """日記読み込み"""
    repository = DiariesRepository()

    signal = pyqtSignal()
    finished = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(self)

    def run(self):
        pass
