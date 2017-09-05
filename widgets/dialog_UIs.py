# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\work\compressor\widgets\dialog.ui'
#
# Created: Tue Sep 05 23:27:52 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_resizer(object):
    def setupUi(self, resizer):
        resizer.setObjectName("resizer")
        resizer.resize(628, 470)
        self.centralwidget = QtGui.QWidget(resizer)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.resize_w_spb = QtGui.QSpinBox(self.groupBox)
        self.resize_w_spb.setMinimum(100)
        self.resize_w_spb.setMaximum(10000)
        self.resize_w_spb.setProperty("value", 1000)
        self.resize_w_spb.setObjectName("resize_w_spb")
        self.horizontalLayout_2.addWidget(self.resize_w_spb)
        self.resize_h_spb = QtGui.QSpinBox(self.groupBox)
        self.resize_h_spb.setMinimum(100)
        self.resize_h_spb.setMaximum(10000)
        self.resize_h_spb.setProperty("value", 1000)
        self.resize_h_spb.setObjectName("resize_h_spb")
        self.horizontalLayout_2.addWidget(self.resize_h_spb)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.quality_spb = QtGui.QSpinBox(self.groupBox_2)
        self.quality_spb.setMinimum(50)
        self.quality_spb.setMaximum(100)
        self.quality_spb.setObjectName("quality_spb")
        self.horizontalLayout.addWidget(self.quality_spb)
        self.horizontalSlider = QtGui.QSlider(self.groupBox_2)
        self.horizontalSlider.setMinimum(50)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.clear_btn = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy)
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout.addWidget(self.clear_btn)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.list_ly = QtGui.QVBoxLayout()
        self.list_ly.setObjectName("list_ly")
        self.verticalLayout.addLayout(self.list_ly)
        self.verticalLayout.setStretch(2, 1)
        resizer.setCentralWidget(self.centralwidget)

        self.retranslateUi(resizer)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL("valueChanged(int)"), self.quality_spb.setValue)
        QtCore.QObject.connect(self.quality_spb, QtCore.SIGNAL("valueChanged(int)"), self.horizontalSlider.setValue)
        QtCore.QMetaObject.connectSlotsByName(resizer)

    def retranslateUi(self, resizer):
        resizer.setWindowTitle(QtGui.QApplication.translate("resizer", "Resize Images", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("resizer", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("resizer", "Quality", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_btn.setText(QtGui.QApplication.translate("resizer", "CLEAR", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("resizer", "Supported JPEG files only", None, QtGui.QApplication.UnicodeUTF8))

