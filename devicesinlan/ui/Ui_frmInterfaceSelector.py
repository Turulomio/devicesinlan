# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'devicesinlan/ui/frmInterfaceSelector.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmInterfaceSelector(object):
    def setupUi(self, frmInterfaceSelector):
        frmInterfaceSelector.setObjectName("frmInterfaceSelector")
        frmInterfaceSelector.resize(539, 380)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/configure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmInterfaceSelector.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(frmInterfaceSelector)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblTitulo = QtWidgets.QLabel(frmInterfaceSelector)
        self.lblTitulo.setMinimumSize(QtCore.QSize(0, 30))
        self.lblTitulo.setMaximumSize(QtCore.QSize(16777215, 30))
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
        self.lblPixmap = QtWidgets.QLabel(frmInterfaceSelector)
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
        self.label_2 = QtWidgets.QLabel(frmInterfaceSelector)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.cmbName = QtWidgets.QComboBox(frmInterfaceSelector)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbName.sizePolicy().hasHeightForWidth())
        self.cmbName.setSizePolicy(sizePolicy)
        self.cmbName.setObjectName("cmbName")
        self.horizontalLayout.addWidget(self.cmbName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(frmInterfaceSelector)
        self.label.setMinimumSize(QtCore.QSize(150, 0))
        self.label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.txtId = QtWidgets.QLineEdit(frmInterfaceSelector)
        self.txtId.setObjectName("txtId")
        self.horizontalLayout_3.addWidget(self.txtId)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(frmInterfaceSelector)
        self.label_3.setMinimumSize(QtCore.QSize(150, 0))
        self.label_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.txtIP = QtWidgets.QLineEdit(frmInterfaceSelector)
        self.txtIP.setObjectName("txtIP")
        self.horizontalLayout_4.addWidget(self.txtIP)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(frmInterfaceSelector)
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
        self.label_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.txtMAC = QtWidgets.QLineEdit(frmInterfaceSelector)
        self.txtMAC.setObjectName("txtMAC")
        self.horizontalLayout_5.addWidget(self.txtMAC)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(frmInterfaceSelector)
        self.label_5.setMinimumSize(QtCore.QSize(150, 0))
        self.label_5.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.txtBroadcast = QtWidgets.QLineEdit(frmInterfaceSelector)
        self.txtBroadcast.setObjectName("txtBroadcast")
        self.horizontalLayout_6.addWidget(self.txtBroadcast)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(frmInterfaceSelector)
        self.label_6.setMinimumSize(QtCore.QSize(150, 0))
        self.label_6.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.txtMask = QtWidgets.QLineEdit(frmInterfaceSelector)
        self.txtMask.setObjectName("txtMask")
        self.horizontalLayout_7.addWidget(self.txtMask)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.buttonBox = QtWidgets.QDialogButtonBox(frmInterfaceSelector)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(frmInterfaceSelector)
        self.buttonBox.accepted.connect(frmInterfaceSelector.accept)
        self.buttonBox.rejected.connect(frmInterfaceSelector.reject)
        QtCore.QMetaObject.connectSlotsByName(frmInterfaceSelector)

    def retranslateUi(self, frmInterfaceSelector):
        _translate = QtCore.QCoreApplication.translate
        frmInterfaceSelector.setWindowTitle(_translate("frmInterfaceSelector", "Interface configuration"))
        self.lblTitulo.setText(_translate("frmInterfaceSelector", "Interface configuration"))
        self.label_2.setText(_translate("frmInterfaceSelector", "Select an interface"))
        self.label.setText(_translate("frmInterfaceSelector", "Interface Id"))
        self.label_3.setText(_translate("frmInterfaceSelector", "Interface Ip"))
        self.label_4.setText(_translate("frmInterfaceSelector", "Interface MAC"))
        self.label_5.setText(_translate("frmInterfaceSelector", "Interface broadcast"))
        self.label_6.setText(_translate("frmInterfaceSelector", "Interface Mask"))

import devicesinlan.images.devicesinlan_rc
