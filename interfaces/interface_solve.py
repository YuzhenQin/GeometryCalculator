import time

from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QWidget
import sympy

from .ui_solve import Ui_Solve
from .utils import tex2img
import read

if __name__ == '__main__':
    import main


class InterfaceSolve(QWidget, Ui_Solve):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)
        # 必须给子界面设置全局唯一的对象名
        self.setObjectName(self.__class__.__name__)

        self.w: "main.Window" = parent

        # 初始关闭进度条
        self.IndeterminateProgressBar.stop()

        # 求解的子线程
        self.thread_solve = ThreadSolve(self.w)
        # 计时器子线程
        self.thread_timer = ThreadTimer()

        # 连接信号与槽
        self.connect()

    def connect(self):
        """连接信号与槽"""
        self.LineEdit_want.textChanged.connect(self._replace)  # 输入
        self.PrimaryPushButton_solve.clicked.connect(self.solve)  # 开始计算
        self.thread_timer.sig_set_text.connect(self.SubtitleLabel_timer.setText)  # 计时器
        # 开始后
        self.thread_solve.started.connect(lambda: self.set_enabled(False))  # 禁用组件
        self.thread_solve.started.connect(self.thread_timer.start)  # 计时器，启动！（划掉）打开计时器
        self.thread_solve.started.connect(lambda: self.SubtitleLabel_state.setText('计算中，请耐心等待...'))  # 显示状态
        self.thread_solve.started.connect(self.IndeterminateProgressBar.start)  # 开启进度条
        # 完成后
        self.thread_solve.finished.connect(lambda: self.set_enabled(True))  # 启用组件
        self.thread_solve.finished.connect(self.show_result)  # 显示结果
        self.thread_solve.finished.connect(self.thread_timer.turn_off)  # 关闭计时器
        self.thread_solve.finished.connect(lambda: self.SubtitleLabel_state.setText('所有可能的结果如下'))  # 显示状态
        self.thread_solve.finished.connect(self.IndeterminateProgressBar.stop)  # 停止进度条

    def set_enabled(self, enabled: bool):
        """设置所有互动组件的可用/禁用"""
        self.PrimaryPushButton_solve.setEnabled(enabled)
        self.LineEdit_want.setEnabled(enabled)
        self.w.ui_add.PushButton_point.setEnabled(enabled)
        self.w.ui_add.PushButton_intersection.setEnabled(enabled)
        self.w.ui_add.PushButton_point_on_line.setEnabled(enabled)
        self.w.ui_add.PushButton_parallel.setEnabled(enabled)
        self.w.ui_add.PushButton_vertical.setEnabled(enabled)
        self.w.ui_add.PushButton_eq.setEnabled(enabled)
        self.w.ui_add.CheckBox_pre_simplify.setEnabled(enabled)

    def solve(self):
        """开始计算"""
        # 读取要求的值
        expr = read.to_expr(self.LineEdit_want.text(), self.w.question.points)
        a = sympy.Symbol('a')  # 要求的符号
        self.w.question.conditions['tmp'] = a - expr
        # 开子线程求解
        self.thread_solve.a = a
        self.thread_solve.start()

    def show_result(self):
        formula = ''
        for i in self.thread_solve.result:
            formula = formula + sympy.latex(i) + ','
        formula = formula.rstrip(',')
        self.LargeTitleLabel_result.setPixmap(tex2img(formula))

    def _replace(self):
        s = self.LineEdit_want.text()
        s = s.replace('角', '∠').replace('度', '°').replace('pi', 'π')
        self.LineEdit_want.setText(s)


class ThreadSolve(QThread):
    def __init__(self, w):
        """在多线程中解方程，不让主线程卡死"""
        super().__init__()
        self.result = None
        self.w: "main.Window" = w
        self.a = None

    def run(self):
        symbols = self.w.question.symbols()
        symbols.add(self.a)
        self.result = sympy.solve(self.w.question.conditions.values(), symbols, dict=True)
        self.result = set([i[self.a] for i in self.result])
        # 清理临时变量
        del self.w.question.conditions['tmp']


class ThreadTimer(QThread):
    sig_set_text = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.running = False

    def run(self):
        self.running = True
        t0 = time.time()
        while self.running:
            t = time.time() - t0
            h = str(int(t // 3600)).zfill(2)
            m = str(int(t % 3600 // 60)).zfill(2)
            s = str(int(t % 60)).zfill(2)
            f = str(int(t % 1 * 100)).zfill(2)  # float
            self.sig_set_text.emit(f'用时 {h}:{m}:{s}.{f}')
            time.sleep(0.01)

    def turn_off(self):
        self.running = False
