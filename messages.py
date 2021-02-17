"""表示用メッセージ列挙体"""
from enum import Enum


class Messages(Enum):
    # 通常メッセージ

    # エラーメッセージ
    DATA_INTEGRITY_ERROR = 'データの保存時にエラーが発生しました'
    DATABASE_CONNECTION_ERROR = 'データベースの接続時にエラーが発生しました'

    # システムエラー
    FATAL_ERROR = 'システムエラーが発生しました'
