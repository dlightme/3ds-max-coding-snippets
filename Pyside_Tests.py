import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QAction
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec_(e.globalPos())

def main():
    if not QApplication.instance():
            app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    window = MainWindow()
    window.show()
    
    app.exec_()
    
if __name__ == "__main__": 
    main()