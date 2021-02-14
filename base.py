from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QProgressBar
)
from style import style


class BaseWindow(QMainWindow):
    """カスタムウインドウ基底クラス"""

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.statusBar()
        self.setStyleSheet(style)
        self.progress = QProgressBar(self)
        self.menubar = self.menuBar()
