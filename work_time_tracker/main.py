import sys

from PySide6 import QtWidgets
from ui.main_window import WorkTimerApp


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WorkTimerApp()
    window.show()
    app.exec()