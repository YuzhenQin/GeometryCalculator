from PyQt6.QtWidgets import QWidget, QAbstractItemView, QHeaderView, QMainWindow
from qfluentwidgets import MessageBoxBase
from sympy import sqrt, Eq

from .ui_add import Ui_Add
from .msgbox_point import Ui_MsgBoxPoint
from .msgbox_intersection import Ui_MsgBoxIntersection
from .msgbox_point_on_line import Ui_MsgBoxPointOnLine
from .msgbox_binary import Ui_MsgBoxBinary
from classes import *
import read

# 给ide代码补全用
if __name__ == '__main__':
    import main


class InterfaceAdd(QMainWindow, Ui_Add):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # 必须给子界面设置全局唯一的对象名
        self.setObjectName(self.__class__.__name__)

        self.w: "main.Window" = parent

        # 连接信号与槽
        self.connect()

        self.point_cnt = 0
        self.condition_cnt = 0

    @staticmethod
    def init_tableview(tableview):
        tableview.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        tableview.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        tableview.setBorderVisible(True)
        tableview.setBorderRadius(8)
        tableview.setWordWrap(False)

    def connect(self):
        """连接信号与槽"""
        # 创建点
        self.PushButton_point.clicked.connect(self.add_point)
        self.PushButton_intersection.clicked.connect(self.add_intersection)
        self.PushButton_point_on_line.clicked.connect(self.add_point_on_line)
        self.ListWidget_points.setColumnCount(3)
        self.ListWidget_points.setHorizontalHeaderLabels(['点', '横坐标 x', '纵坐标 y'])
        self.init_tableview(self.ListWidget_points)
        # 条件
        self.PushButton_parallel.clicked.connect(self.add_parallel)
        self.PushButton_vertical.clicked.connect(self.add_vertical)
        self.PushButton_eq.clicked.connect(self.add_eq)
        self.ListWidget_conditions.setColumnCount(2)
        self.ListWidget_conditions.setHorizontalHeaderLabels(['条件', '方程'])
        self.init_tableview(self.ListWidget_conditions)
        # 删除点/条件
        self.PushButton_delete.clicked.connect(self.delete)

    def add_point_and_show(self, point: Point):
        """
        执行预化简（如果开了的话），添加点并显示
        :param point: 点的对象
        :return:
        """
        self.w.question.add_point(point)

    def add_condition_and_show(self, eq: Eq, text: str):
        """
        添加条件并显示
        :param eq: 条件的方程
        :param text: 条件的文本
        :return:
        """
        # 预化简
        self.w.question.add_condition(eq, text)

    def add_point(self):
        """添加点"""
        w = MsgBoxPoint(self.w)
        if w.exec():
            # 读取输入的内容
            name = w.wid.LineEdit_name.text()
            try:
                x = read.to_expr(w.wid.LineEdit_x.text(), self.w.question.points)
            except:
                x = None
            try:
                y = read.to_expr(w.wid.LineEdit_y.text(), self.w.question.points)
            except:
                y = None
            # 创建点并添加
            point = Point(name, x, y)
            self.add_point_and_show(point)

    def add_intersection(self):
        """添加交点"""
        w = MsgBoxIntersection(self.w)
        if w.exec():
            # 读取输入的内容
            name = w.wid.LineEdit_name.text()
            l1 = read.to_line_object(w.wid.LineEdit_l1.text(), self.w.question.points)
            l2 = read.to_line_object(w.wid.LineEdit_l2.text(), self.w.question.points)
            # 创建点并添加
            point = Intersection(name, l1, l2)
            self.add_point_and_show(point)

    def add_point_on_line(self):
        """添加线上的点"""
        w = MsgBoxPointOnLine(self.w)
        if w.exec():
            # 读取输入的内容
            name = w.wid.LineEdit_name.text()
            l = read.to_line_object(w.wid.LineEdit_l.text(), self.w.question.points)
            try:
                x = read.to_expr(w.wid.LineEdit_x.text(), self.w.question.points)
            except:
                x = None
            # 创建点并添加
            point = PointOnLine(name, x, l)
            self.add_point_and_show(point)

    def add_parallel(self):
        """平行"""
        w = MsgBoxLinePositionRelationship(self.w, '//')
        if w.exec():
            # 读取输入的内容
            l1 = read.to_line_object(w.wid.LineEdit_1.text(), self.w.question.points)
            l2 = read.to_line_object(w.wid.LineEdit_2.text(), self.w.question.points)
            # 平行斜率相等
            eq = Eq(l1.k, l2.k)
            self.add_condition_and_show(eq, f'{w.wid.LineEdit_1.text()}//{w.wid.LineEdit_2.text()}')

    def add_vertical(self):
        """垂直"""
        w = MsgBoxLinePositionRelationship(self.w, '⊥')
        if w.exec():
            # 读取输入的内容
            l1 = read.to_line_object(w.wid.LineEdit_1.text(), self.w.question.points)
            l2 = read.to_line_object(w.wid.LineEdit_2.text(), self.w.question.points)
            # 垂直则斜率积为-1
            eq = Eq(l1.k * l2.k, -1)
            self.add_condition_and_show(eq, f'{w.wid.LineEdit_1.text()}⊥{w.wid.LineEdit_2.text()}')

    def add_eq(self):
        """等式"""
        w = MsgBoxEq(self.w)
        if w.exec():
            # 读取输入的内容
            left = read.to_expr(w.wid.LineEdit_1.text(), self.w.question.points)
            right = read.to_expr(w.wid.LineEdit_2.text(), self.w.question.points)
            # 两边相等
            eq = Eq(left, right)
            self.add_condition_and_show(eq, f'{w.wid.LineEdit_1.text()}={w.wid.LineEdit_2.text()}')

    def delete(self):
        """删除点/条件的槽函数"""
        self.w.question.delete()


