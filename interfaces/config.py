# coding:utf-8

from qfluentwidgets import qconfig, QConfig


class Config(QConfig):
    """ Config of application """


cfg = Config()
qconfig.load('config/config.json', cfg)
