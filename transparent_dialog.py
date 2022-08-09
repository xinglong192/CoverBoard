from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog

from ui_CusTDialog import Ui_CusTDialog


class TransparentDialog(QDialog, Ui_CusTDialog):

    def __init__(self, val=255, parent=None):
        super(TransparentDialog, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.tvSlider.setValue(val)
        self.start = val

    @Slot()
    def on_btnOk_clicked(self):
        self.accept()

    @Slot()
    def on_btnCancel_clicked(self):
        self.reject()

    @Slot()
    def on_tvSlider_valueChanged(self):
        v = self.tvSlider.value()
        if self.parent():
            self.parent().setWindowOpacity(v / 255)

    def getVal(self):
        r = self.exec_()
        if r == QDialog.Accepted:
            return self.tvSlider.value()
        else:
            if self.parent():
                self.parent().setWindowOpacity(self.start / 255)
            return self.start