def get_widget(Ui):
    """
    将ui类转换为widget对象供消息框使用
    :param Ui: ui类
    :return: 一个widget
    """

    class Widget(QWidget, Ui):
        def __init__(self):
            super().__init__()
            self.setupUi(self)

    widget = Widget()
    return widget


def is_number(s: str) -> bool:
    """
    检查字符串是否是合法的数字，包括小数、负数、分数、无理数
    :param s: 字符串
    :return: 是数字则为True，不是为False
    """
    try:
        eval(s)
    except:
        return False
    else:
        return True


class MsgBoxPoint(MessageBoxBase):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.wid: Ui_MsgBoxPoint = get_widget(Ui_MsgBoxPoint)
        self.viewLayout.addWidget(self.wid)
        # 初始禁用确定按钮
        self.yesButton.setEnabled(False)
        # 文本改动时检查
        self.wid.LineEdit_name.textChanged.connect(self._check)
        self.wid.LineEdit_x.textChanged.connect(self._check)
        self.wid.LineEdit_y.textChanged.connect(self._check)

    def _check(self):
        """检查输入是否合法，若合法则开放确定按钮"""
        name = self.wid.LineEdit_name.text()
        name_ok = len(name) == 1 and name.isupper()
        x = self.wid.LineEdit_x.text()
        x_ok = len(x) == 0 or is_number(x)
        y = self.wid.LineEdit_y.text()
        y_ok = len(y) == 0 or is_number(y)
        self.yesButton.setEnabled(name_ok and x_ok and y_ok)


class MsgBoxIntersection(MessageBoxBase):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.wid: Ui_MsgBoxIntersection = get_widget(Ui_MsgBoxIntersection)
        self.viewLayout.addWidget(self.wid)
        # 初始禁用确定按钮
        self.yesButton.setEnabled(False)
        # 文本改动时检查
        self.wid.LineEdit_name.textChanged.connect(self._check)
        self.wid.LineEdit_l1.textChanged.connect(self._check)
        self.wid.LineEdit_l2.textChanged.connect(self._check)

    def _check(self):
        """检查输入是否合法，若合法则开放确定按钮"""
        name = self.wid.LineEdit_name.text()
        name_ok = len(name) == 1 and name.isupper()
        l1 = self.wid.LineEdit_l1.text()
        l1_ok = len(l1) == 2 and l1.isupper()
        l2 = self.wid.LineEdit_l2.text()
        l2_ok = len(l2) == 2 and l2.isupper()
        self.yesButton.setEnabled(name_ok and l1_ok and l2_ok)


class MsgBoxPointOnLine(MessageBoxBase):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.wid: Ui_MsgBoxPointOnLine = get_widget(Ui_MsgBoxPointOnLine)
        self.viewLayout.addWidget(self.wid)
        # 初始禁用确定按钮
        self.yesButton.setEnabled(False)
        # 文本改动时检查
        self.wid.LineEdit_name.textChanged.connect(self._check)
        self.wid.LineEdit_l.textChanged.connect(self._check)
        self.wid.LineEdit_x.textChanged.connect(self._check)

    def _check(self):
        """检查输入是否合法，若合法则开放确定按钮"""
        name = self.wid.LineEdit_name.text()
        name_ok = len(name) == 1 and name.isupper()
        l = self.wid.LineEdit_l.text()
        l_ok = len(l) == 2 and l.isupper()
        x = self.wid.LineEdit_x.text()
        x_ok = len(x) == 0 or is_number(x)
        self.yesButton.setEnabled(name_ok and l_ok and x_ok)


class MsgBoxLinePositionRelationship(MessageBoxBase):
    def __init__(self, parent, relationship: str):
        """
        平行和相等的消息框的共同的类
        :param parent: w
        :param relationship: 中间显示的符号
        """
        super().__init__(parent=parent)
        # 所有二元的条件共用这一个ui
        self.wid: Ui_MsgBoxBinary = get_widget(Ui_MsgBoxBinary)
        self.viewLayout.addWidget(self.wid)
        self.wid.SubtitleLabel_symbol.setText(relationship)
        # 初始禁用确定按钮
        self.yesButton.setEnabled(False)
        # 文本改动时检查
        self.wid.LineEdit_1.textChanged.connect(self._check)
        self.wid.LineEdit_2.textChanged.connect(self._check)

    def _check(self):
        """检查输入是否合法，若合法则开放确定按钮"""
        l1 = self.wid.LineEdit_1.text()
        l1_ok = len(l1) == 2 and l1.isupper()
        l2 = self.wid.LineEdit_2.text()
        l2_ok = len(l2) == 2 and l2.isupper()
        self.yesButton.setEnabled(l1_ok and l2_ok)


class MsgBoxEq(MessageBoxBase):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.wid: Ui_MsgBoxBinary = get_widget(Ui_MsgBoxBinary)
        self.viewLayout.addWidget(self.wid)
        self.wid.SubtitleLabel_symbol.setText('=')
        # 输入时转化字符串
        self.wid.LineEdit_1.textChanged.connect(self._replace)
        self.wid.LineEdit_2.textChanged.connect(self._replace)

    def _replace(self):
        self.wid.LineEdit_1.setText(self._replace_one(self.wid.LineEdit_1.text()))
        self.wid.LineEdit_2.setText(self._replace_one(self.wid.LineEdit_2.text()))

    @staticmethod
    def _replace_one(s: str):
        """
        让字符串更漂亮
        :param s: 角AOB 90度 pi
        :return: ∠AOB 90° π
        """
        return s.replace('角', '∠').replace('度', '°').replace('pi', 'π')
