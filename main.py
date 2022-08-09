import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent, QContextMenuEvent, QCursor, QAction, QPalette
from PySide6.QtWidgets import QMainWindow, QApplication, QMenu, QStyle, QColorDialog

from transparent_dialog import TransparentDialog
from ui_coverboard import Ui_CoverBoard


class MainWindow(QMainWindow, Ui_CoverBoard):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint|Qt.NoDropShadowWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.r_menu = None
        self.start_pos = None
        self.setupUi(self)
        self.mainRMen()

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.start_pos = e.globalPosition().toPoint() - self.pos()

    def mouseMoveEvent(self, e: QMouseEvent):
        rel_pos = e.globalPosition().toPoint() - self.start_pos
        self.move(rel_pos)
        e.accept()

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        self.r_menu.exec(QCursor.pos())

    def mainRMen(self):
        r_menu = QMenu(self)
        quit_action = QAction(self.style().standardIcon(QStyle.SP_DirLinkOpenIcon), '退出程序')
        quit_action.setParent(r_menu)
        quit_action.triggered.connect(self.quitApp)

        color_action = QAction(self.style().standardIcon(QStyle.SP_DirLinkOpenIcon), '设置颜色')
        color_action.setParent(r_menu)
        color_action.triggered.connect(self.chooseColor)

        transparent_action = QAction(self.style().standardIcon(QStyle.SP_DirLinkOpenIcon), '设置透明度')
        transparent_action.setParent(r_menu)
        transparent_action.triggered.connect(self.transparent)

        top_action = QAction(self.style().standardIcon(QStyle.SP_DirLinkOpenIcon), '置顶/取消置顶')
        top_action.setParent(r_menu)
        top_action.triggered.connect(self.onTop)

        r_menu.addAction(color_action)
        r_menu.addAction(transparent_action)
        r_menu.addAction(top_action)
        r_menu.addAction(quit_action)
        self.r_menu = r_menu

    def onTop(self):
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowStaysOnTopHint)
        self.show()

    def chooseColor(self):
        color = QColorDialog.getColor(initial=self.palette().color(QPalette.Window), parent=self, title='选择颜色')
        if not color.isValid():
            return
        p = self.palette()
        p.setColor(QPalette.Window, color)
        self.setPalette(p)

    def transparent(self):
        TransparentDialog(self.windowOpacity() * 255, self).getVal()

    def quitApp(self):
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
