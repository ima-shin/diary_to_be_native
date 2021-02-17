from PyQt5.QtWidgets import (
    QPushButton, QHBoxLayout, QVBoxLayout, QDialog, QLabel, QTextEdit
)
from PyQt5.QtCore import QThread, pyqtSignal, Qt
import datetime
from entity.diary import Diary
from settings import *
from repository.repository import DiariesRepository
from base import BaseWindow


class DiaryWindow(BaseWindow):
    """日記記入画面"""

    repository = DiariesRepository()

    def __init__(self, parent=None, today=None, *args, **kwargs):
        super().__init__()
        self.window = QDialog(parent)
        self.window.setWindowTitle('Diary To Be Native | Diary')
        self.window.setWindowFlags(
            Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint
        )
        self.parent = parent
        self.today = today

        self.diary = self.repository.find_by_date(today)
        if self.diary is None:
            # 指定した日付の日記が見つからなかった場合は新たに登録する
            self.diary = Diary()
            self.diary.written_date = self.today
            self.create_new_diary(self.diary)

        self.date_label, self.save_btn, self.last_updated_at, self.letter_length, self.textarea =\
            QLabel(today), QPushButton("保存"), QLabel(), QLabel(), QTextEdit()

        # self.fetch_record_worker = LoadDiaryWorker()
        # self.fetch_record_thread = QThread()

        self.init_layout()
        # self.init_thread()

    def init_layout(self):

        # 更新完了ボタン
        auto_saved_label = QLabel()
        auto_saved_label.setText('最終更新時刻: ')

        # 保存ボタン
        self.save_btn.clicked.connect(self.update_diary)

        # 最終更新日時
        self.last_updated_at.setText(self.diary.updated_at)

        # テキストエリア
        self.textarea.textChanged.connect(self.count_text)
        self.textarea.setText(self.diary.content)

        self.window.setGeometry(0, 0, 1000, 600)

        vbox = QVBoxLayout()
        vbox.setSpacing(20)

        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(self.date_label)
        hbox_1.addStretch(2)

        hbox_1_right = QHBoxLayout()
        hbox_1_right.addWidget(self.save_btn)
        vbox_1_right = QVBoxLayout()
        vbox_1_right.addWidget(auto_saved_label)
        vbox_1_right.addWidget(self.last_updated_at)

        hbox_1_right.addLayout(vbox_1_right)

        hbox_1.addLayout(hbox_1_right)

        vbox.addLayout(hbox_1)

        vbox.addWidget(self.textarea)

        vbox.addWidget(self.letter_length)

        self.window.setLayout(vbox)

    # def init_thread(self):
    #     self.fetch_record_worker.moveToThread(self.fetch_record_thread)
    #     self.fetch_record_worker.signal.connect(self.progress.setValue)
    #     self.fetch_record_worker.finished.connect(self.finish_load_record_thread)
    #     self.fetch_record_thread.started.connect(self.fetch_record_worker.run)
    #     self.fetch_record_thread.start()
    #
    # def finish_load_record_thread(self):
    #     self.fetch_record_thread.quit()
    #     self.fetch_record_thread.wait()
    #
    # def finish_auto_save_thread(self):
    #     pass

    def show(self):
        self.window.exec_()

    # 文字数をカウント
    def count_text(self):
        text = self.textarea.toPlainText()
        self.letter_length.setText(str(len(text)))

    # 日記を保存
    def update_diary(self):
        self.diary.content = self.textarea.toPlainText()
        self.diary.updated_at = datetime.datetime.now(JST).strftime(DATE_FORMAT)
        self.diary.letter_length = self.letter_length.text()

        self.repository.update(self.diary)
        if self.repository.has_error:
            self.statusBar().showMessage(self.repository.error_message)

    # 新しい日記レコードを挿入
    def create_new_diary(self, diary: Diary):
        if not self.repository.has_error:
            self.repository.create(diary)
        else:
            self.statusbar.showMessage('Failed to connect database')


# class AutoSaveWorker(QThread):
#     repository = DiariesRepository()
#
#     _signal = pyqtSignal(int)
#
#     """文字数カウントスレッド"""
#     def __init__(self, *args, **kwargs):
#         QThread.__init__(self, *args, **kwargs)
#
#     def run(self):
#         pass
