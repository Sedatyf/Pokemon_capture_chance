from PySide2 import QtWidgets, QtCore
import package.pokeapi as pokeapi

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Calculate Pokemon capture chance")
        self.setMinimumSize(355, 320)

        self.layout = QtWidgets.QGridLayout(self)

        self.createNamePokemon(self.layout)
        self.createSliderHP(self.layout)
        self.createBallGroup(self.layout)
        self.createStatusGroup(self.layout)
        self.createCalculateButton(self.layout)
        self.createResultBox(self.layout)

        self.connectCalculateButton()


    def createNamePokemon(self, layout_variable):
        self.label_pokemon = QtWidgets.QLabel("What's the Pokemon name?")

        self.input_pokemon_name = QtWidgets.QLineEdit()
        self.input_pokemon_name.setPlaceholderText("Enter here the Pokemon name (French version)")

        layout_variable.addWidget(self.label_pokemon, 0, 0, 1, 6)
        layout_variable.addWidget(self.input_pokemon_name, 1, 0, 1, 6)


    def createSliderHP(self, layout_variable):
        self.label_hp = QtWidgets.QLabel("How much HP does the Pokemon have?")

        self.slider_current_hp = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.slider_current_hp.setMaximum(100)
        self.slider_current_hp.setMinimum(0)
        self.slider_current_hp.setValue(100)

        layout_variable.addWidget(self.label_hp, 2, 0, 1, 6)
        layout_variable.addWidget(self.slider_current_hp, 3, 0, 1, 6)


    def createBallGroup(self, layout_variable):
        self.bgroupBall = QtWidgets.QButtonGroup(self)

        self.label_ball = QtWidgets.QLabel("What Pokeball will you use?")

        self.radio_pokeball = QtWidgets.QRadioButton("Poke Ball")
        self.radio_superball = QtWidgets.QRadioButton("Super Ball")
        self.radio_hyperball = QtWidgets.QRadioButton("Hyper Ball")

        self.radio_pokeball.setChecked(True)

        self.bgroupBall.addButton(self.radio_pokeball)
        self.bgroupBall.addButton(self.radio_superball)
        self.bgroupBall.addButton(self.radio_hyperball)

        self.bgroupBall.setId(self.radio_pokeball, 1)
        self.bgroupBall.setId(self.radio_superball, 2)
        self.bgroupBall.setId(self.radio_hyperball, 3)

        layout_variable.addWidget(self.label_ball, 4, 0, 1, 6)
        layout_variable.addWidget(self.radio_pokeball, 5, 0, 1, 1)
        layout_variable.addWidget(self.radio_superball, 5, 1, 1, 1)
        layout_variable.addWidget(self.radio_hyperball, 5, 2, 1, 1)
    

    def createStatusGroup(self, layout_variable):
        self.bgroupStatus = QtWidgets.QButtonGroup(self)

        self.label_status = QtWidgets.QLabel("Does the Pokemon suffor from a status?")

        self.radio_status_brn = QtWidgets.QRadioButton("BRN")
        self.radio_status_par = QtWidgets.QRadioButton("PAR")
        self.radio_status_psn = QtWidgets.QRadioButton("PSN")
        self.radio_status_frz = QtWidgets.QRadioButton("FRZ")
        self.radio_status_slp = QtWidgets.QRadioButton("SLP")
        self.radio_status_none = QtWidgets.QRadioButton("None")

        self.radio_status_none.setChecked(True)

        self.bgroupStatus.addButton(self.radio_status_brn)
        self.bgroupStatus.addButton(self.radio_status_par)
        self.bgroupStatus.addButton(self.radio_status_psn)
        self.bgroupStatus.addButton(self.radio_status_frz)
        self.bgroupStatus.addButton(self.radio_status_slp)
        self.bgroupStatus.addButton(self.radio_status_none)

        self.bgroupStatus.setId(self.radio_status_brn, 1)
        self.bgroupStatus.setId(self.radio_status_par, 2)
        self.bgroupStatus.setId(self.radio_status_psn, 3)
        self.bgroupStatus.setId(self.radio_status_frz, 4)
        self.bgroupStatus.setId(self.radio_status_slp, 5)
        self.bgroupStatus.setId(self.radio_status_none, 6)

        layout_variable.addWidget(self.label_status, 6, 0, 1, 6)
        layout_variable.addWidget(self.radio_status_brn, 7, 0, 1, 1)
        layout_variable.addWidget(self.radio_status_par, 7, 1, 1, 1)
        layout_variable.addWidget(self.radio_status_psn, 7, 2, 1, 1)
        layout_variable.addWidget(self.radio_status_frz, 8, 0, 1, 1)
        layout_variable.addWidget(self.radio_status_slp, 8, 1, 1, 1)
        layout_variable.addWidget(self.radio_status_none, 8, 2, 1, 1)


    def createCalculateButton(self, layout_variable):
        self.button_calculate = QtWidgets.QPushButton("Calculate")
        layout_variable.addWidget(self.button_calculate, 9, 0, 1, 6)


    def createResultBox(self, layout_variable):
        self.label_result = QtWidgets.QLabel("Result")
        self.le_result = QtWidgets.QLineEdit()
        self.le_result.setReadOnly(True)

        layout_variable.addWidget(self.label_result, 10, 0, 1, 6)
        layout_variable.addWidget(self.le_result, 11, 0, 1, 6)


    def connectCalculateButton(self):
        self.button_calculate.clicked.connect(self.calculate)
    

    def calculate(self):
        pokemon_name = self.input_pokemon_name.text()
        capture_rate = pokeapi.get_capture_rate(pokemon_name)
        ball = self.bgroupBall.checkedId()
        status = self.bgroupStatus.checkedId()
        current_hp = self.slider_current_hp.sliderPosition()
        print(current_hp)

