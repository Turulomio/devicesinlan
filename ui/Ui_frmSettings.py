# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/frmSettings.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmSettings(object):
    def setupUi(self, frmSettings):
        frmSettings.setObjectName("frmSettings")
        frmSettings.resize(385, 213)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/configure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmSettings.setWindowIcon(icon)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(frmSettings)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblTitulo = QtWidgets.QLabel(frmSettings)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setObjectName("lblTitulo")
        self.verticalLayout.addWidget(self.lblTitulo)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lblPixmap = QtWidgets.QLabel(frmSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPixmap.sizePolicy().hasHeightForWidth())
        self.lblPixmap.setSizePolicy(sizePolicy)
        self.lblPixmap.setMinimumSize(QtCore.QSize(48, 48))
        self.lblPixmap.setMaximumSize(QtCore.QSize(48, 48))
        self.lblPixmap.setPixmap(QtGui.QPixmap(":/configure.png"))
        self.lblPixmap.setScaledContents(True)
        self.lblPixmap.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPixmap.setObjectName("lblPixmap")
        self.horizontalLayout_2.addWidget(self.lblPixmap)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(frmSettings)
        self.label_2.setMinimumSize(QtCore.QSize(200, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.cmbLanguage = QtWidgets.QComboBox(frmSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbLanguage.sizePolicy().hasHeightForWidth())
        self.cmbLanguage.setSizePolicy(sizePolicy)
        self.cmbLanguage.setObjectName("cmbLanguage")
        self.horizontalLayout.addWidget(self.cmbLanguage)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(frmSettings)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.spnConcurrent = QtWidgets.QSpinBox(frmSettings)
        self.spnConcurrent.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnConcurrent.setMinimum(1)
        self.spnConcurrent.setMaximum(20000)
        self.spnConcurrent.setSingleStep(5)
        self.spnConcurrent.setProperty("value", 100)
        self.spnConcurrent.setObjectName("spnConcurrent")
        self.horizontalLayout_3.addWidget(self.spnConcurrent)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(frmSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.retranslateUi(frmSettings)
        self.buttonBox.accepted.connect(frmSettings.accept)
        self.buttonBox.rejected.connect(frmSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(frmSettings)

    def retranslateUi(self, frmSettings):
        _translate = QtCore.QCoreApplication.translate
        frmSettings.setWindowTitle(_translate("frmSettings", "DevicesInLan settings"))
        self.lblTitulo.setText(_translate("frmSettings", "DevicesInLan settings"))
        self.label_2.setText(_translate("frmSettings", "Select a language"))
        self.label.setText(_translate("frmSettings", "Concurrent requests"))

import devicesinlan_rc
