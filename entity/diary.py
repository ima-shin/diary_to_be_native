import datetime
import uuid
from settings import *


class Diary(object):
    """日記エンティティ"""

    def __init__(self):
        super().__init__()

        self.id = str(uuid.uuid4())
        self.content = ''
        self.written_date = str(datetime.datetime.now(JST).strftime(DATE_FORMAT))
        self.created_at = str(datetime.datetime.now(JST).strftime(DATE_FORMAT))
        self.updated_at = str(datetime.datetime.now(JST).strftime(DATE_FORMAT))
