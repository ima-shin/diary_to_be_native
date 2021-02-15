from PyQt5.QtWidgets import (
    QApplication, QLabel, QGridLayout, QCalendarWidget, QSizePolicy
)
from PyQt5.QtCore import QDate
import sys

from settings import *
from repository.repository import DiariesRepository
from sub_windows.windows import DiaryWindow
from base import BaseWindow


class App(BaseWindow):

    repository = DiariesRepository()

    def __init__(self, w_w=500, w_h=500):
        super().__init__()
        self.setWindowTitle('Diary To Be Native')
        self.setGeometry(int(w_w / 2 / 2), int(w_h / 2 / 2), 1000, 600)
        self.setFixedSize(self.size())
        self.message_label = QLabel()
        if self.repository.has_error:
            self.statusbar.showMessage('Failed to get connection with database')
            self.statusbar.show()

        self.init_ui()

    def init_ui(self):
        calendar = QCalendarWidget(self)
        calendar.setGeometry(0, 0, self.width(), self.height())
        calendar.setGridVisible(True)

        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(self.message_label, *(0, 0))
        for i in range(0, 2):
            grid.addWidget(calendar, *(i, 0))

        calendar.clicked[QDate].connect(self.on_clicked_calendar)

    def on_clicked_calendar(self, date):
        """日付クリックでその日付の日記を表示"""
        diary_window = DiaryWindow(parent=self, today=date.toPyDate().strftime(DATE_FORMAT))
        diary_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    desktop = app.desktop()
    ex = App(w_w=desktop.width(), w_h=desktop.height())
    ex.show()
    sys.exit(app.exec_())
