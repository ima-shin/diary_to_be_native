import sqlite3
from sqlite3 import DatabaseError, IntegrityError
from contextlib import closing
from entity.diary import Diary
from settings import *
from messages import Messages


class DiariesRepository(object):
    """データベース接続用クラス"""
    def __init__(self, *args, **kwargs):
        try:
            self.con = sqlite3.connect(DB)
            self.con.row_factory = sqlite3.Row
            self.has_error = False
        except DatabaseError as e:
            self.has_error = True
            self.error_message = Messages.DATABASE_CONNECTION_ERROR.value

    # 全レコード取得（データがなければNoneを返す）
    def fetch_all(self) -> [Diary]:
        query = "SELECT * FROM diaries"
        with closing(self.con.cursor()) as cur:
            cur.execute(query)
            result = cur.fetchall()
            if result is None: return None

            diaries = []
            diary = Diary()
            for row in result:
                diary.id = row['id']
                diary.content = row['content']
                diary.created_at = row['created_at']
                diary.updated_at = row['updated_at']

                diaries.append(diary)
            return diaries

    # 指定した日付のデータを1件取得（データが空ならNoneを返す）
    def find_by_date(self, date=None) -> Diary:
        query = "SELECT * FROM diaries WHERE written_date = ?"
        with closing(self.con.cursor()) as cur:
            cur.execute(query, (date,))
            entity = cur.fetchone()
            if entity is None:
                return None

            diary = Diary()
            diary.id = entity['id']
            diary.content = entity['content']
            diary.written_date = date
            diary.created_at = entity['created_at']
            diary.updated_at = entity['updated_at']

            return diary

    # レコードの新規追加
    def create(self, entity=None):
        query = "INSERT INTO diaries (id, content, written_date, created_at, updated_at) " \
                "VALUES (?, ?, ?, ?, ?);"
        with closing(self.con.cursor()) as cur:
            try:
                cur.execute(query, (entity.id, entity.content, entity.written_date, entity.created_at, entity.updated_at,))
                self.con.commit()
            except IntegrityError as e:
                self.has_error = True
                self.error_message = Messages.DATA_INTEGRITY_ERROR.value
            except DatabaseError as e:
                self.has_error = True
                self.error_message = Messages.DATABASE_CONNECTION_ERROR.value
            except Exception as e:
                self.has_error = True
                self.error_message = Messages.FATAL_ERROR.value

    # レコードの更新
    def update(self, entity=None):
        query = "UPDATE diaries SET content = ?, updated_at = ? WHERE id = ?;"
        with closing(self.con.cursor()) as cur:
            try:
                cur.execute(query, (entity.content, entity.updated_at, entity.id,))
                self.con.commit()
            except IntegrityError as e:
                self.has_error = True
                self.error_message = Messages.DATA_INTEGRITY_ERROR.value
            except DatabaseError as e:
                self.has_error = True
                self.error_message = Messages.DATABASE_CONNECTION_ERROR.value
            except Exception as e:
                self.has_error = True
                self.error_message = Messages.FATAL_ERROR.value
