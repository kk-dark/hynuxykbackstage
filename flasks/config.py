import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    threaded = True
    processes = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:03190319@localhost:3306/grade?charset=utf8mb4"
    wx_appsecret = os.getenv('wx_appsecret')
    appid = "wxe432820317bce964"

    @staticmethod
    def __int__(self):
        pass
