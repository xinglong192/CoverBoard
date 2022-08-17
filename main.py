import configparser
import os
import re
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent, QContextMenuEvent, QCursor, QAction, QPalette, QColor
from PySide6.QtWidgets import QMainWindow, QApplication, QMenu, QStyle, QColorDialog

from transparent_dialog import TransparentDialog
from ui_coverboard import Ui_CoverBoard

confFile = 'cbConf.ini'
con = configparser.ConfigParser()

cb_color_rgb = 'rgb(255,255,255)'  # 背景色 rgb
cb_transparent = '255'  # 透明度 0~255
cb_top = '0'  # 是否置顶

# 读取配置文件
if os.path.exists(confFile):
    con.read(confFile, 'utf-8')
    if con.has_section('base'):
        baseItems = dict(con.items('base'))
        if 'board_bg_color_rgb' in baseItems:
            # 读取背景色
            cb_color_rgb = baseItems.get('board_bg_color_rgb', 'rgb(255,255,255)')
        if 'board_transparent' in baseItems:
            # 读取透明度
            cb_transparent = baseItems.get('board_transparent', '255')
        if 'board_top' in baseItems:
            # 读取置顶状态
            cb_top = baseItems.get('board_top', '0')


def update_conf(sec: str, opt: str, val: str) -> None:
    """ 更新配置文件中键值 """
    if os.path.exists(confFile) and con.has_section(sec):
        con.read(confFile)
        con.set(sec, opt, val)
        con.write(open(file=confFile, mode='r+', encoding='utf8'))
        return
    con.add_section(sec)
    con.set(sec, opt, val)
    con.write(open(file=confFile, mode='a', encoding='utf8'))


class MainWindow(QMainWindow, Ui_CoverBoard):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.NoDropShadowWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.r_menu = None
        self.start_pos = None
        self.setupUi(self)
        self.mainRMen()
        self.__init_board_conf()

    def __init_board_conf(self):
        try:
            self.setWindowFlag(Qt.WindowStaysOnTopHint, cb_top == '1')
            self.setWindowOpacity(float(cb_transparent) / 255)
            t = re.findall(r'[a-zA-z]*\(?(\d*),(\d*),(\d*).*\)?', cb_color_rgb.replace(" ", ""))
            if t and t[0] and len(t[0]) >= 3:
                t = t[0]
                p = self.palette()
                p.setColor(QPalette.Window, QColor.fromRgb(int(t[0]), int(t[1]), int(t[2])))
                self.setPalette(p)
        except Exception as ignore:
            pass

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

    def closeEvent(self, event) -> None:
        try:
            c = self.palette().color(QPalette.Window).getRgb()
            update_conf('base', 'board_bg_color_rgb', f'rgb({c[0]},{c[1]},{c[2]})')
            update_conf('base', 'board_transparent', str(int(self.windowOpacity() * 255)))
            update_conf('base', 'board_top', '0' if (self.windowFlags() & Qt.WindowStaysOnTopHint) == 0 else '1')
        except Exception as ignore:
            pass
        super(MainWindow, self).closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
