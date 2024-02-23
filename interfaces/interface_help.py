from PyQt6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon

from .ui_help import Ui_Help

if __name__ == '__main__':
    import main


class InterfaceHelp(QWidget, Ui_Help):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)
        # 必须给子界面设置全局唯一的对象名
        self.setObjectName(self.__class__.__name__)

        self.w: "main.Window" = parent

        # 给按钮添加图标
        self.HyperlinkButton_author.setIcon(FluentIcon.LINK)
        self.HyperlinkButton_github.setIcon(FluentIcon.GITHUB)

        # 设置markdown
        with open('interfaces/help.md', encoding='utf-8') as f:
            md = f.read()
        self.TextEdit_help.setMarkdown(md)
