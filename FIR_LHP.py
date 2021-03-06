

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FIR_Design(object):
    def setupUi(self, FIR_Design):
        FIR_Design.setObjectName("FIR_Design")
        FIR_Design.resize(505, 232)
        self.gridLayout_2 = QtWidgets.QGridLayout(FIR_Design)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(FIR_Design)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(FIR_Design)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(FIR_Design)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(FIR_Design)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.numtaps = QtWidgets.QSpinBox(FIR_Design)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.numtaps.setFont(font)
        self.numtaps.setMinimum(1)
        self.numtaps.setMaximum(100001)
        self.numtaps.setSingleStep(2)
        self.numtaps.setObjectName("numtaps")
        self.gridLayout.addWidget(self.numtaps, 0, 1, 1, 1)
        self.frequency_ = QtWidgets.QDoubleSpinBox(FIR_Design)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.frequency_.setFont(font)
        self.frequency_.setDecimals(6)
        self.frequency_.setMaximum(1.0)
        self.frequency_.setSingleStep(0.001)
        self.frequency_.setProperty("value", 0.1)
        self.frequency_.setObjectName("frequency_")
        self.gridLayout.addWidget(self.frequency_, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(FIR_Design)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(FIR_Design)
        self.buttonBox.accepted.connect(self.onOk)# Added
        self.buttonBox.rejected.connect(FIR_Design.reject)
        QtCore.QMetaObject.connectSlotsByName(FIR_Design)
        self.buttonBox.accepted.connect(FIR_Design.accept)#Displaced

    def retranslateUi(self, FIR_Design):
        _translate = QtCore.QCoreApplication.translate
        FIR_Design.setWindowTitle(_translate("FIR_Design", "Design FIR Filter "))
        self.label_3.setText(_translate("FIR_Design", "Cutoff Frequency (0-1):"))
        self.comboBox.setItemText(0, _translate("FIR_Design", "boxcar"))
        self.comboBox.setItemText(1, _translate("FIR_Design", "triang"))
        self.comboBox.setItemText(2, _translate("FIR_Design", "blackman"))
        self.comboBox.setItemText(3, _translate("FIR_Design", "hamming"))
        self.comboBox.setItemText(4, _translate("FIR_Design", "hann"))
        self.comboBox.setItemText(5, _translate("FIR_Design", "bartlett"))
        self.comboBox.setItemText(6, _translate("FIR_Design", "flattop"))
        self.comboBox.setItemText(7, _translate("FIR_Design", "parzen"))
        self.comboBox.setItemText(8, _translate("FIR_Design", "bohman"))
        self.comboBox.setItemText(9, _translate("FIR_Design", "blackmanharris"))
        self.comboBox.setItemText(10, _translate("FIR_Design", "nuttall"))
        self.comboBox.setItemText(11, _translate("FIR_Design", "barthann"))
        self.label_4.setText(_translate("FIR_Design", "              Window : "))
        self.label.setText(_translate("FIR_Design", "        No. of taps : "))

        ############ Added
    def onOk(self):
        ntaps = str(self.numtaps.text())
        freq = str(self.frequency_.text())
        win = str(self.comboBox.currentText())
        return int(ntaps), float(freq), win
        ############
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FIR_Design = QtWidgets.QDialog()
    ui = Ui_FIR_Design()
    ui.setupUi(FIR_Design)
    FIR_Design.show()
    sys.exit(app.exec_())

        
