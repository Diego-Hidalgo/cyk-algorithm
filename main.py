from PyQt5 import QtWidgets
from src.controller.GrammarController import GrammarController
import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = GrammarController()
    window.show()
    sys.exit(app.exec_())
