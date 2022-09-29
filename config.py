import os.path

import app

DATABASE_FILE_PATH = os.path.join(os.getcwd(), 'test.db')


class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_FILE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
