# Form implementation generated from reading ui file 'ui_add.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Add(object):
    def setupUi(self, Add):
        Add.setObjectName("Add")
        Add.resize(800, 600)
        self.gridLayout_6 = QtWidgets.QGridLayout(Add)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.PushButton_intersection = PushButton(parent=Add)
        self.PushButton_intersection.setObjectName("PushButton_intersection")
        self.gridLayout_2.addWidget(self.PushButton_intersection, 2, 0, 1, 1)
        self.PushButton_point_on_line = PushButton(parent=Add)
        self.PushButton_point_on_line.setObjectName("PushButton_point_on_line")
        self.gridLayout_2.addWidget(self.PushButton_point_on_line, 3, 0, 1, 1)
        self.PushButton_point = PushButton(parent=Add)
        self.PushButton_point.setObjectName("PushButton_point")
        self.gridLayout_2.addWidget(self.PushButton_point, 1, 0, 1, 1)
        self.CardWidget = CardWidget(parent=Add)
        self.CardWidget.setObjectName("CardWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.CardWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.ListWidget_points = TableWidget(parent=self.CardWidget)
        self.ListWidget_points.setObjectName("ListWidget_points")
        self.ListWidget_points.setColumnCount(0)
        self.ListWidget_points.setRowCount(0)
        self.gridLayout.addWidget(self.ListWidget_points, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.CardWidget, 5, 0, 1, 1)
        self.TitleLabel = TitleLabel(parent=Add)
        self.TitleLabel.setObjectName("TitleLabel")
        self.gridLayout_2.addWidget(self.TitleLabel, 0, 0, 1, 1)
        self.SubtitleLabel = SubtitleLabel(parent=Add)
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        self.gridLayout_2.addWidget(self.SubtitleLabel, 4, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.TitleLabel_2 = TitleLabel(parent=Add)
        self.TitleLabel_2.setObjectName("TitleLabel_2")
        self.gridLayout_4.addWidget(self.TitleLabel_2, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        self.PushButton_parallel = PushButton(parent=Add)
        self.PushButton_parallel.setObjectName("PushButton_parallel")
        self.gridLayout_4.addWidget(self.PushButton_parallel, 1, 0, 1, 3)
        self.PushButton_vertical = PushButton(parent=Add)
        self.PushButton_vertical.setObjectName("PushButton_vertical")
        self.gridLayout_4.addWidget(self.PushButton_vertical, 2, 0, 1, 3)
        self.PushButton_eq = PushButton(parent=Add)
        self.PushButton_eq.setObjectName("PushButton_eq")
        self.gridLayout_4.addWidget(self.PushButton_eq, 3, 0, 1, 3)
        self.SubtitleLabel_2 = SubtitleLabel(parent=Add)
        self.SubtitleLabel_2.setObjectName("SubtitleLabel_2")
        self.gridLayout_4.addWidget(self.SubtitleLabel_2, 4, 0, 1, 3)
        self.CardWidget_2 = CardWidget(parent=Add)
        self.CardWidget_2.setObjectName("CardWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.CardWidget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ListWidget_conditions = TableWidget(parent=self.CardWidget_2)
        self.ListWidget_conditions.setObjectName("ListWidget_conditions")
        self.ListWidget_conditions.setColumnCount(0)
        self.ListWidget_conditions.setRowCount(0)
        self.gridLayout_3.addWidget(self.ListWidget_conditions, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.CardWidget_2, 5, 0, 1, 3)
        self.CheckBox_pre_simplify = CheckBox(parent=Add)
        self.CheckBox_pre_simplify.setChecked(True)
        self.CheckBox_pre_simplify.setObjectName("CheckBox_pre_simplify")
        self.gridLayout_4.addWidget(self.CheckBox_pre_simplify, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.BodyLabel = BodyLabel(parent=Add)
        self.BodyLabel.setObjectName("BodyLabel")
        self.gridLayout_5.addWidget(self.BodyLabel, 0, 0, 1, 1)
        self.LineEdit_delete = LineEdit(parent=Add)
        self.LineEdit_delete.setObjectName("LineEdit_delete")
        self.gridLayout_5.addWidget(self.LineEdit_delete, 0, 1, 1, 1)
        self.PushButton_delete = PushButton(parent=Add)
        self.PushButton_delete.setStyleSheet("PushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
"    color: red;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    border-radius: 5px;\n"
"    /* font: 14px \'Segoe UI\', \'Microsoft YaHei\'; */\n"
"    padding: 5px 12px 6px 12px;\n"
"    outline: none;\n"
"}\n"
"\n"
"ToolButton {\n"
"    padding: 5px 9px 6px 8px;\n"
"}\n"
"\n"
"PushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 12px;\n"
"}\n"
"\n"
"PushButton[hasIcon=true] {\n"
"    padding: 5px 12px 6px 36px;\n"
"}\n"
"\n"
"DropDownToolButton, PrimaryDropDownToolButton {\n"
"    padding: 5px 31px 6px 8px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=false],\n"
"PrimaryDropDownPushButton[hasIcon=false] {\n"
"    padding: 5px 31px 6px 12px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=true],\n"
"PrimaryDropDownPushButton[hasIcon=true] {\n"
"    padding: 5px 31px 6px 36px;\n"
"}\n"
"\n"
"PushButton:hover, ToolButton:hover, ToggleButton:hover, ToggleToolButton:hover {\n"
"    background: rgba(249, 249, 249, 0.5);\n"
"}\n"
"\n"
"PushButton:pressed, ToolButton:pressed, ToggleButton:pressed, ToggleToolButton:pressed {\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"}\n"
"\n"
"PushButton:disabled, ToolButton:disabled, ToggleButton:disabled, ToggleToolButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 0.06);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
"}\n"
"\n"
"\n"
"PrimaryPushButton,\n"
"PrimaryToolButton,\n"
"ToggleButton:checked,\n"
"ToggleToolButton:checked {\n"
"    color: white;\n"
"    background-color: #009faa;\n"
"    border: 1px solid #00a7b3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:hover,\n"
"PrimaryToolButton:hover,\n"
"ToggleButton:checked:hover,\n"
"ToggleToolButton:checked:hover {\n"
"    background-color: #00a7b3;\n"
"    border: 1px solid #2daab3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:pressed,\n"
"PrimaryToolButton:pressed,\n"
"ToggleButton:checked:pressed,\n"
"ToggleToolButton:checked:pressed {\n"
"    color: rgba(255, 255, 255, 0.63);\n"
"    background-color: #3eabb3;\n"
"    border: 1px solid #3eabb3;\n"
"}\n"
"\n"
"PrimaryPushButton:disabled,\n"
"PrimaryToolButton:disabled,\n"
"ToggleButton:checked:disabled,\n"
"ToggleToolButton:checked:disabled {\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"    background-color: rgb(205, 205, 205);\n"
"    border: 1px solid rgb(205, 205, 205);\n"
"}\n"
"\n"
"SplitDropButton,\n"
"PrimarySplitDropButton {\n"
"    border-left: none;\n"
"    border-top-left-radius: 0;\n"
"    border-bottom-left-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton,\n"
"#splitToolButton,\n"
"#primarySplitPushButton,\n"
"#primarySplitToolButton {\n"
"    border-top-right-radius: 0;\n"
"    border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton:pressed,\n"
"#splitToolButton:pressed,\n"
"SplitDropButton:pressed {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"}\n"
"\n"
"PrimarySplitDropButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"#primarySplitPushButton, #primarySplitToolButton {\n"
"    border-right: 1px solid #3eabb3;\n"
"}\n"
"\n"
"#primarySplitPushButton:pressed, #primarySplitToolButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"HyperlinkButton {\n"
"    /* font: 14px \'Segoe UI\', \'Microsoft YaHei\'; */\n"
"    padding: 6px 12px 6px 12px;\n"
"    color: #009faa;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=false] {\n"
"    padding: 6px 12px 6px 12px;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=true] {\n"
"    padding: 6px 12px 6px 36px;\n"
"}\n"
"\n"
"HyperlinkButton:hover {\n"
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 10);\n"
"    border: none;\n"
"}\n"
"\n"
"HyperlinkButton:pressed {\n"
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
"HyperlinkButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.43);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"RadioButton {\n"
"    min-height: 24px;\n"
"    max-height: 24px;\n"
"    background-color: transparent;\n"
"    font: 14px \'Segoe UI\', \'Microsoft YaHei\', \'PingFang SC\';\n"
"    color: black;\n"
"}\n"
"\n"
"RadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 11px;\n"
"    border: 2px solid #999999;\n"
"    background-color: rgba(0, 0, 0, 5);\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"RadioButton::indicator:hover {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"RadioButton::indicator:pressed {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(225, 224, 223),\n"
"            stop:1 rgb(225, 224, 223));\n"
"}\n"
"\n"
"RadioButton::indicator:checked {\n"
"    height: 22px;\n"
"    width: 22px;\n"
"    border: none;\n"
"    border-radius: 11px;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:hover {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(255, 255, 255),\n"
"            stop:0.7 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton:disabled {\n"
"    color: rgba(0, 0, 0, 110);\n"
"}\n"
"\n"
"RadioButton::indicator:disabled {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"RadioButton::indicator:disabled:checked {\n"
"    border: none;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgba(0, 0, 0, 0.2169),\n"
"            stop:1 rgba(0, 0, 0, 0.2169));\n"
"}\n"
"\n"
"TransparentToolButton,\n"
"TransparentToggleToolButton,\n"
"TransparentDropDownToolButton,\n"
"TransparentPushButton,\n"
"TransparentDropDownPushButton,\n"
"TransparentTogglePushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"TransparentToolButton:hover,\n"
"TransparentToggleToolButton:hover,\n"
"TransparentDropDownToolButton:hover,\n"
"TransparentPushButton:hover,\n"
"TransparentDropDownPushButton:hover,\n"
"TransparentTogglePushButton:hover {\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:pressed,\n"
"TransparentToggleToolButton:pressed,\n"
"TransparentDropDownToolButton:pressed,\n"
"TransparentPushButton:pressed,\n"
"TransparentDropDownPushButton:pressed,\n"
"TransparentTogglePushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:disabled,\n"
"TransparentToggleToolButton:disabled,\n"
"TransparentDropDownToolButton:disabled,\n"
"TransprentPushButton:disabled,\n"
"TransparentDropDownPushButton:disabled,\n"
"TransprentTogglePushButton:disabled {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"PillPushButton,\n"
"PillPushButton:hover,\n"
"PillPushButton:pressed,\n"
"PillPushButton:disabled,\n"
"PillPushButton:checked,\n"
"PillPushButton:checked:hover,\n"
"PillPushButton:checked:pressed,\n"
"PillPushButton:disabled:checked,\n"
"PillToolButton,\n"
"PillToolButton:hover,\n"
"PillToolButton:pressed,\n"
"PillToolButton:disabled,\n"
"PillToolButton:checked,\n"
"PillToolButton:checked:hover,\n"
"PillToolButton:checked:pressed,\n"
"PillToolButton:disabled:checked {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"")
        self.PushButton_delete.setObjectName("PushButton_delete")
        self.gridLayout_5.addWidget(self.PushButton_delete, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 2)

        self.retranslateUi(Add)
        QtCore.QMetaObject.connectSlotsByName(Add)

    def retranslateUi(self, Add):
        _translate = QtCore.QCoreApplication.translate
        Add.setWindowTitle(_translate("Add", "Form"))
        self.PushButton_intersection.setText(_translate("Add", "添加交点"))
        self.PushButton_point_on_line.setText(_translate("Add", "添加线上的点"))
        self.PushButton_point.setText(_translate("Add", "添加点"))
        self.TitleLabel.setText(_translate("Add", "创建点"))
        self.SubtitleLabel.setText(_translate("Add", "已有的点："))
        self.TitleLabel_2.setText(_translate("Add", "条件"))
        self.PushButton_parallel.setText(_translate("Add", "平行"))
        self.PushButton_vertical.setText(_translate("Add", "垂直"))
        self.PushButton_eq.setText(_translate("Add", "等式"))
        self.SubtitleLabel_2.setText(_translate("Add", "已有的条件（方程）："))
        self.CheckBox_pre_simplify.setText(_translate("Add", "预化简"))
        self.BodyLabel.setText(_translate("Add", "删除点/条件"))
        self.PushButton_delete.setText(_translate("Add", "确认"))
from qfluentwidgets import BodyLabel, CardWidget, CheckBox, LineEdit, PushButton, SubtitleLabel, TableWidget, TitleLabel
