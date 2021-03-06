from PySide2 import QtWidgets

import package.pokeapi as pokeapi
import package.calculate as calculate
import package.gui as gui

app = QtWidgets.QApplication([])
window = gui.MainWindow()
window.show()
app.exec_()

#if a >= 255:
#    print(f"You have a 100% chance to capture {pokemon}!")
#else:
#    p = calculate.calculate_capture_chance(a)
#    print(f"You have, approximately, a {p * 100}% chance to capture {pokemon} per ball with the chosen ball.")