import mysql.connector as mysqldb
from entity.diary import Diary
from settings import *


class DiariesRepository(object):
    """データベース接続用クラス"""
    def __init__(self, *args, **kwargs):
        try:
            self.con = mysqldb.connect(
                user=USER,
                passwd=PASS,
                host=HOST,
                db=DB_NAME,
                charset='utf8',
            )
            self.con.ping(reconnect=True)
            self.con.autocommit = False
            self.has_error = False
        except Exception as e:
            print(e)
            self.has_error = True

    # 全レコード取得（データがなければNoneを返す）
    def fetch_all(self) -> [Diary]:
        query = "SELECT * FROM diaries"
        with self.con.cursor(dictionary=True, buffered=True) as cur:
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
        query = "SELECT * FROM diaries WHERE created_at = %s"
        with self.con.cursor(dictionary=True, buffered=True) as cur:
            cur.execute(query, (date,))
            entity = cur.fetchone()
            if entity is None:
                return None

            diary = Diary()
            diary.id = entity['id']
            diary.content = entity['content']
            diary.created_at = entity['created_at']
            diary.updated_at = entity['updated_at']

            return diary

    # レコードの新規追加
    def create(self, entity=None):
        query = "INSERT INTO diaries (id, content, created_at, updated_at) " \
                "VALUES (%s, %s, %s, %s);"
        with self.con.cursor() as cur:
            cur.execute(query, (entity.id, entity.content, entity.created_at, entity.updated_at,))
            self.con.commit()

    # レコードの更新
    def update(self, entity=None):
        query = "UPDATE diaries SET content = %s, updated_at = %s WHERE id = %s;"
        content = None if entity.content == '' else entity.content
        with self.con.cursor() as cur:
            cur.execute(query, (content, entity.updated_at, entity.id,))
            self.con.commit()
