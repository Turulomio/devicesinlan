# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/frmHelp.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmHelp(object):
    def setupUi(self, frmHelp):
        frmHelp.setObjectName("frmHelp")
        frmHelp.setWindowModality(QtCore.Qt.WindowModal)
        frmHelp.resize(549, 607)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmHelp.setWindowIcon(icon)
        frmHelp.setSizeGripEnabled(True)
        frmHelp.setModal(True)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(frmHelp)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblApp = QtWidgets.QLabel(frmHelp)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblApp.setFont(font)
        self.lblApp.setAlignment(QtCore.Qt.AlignCenter)
        self.lblApp.setObjectName("lblApp")
        self.verticalLayout.addWidget(self.lblApp)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lblPixmap = QtWidgets.QLabel(frmHelp)
        self.lblPixmap.setMaximumSize(QtCore.QSize(68, 68))
        self.lblPixmap.setPixmap(QtGui.QPixmap(":/help.png"))
        self.lblPixmap.setScaledContents(True)
        self.lblPixmap.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPixmap.setObjectName("lblPixmap")
        self.horizontalLayout.addWidget(self.lblPixmap)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(frmHelp)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cmbLanguage = QtWidgets.QComboBox(frmHelp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbLanguage.sizePolicy().hasHeightForWidth())
        self.cmbLanguage.setSizePolicy(sizePolicy)
        self.cmbLanguage.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.cmbLanguage.setObjectName("cmbLanguage")
        self.horizontalLayout_2.addWidget(self.cmbLanguage)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.viewer = QtWidgets.QTextBrowser(frmHelp)
        self.viewer.setObjectName("viewer")
        self.verticalLayout.addWidget(self.viewer)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(frmHelp)
        QtCore.QMetaObject.connectSlotsByName(frmHelp)

    def retranslateUi(self, frmHelp):
        _translate = QtCore.QCoreApplication.translate
        frmHelp.setWindowTitle(_translate("frmHelp", "DevicesInLan help"))
        self.lblApp.setText(_translate("frmHelp", "DevicesInLan help"))
        self.label_2.setText(_translate("frmHelp", "Select a language"))

import devicesinlan_rc