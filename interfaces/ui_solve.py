# Form implementation generated from reading ui file '.\interfaces\ui_solve.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Solve(object):
    def setupUi(self, Solve):
        Solve.setObjectName("Solve")
        Solve.resize(800, 600)
        self.gridLayout_4 = QtWidgets.QGridLayout(Solve)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.SubtitleLabel = SubtitleLabel(parent=Solve)
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        self.gridLayout.addWidget(self.SubtitleLabel, 0, 0, 1, 1)
        self.LineEdit_want = LineEdit(parent=Solve)
        self.LineEdit_want.setObjectName("LineEdit_want")
        self.gridLayout.addWidget(self.LineEdit_want, 0, 1, 1, 1)
        self.PrimaryPushButton_solve = PrimaryPushButton(parent=Solve)
        self.PrimaryPushButton_solve.setObjectName("PrimaryPushButton_solve")
        self.gridLayout.addWidget(self.PrimaryPushButton_solve, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SubtitleLabel_timer = SubtitleLabel(parent=Solve)
        self.SubtitleLabel_timer.setObjectName("SubtitleLabel_timer")
        self.gridLayout_2.addWidget(self.SubtitleLabel_timer, 0, 0, 1, 1)
        self.IndeterminateProgressBar = IndeterminateProgressBar(parent=Solve)
        self.IndeterminateProgressBar.setObjectName("IndeterminateProgressBar")
        self.gridLayout_2.addWidget(self.IndeterminateProgressBar, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.TitleLabel = TitleLabel(parent=Solve)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.gridLayout_4.addWidget(self.TitleLabel, 0, 0, 1, 1)
        self.SubtitleLabel_state = SubtitleLabel(parent=Solve)
        self.SubtitleLabel_state.setObjectName("SubtitleLabel_state")
        self.gridLayout_4.addWidget(self.SubtitleLabel_state, 3, 0, 1, 1)
        self.SmoothScrollArea = SmoothScrollArea(parent=Solve)
        self.SmoothScrollArea.setWidgetResizable(True)
        self.SmoothScrollArea.setObjectName("SmoothScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 428))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.LargeTitleLabel_result = LargeTitleLabel(parent=self.scrollAreaWidgetContents)
        self.LargeTitleLabel_result.setText("")
        self.LargeTitleLabel_result.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LargeTitleLabel_result.setObjectName("LargeTitleLabel_result")
        self.gridLayout_3.addWidget(self.LargeTitleLabel_result, 0, 0, 1, 1)
        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.SmoothScrollArea, 4, 0, 1, 1)

        self.retranslateUi(Solve)
        QtCore.QMetaObject.connectSlotsByName(Solve)

    def retranslateUi(self, Solve):
        _translate = QtCore.QCoreApplication.translate
        Solve.setWindowTitle(_translate("Solve", "Form"))
        self.SubtitleLabel.setText(_translate("Solve", "求"))
        self.PrimaryPushButton_solve.setText(_translate("Solve", "开始计算"))
        self.SubtitleLabel_timer.setText(_translate("Solve", "用时 00:00:00.00"))
        self.TitleLabel.setText(_translate("Solve", "求解"))
        self.SubtitleLabel_state.setText(_translate("Solve", "未计算"))
from qfluentwidgets import IndeterminateProgressBar, LargeTitleLabel, LineEdit, PrimaryPushButton, SmoothScrollArea, SubtitleLabel, TitleLabel
