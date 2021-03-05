from PySide2 import QtWidgets, QtCore

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Calculate Pokemon capture chance")
        self.setMinimumSize(355, 320)

        layout = QtWidgets.QGridLayout(self)

        p_name = self.createNamePokemon(layout)

        self.createSliderHP(layout)

        self.createBallGroup(layout)

        self.createStatusGroup(layout)

        self.createCalculateButton(layout)

        self.createResultBox(layout)


    def createNamePokemon(self, layout_variable):
        label_pokemon = QtWidgets.QLabel("What's the Pokemon name?")

        input_pokemon_name = QtWidgets.QLineEdit()
        input_pokemon_name.setPlaceholderText("Enter here the Pokemon name (French version)")
        pokemon_name = input_pokemon_name.text()

        layout_variable.addWidget(label_pokemon, 0, 0, 1, 6)
        layout_variable.addWidget(input_pokemon_name, 1, 0, 1, 6)

        return pokemon_name


    def createSliderHP(self, layout_variable):
        label_hp = QtWidgets.QLabel("How much HP does the Pokemon have?")

        slider_current_hp = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        slider_current_hp.setMaximum(100)
        slider_current_hp.setMinimum(0)
        slider_current_hp.setValue(100)

        layout_variable.addWidget(label_hp, 2, 0, 1, 6)
        layout_variable.addWidget(slider_current_hp, 3, 0, 1, 6)


    def createBallGroup(self, layout_variable):
        bgroup = QtWidgets.QButtonGroup(self)

        label_ball = QtWidgets.QLabel("What Pokeball will you use?")

        radio_pokeball = QtWidgets.QRadioButton("Poke Ball")
        radio_superball = QtWidgets.QRadioButton("Super Ball")
        radio_hyperball = QtWidgets.QRadioButton("Hyper Ball")

        radio_pokeball.setChecked(True)

        bgroup.addButton(radio_pokeball)
        bgroup.addButton(radio_superball)
        bgroup.addButton(radio_hyperball)

        layout_variable.addWidget(label_ball, 4, 0, 1, 6)
        layout_variable.addWidget(radio_pokeball, 5, 0, 1, 1)
        layout_variable.addWidget(radio_superball, 5, 1, 1, 1)
        layout_variable.addWidget(radio_hyperball, 5, 2, 1, 1)
    

    def createStatusGroup(self, layout_variable):
        bgroup = QtWidgets.QButtonGroup(self)

        label_status = QtWidgets.QLabel("Does the Pokemon suffor from a status?")

        radio_status_brn = QtWidgets.QRadioButton("BRN")
        radio_status_par = QtWidgets.QRadioButton("PAR")
        radio_status_psn = QtWidgets.QRadioButton("PSN")
        radio_status_frz = QtWidgets.QRadioButton("FRZ")
        radio_status_slp = QtWidgets.QRadioButton("SLP")
        radio_status_none = QtWidgets.QRadioButton("None")

        radio_status_none.setChecked(True)

        bgroup.addButton(radio_status_brn)
        bgroup.addButton(radio_status_par)
        bgroup.addButton(radio_status_psn)
        bgroup.addButton(radio_status_frz)
        bgroup.addButton(radio_status_slp)
        bgroup.addButton(radio_status_none)

        layout_variable.addWidget(label_status, 6, 0, 1, 6)
        layout_variable.addWidget(radio_status_brn, 7, 0, 1, 1)
        layout_variable.addWidget(radio_status_par, 7, 1, 1, 1)
        layout_variable.addWidget(radio_status_psn, 7, 2, 1, 1)
        layout_variable.addWidget(radio_status_frz, 8, 0, 1, 1)
        layout_variable.addWidget(radio_status_slp, 8, 1, 1, 1)
        layout_variable.addWidget(radio_status_none, 8, 2, 1, 1)


    def createCalculateButton(self, layout_variable):
        button_calculate = QtWidgets.QPushButton("Calculate")
        layout_variable.addWidget(button_calculate, 9, 0, 1, 6)


    def createResultBox(self, layout_variable):
        label_result = QtWidgets.QLabel("Result")
        le_result = QtWidgets.QLineEdit()
        le_result.setReadOnly(True)

        layout_variable.addWidget(label_result, 10, 0, 1, 6)
        layout_variable.addWidget(le_result, 11, 0, 1, 6)


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec_()