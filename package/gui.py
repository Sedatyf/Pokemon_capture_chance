from PySide2 import QtWidgets, QtCore, QtGui
import platform
import package.pokeapi as pokeapi
import package.calculate as calculate

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Calculate Pokemon capture chance")
        self.setMinimumSize(355, 320)
        self.setWindowIcon(QtGui.QIcon("img/balls/pokeball.png"))

        self.layout = QtWidgets.QGridLayout(self)

        self.createNamePokemon(self.layout)
        self.createLevel(self.layout)
        self.createSliderHP(self.layout)
        self.createBallGroup(self.layout)
        self.createStatusGroup(self.layout)
        self.createCalculateButton(self.layout)
        self.createResultBox(self.layout)

        self.connectWidgets()


    def createNamePokemon(self, layout_variable):
        self.label_pokemon = QtWidgets.QLabel("What's the Pokemon's name?")

        self.input_pokemon_name = QtWidgets.QLineEdit()
        self.input_pokemon_name.setPlaceholderText("Enter here the Pokemon's name (French version)")

        layout_variable.addWidget(self.label_pokemon, 0, 0, 1, 6)
        layout_variable.addWidget(self.input_pokemon_name, 1, 0, 1, 6)


    def createLevel(self, layout_variable):
        # SPINBOX ??
        self.label_level = QtWidgets.QLabel("What's the Pokemon's level?")

        self.input_pokemon_level = QtWidgets.QSpinBox()
        
        layout_variable.addWidget(self.label_level, 2, 0, 1, 6)
        layout_variable.addWidget(self.input_pokemon_level, 3, 0, 1, 1)


    def createSliderHP(self, layout_variable):
        self.label_hp = QtWidgets.QLabel("How much HP does the Pokemon have?")

        self.slider_current_hp = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.slider_current_hp.setMaximum(100)
        self.slider_current_hp.setMinimum(0)
        self.slider_current_hp.setValue(100)
        self.slider_current_hp.setStyleSheet("selection-background-color: rgb(0, 255, 0)")

        layout_variable.addWidget(self.label_hp, 4, 0, 1, 6)
        layout_variable.addWidget(self.slider_current_hp, 5, 0, 1, 6)


    def createBallGroup(self, layout_variable):
        self.bgroupBall = QtWidgets.QButtonGroup(self)

        self.label_ball = QtWidgets.QLabel("Which Pokeball will you use?")

        self.radio_pokeball = QtWidgets.QRadioButton()
        self.radio_superball = QtWidgets.QRadioButton()
        self.radio_hyperball = QtWidgets.QRadioButton()

        self.icon_pokeball = QtGui.QIcon("img/balls/pokeball.png")
        self.icon_superball = QtGui.QIcon("img/balls/superball.png")
        self.icon_hyperball = QtGui.QIcon("img/balls/hyperball.png")

        self.radio_pokeball.setIcon(self.icon_pokeball)
        self.radio_pokeball.setIconSize(QtCore.QSize(36, 36))
        self.radio_superball.setIcon(self.icon_superball)
        self.radio_superball.setIconSize(QtCore.QSize(36, 36))
        self.radio_hyperball.setIcon(self.icon_hyperball)
        self.radio_hyperball.setIconSize(QtCore.QSize(36, 36))

        self.radio_pokeball.setChecked(True)

        self.bgroupBall.addButton(self.radio_pokeball)
        self.bgroupBall.addButton(self.radio_superball)
        self.bgroupBall.addButton(self.radio_hyperball)

        self.bgroupBall.setId(self.radio_pokeball, 1)
        self.bgroupBall.setId(self.radio_superball, 2)
        self.bgroupBall.setId(self.radio_hyperball, 3)

        layout_variable.addWidget(self.label_ball, 6, 0, 1, 6)
        layout_variable.addWidget(self.radio_pokeball, 7, 0, 1, 1)
        layout_variable.addWidget(self.radio_superball, 7, 1, 1, 1)
        layout_variable.addWidget(self.radio_hyperball, 7, 2, 1, 1)
    

    def createStatusGroup(self, layout_variable):
        self.bgroupStatus = QtWidgets.QButtonGroup(self)

        self.label_status = QtWidgets.QLabel("Does the Pokemon suffer from a status?")

        self.radio_status_brn = QtWidgets.QRadioButton()
        self.radio_status_par = QtWidgets.QRadioButton()
        self.radio_status_psn = QtWidgets.QRadioButton()
        self.radio_status_frz = QtWidgets.QRadioButton()
        self.radio_status_slp = QtWidgets.QRadioButton()
        self.radio_status_none = QtWidgets.QRadioButton("None")

        self.icon_brn = QtGui.QIcon("img/status/status_brn.png")
        self.icon_par = QtGui.QIcon("img/status/status_par.png")
        self.icon_psn = QtGui.QIcon("img/status/status_psn.png")
        self.icon_frz = QtGui.QIcon("img/status/status_frz.png")
        self.icon_slp = QtGui.QIcon("img/status/status_slp.png")

        self.radio_status_brn.setIcon(self.icon_brn)
        self.radio_status_brn.setIconSize(QtCore.QSize(60, 24))
        self.radio_status_par.setIcon(self.icon_par)
        self.radio_status_par.setIconSize(QtCore.QSize(60, 24))
        self.radio_status_psn.setIcon(self.icon_psn)
        self.radio_status_psn.setIconSize(QtCore.QSize(60, 24))
        self.radio_status_frz.setIcon(self.icon_frz)
        self.radio_status_frz.setIconSize(QtCore.QSize(60, 24))
        self.radio_status_slp.setIcon(self.icon_slp)
        self.radio_status_slp.setIconSize(QtCore.QSize(60, 24))

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

        layout_variable.addWidget(self.label_status, 8, 0, 1, 6)
        layout_variable.addWidget(self.radio_status_brn, 9, 0, 1, 1)
        layout_variable.addWidget(self.radio_status_par, 9, 1, 1, 1)
        layout_variable.addWidget(self.radio_status_psn, 9, 2, 1, 1)
        layout_variable.addWidget(self.radio_status_frz, 10, 0, 1, 1)
        layout_variable.addWidget(self.radio_status_slp, 10, 1, 1, 1)
        layout_variable.addWidget(self.radio_status_none, 10, 2, 1, 1)


    def createCalculateButton(self, layout_variable):
        self.button_calculate = QtWidgets.QPushButton("Calculate")
        layout_variable.addWidget(self.button_calculate, 11, 0, 1, 6)


    def createResultBox(self, layout_variable):
        self.te_result = QtWidgets.QTextEdit()
        self.te_result.setReadOnly(True)
        self.te_result.setFixedHeight(50)

        layout_variable.addWidget(self.te_result, 12, 0, 1, 6)


    def connectWidgets(self):
        if platform.system() == "Linux":
            self.slider_current_hp.valueChanged.connect(self.changeColorHPLinux)
        elif platform.system() == "Windows":
            self.slider_current_hp.valueChanged.connect(self.changeColorHPWindows)
        self.button_calculate.clicked.connect(self.calculate)
    

    def changeColorHPLinux(self):
        color = ""
        if 50 <= self.slider_current_hp.value() <= 100:
            color = "rgb(0, 255, 0)"
        elif 20 <= self.slider_current_hp.value() < 50:
            color = "rgb(255, 153, 0)"
        elif 0 <= self.slider_current_hp.value() < 20:
            color = "rgb(255, 0, 0)"
        
        self.slider_current_hp.setStyleSheet(f"selection-background-color: {color}")

    def changeColorHPWindows(self):
        color = ""
        if 50 <= self.slider_current_hp.value() <= 100:
            color = "rgb(0, 255, 0)"
        elif 20 <= self.slider_current_hp.value() < 50:
            color = "rgb(255, 153, 0)"
        elif 0 <= self.slider_current_hp.value() < 20:
            color = "rgb(255, 0, 0)"

        style = """
            QSlider::groove:horizontal {
            border: 1px solid #999999;
            height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */
            background: """ + color + """
            margin: 2px 0;
            }

            QSlider::handle:horizontal {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
            border: 1px solid #5c5c5c;
            width: 18px;
            margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */
            border-radius: 3px;
            }"""
        
        self.slider_current_hp.setStyleSheet(style)


    def calculate(self):
        pokemon_name = self.input_pokemon_name.text()
        level = int(self.input_pokemon_level.text())
        radio_ball = self.bgroupBall.checkedId()
        radio_status = self.bgroupStatus.checkedId()
        current_hp = int(self.slider_current_hp.sliderPosition())

        ball = pokeapi.get_bonus_ball(radio_ball)
        status = pokeapi.get_bonus_status(radio_status)

        capture_rate = pokeapi.get_capture_rate(pokemon_name)
        base_hp = pokeapi.get_base_hp(pokemon_name)
        max_hp = calculate.calculate_max_hp(base_hp, level)
        current_hp = calculate.calculate_current_hp(current_hp, max_hp)
        a = calculate.calculate_a(current_hp, max_hp, capture_rate, ball, status)

        if a >= 255:
            self.te_result.setText(f"You have a 100% chance to capture {pokemon_name}!")
        else:
            p = calculate.calculate_capture_chance(a)
            self.te_result.setText(f"You have, approximately, a {p * 100}% chance to capture {pokemon_name} per ball with the chosen ball.")
