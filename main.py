import sys
from typing import Dict, Set

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QTableWidgetItem
from qfluentwidgets import FluentWindow, FluentTranslator, FluentIcon, NavigationItemPosition, MessageBox
import sympy
from sympy import Eq, Symbol

import interfaces
from classes import Point

__version__ = '1.2'


class Question:
    def __init__(self, parent: "Window"):
        """
        存储一个问题的所有信息
        :param parent: w
        """
        self.w = parent
        # 点的字典，键为名字，值为点的对象
        self.points: Dict[str, Point] = {}
        # 所有条件的字典，键为文字表述，值为sympy.Eq对象
        self.conditions: Dict[str, Eq] = {}

    def symbols(self) -> Set[Symbol]:
        """获取所有要用的符号"""
        result = set()
        for i in self.points.values():
            if isinstance(i.x, Symbol):
                result.add(i.x)
            if isinstance(i.y, Symbol):
                result.add(i.y)
        return result

    def add_point(self, point: Point):
        """
        执行预化简（如果开了的话）,添加点并显示
        :param point: 点的对象
        :return:
        """
        # 预化简
        if self.w.ui_add.CheckBox_pre_simplify.isChecked():
            point.x = sympy.simplify(point.x)
            point.y = sympy.simplify(point.y)
        # 添加点
        self.points[point.name] = point
        self.update_tableview()

    def add_condition(self, eq: Eq, text: str):
        """
        添加条件并显示
        :param eq: 条件的方程
        :param text: 条件的文本
        :return:
        """
        # 预化简
        if self.w.ui_add.CheckBox_pre_simplify.isChecked():
            eq = sympy.simplify(eq)
        self.conditions[text] = eq
        self.update_tableview()

    def update_tableview(self):
        """更新tableview"""
        # 点
        point_cnt = len(self.points)
        self.w.ui_add.ListWidget_points.setRowCount(point_cnt)
        i = 0
        for name, point in self.points.items():
            self.w.ui_add.ListWidget_points.setItem(i, 0, QTableWidgetItem(name))
            self.w.ui_add.ListWidget_points.setItem(i, 1, QTableWidgetItem(str(point.x)))
            self.w.ui_add.ListWidget_points.setItem(i, 2, QTableWidgetItem(str(point.y)))
            self.w.ui_add.ListWidget_points.resizeColumnsToContents()
            i += 1
        # 条件
        condition_cnt = len(self.conditions)
        self.w.ui_add.ListWidget_conditions.setRowCount(condition_cnt)
        i = 0
        for text, eq in self.conditions.items():
            self.w.ui_add.ListWidget_conditions.setItem(i, 0, QTableWidgetItem(text))
            self.w.ui_add.ListWidget_conditions.setItem(i, 1, QTableWidgetItem(f'{eq.lhs} = {eq.rhs}'))
            self.w.ui_add.ListWidget_conditions.resizeColumnsToContents()
            i += 1

    def delete(self):
        """删除点/条件"""
        to_del = self.w.ui_add.LineEdit_delete.text()
        # 删除点
        if to_del in self.points.keys():
            del self.w.question.points[to_del]
        # 删除条件
        elif to_del in self.conditions.keys():
            del self.conditions[to_del]
        self.update_tableview()


class Window(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f'几何计算器 {__version__}')
        self.resize(800, 600)

        # 目前的题目
        self.question = Question(self)

        # 添加子界面
        self.ui_add = interfaces.InterfaceAdd(self)
        self.addSubInterface(self.ui_add, FluentIcon.ADD, '添加点和条件')
        self.ui_solve = interfaces.InterfaceSolve(self)
        self.addSubInterface(self.ui_solve, FluentIcon.EDIT, '求解')
        self.ui_help = interfaces.InterfaceHelp(self)
        self.addSubInterface(self.ui_help, FluentIcon.HELP, '帮助与关于', NavigationItemPosition.BOTTOM)

        # 报错不崩溃
        # sys.excepthook = self.error

    def error(self, etype: type, value: Exception, tb):
        """处理报错的函数"""
        w = MessageBox('错误', f'{etype.__name__}: {value}', self)
        w.exec()


if __name__ == '__main__':
    # 启用高分辨率缩放 enable hidpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Ceil)
    app = QApplication(sys.argv)
    # 国际化
    # 为啥translator不生效啊，我不理解啊啊啊啊啊
    translator = FluentTranslator()
    app.installTranslator(translator)
    w = Window()
    w.show()
    sys.exit(app.exec())
