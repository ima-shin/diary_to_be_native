"""各種設定値"""
import pytz
import os

"""時刻関係"""
JST = pytz.timezone('Asia/Tokyo')
DATE_FORMAT = '%Y-%m-%d'

"""データファイル"""
FILEPATH = os.path.join(os.getcwd(), 'data.dat')

"""データベース"""
# 環境変数から取得
USER = os.environ.get('USER')
PASS = os.environ.get('PASS')
HOST = os.environ.get('HOST')
DB_NAME = os.environ.get('DB_NAME')
