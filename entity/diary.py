import datetime
import uuid
from settings import *


class Diary(object):
    """日記エンティティ"""

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.id = str(uuid.uuid4())
        self.content = ''
        self.created_at = str(datetime.datetime.now(JST).strftime(DATE_FORMAT))
        self.updated_at = str(datetime.datetime.now(JST).strftime(DATE_FORMAT))
        self.letter_length = 0

    def created_at_str(self):
        return str(self.created_at)

    def updated_at_str(self):
        return str(self.updated_at)
