from PySide2 import QtWidgets
import package.gui as gui

app = QtWidgets.QApplication([])
window = gui.MainWindow()
window.show()
app.exec_()
