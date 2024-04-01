from PyQt5.QtWidgets import *

import sys
from autorisation import Ui_MainWindow
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())