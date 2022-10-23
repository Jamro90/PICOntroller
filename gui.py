from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QMainWindow, QToolBar, QDockWidget, QFrame, QToolButton, QComboBox
from PySide6.QtGui import Qt, QGuiApplication, QKeySequence, QIcon, QPixmap, QAction
from pad_control import Devices, Pad
import sys

def gui_start():
    print("gui działa")

# authorization code
class login_window(QWidget):
    def __init__(self):
        super().__init__()
        
        # window title & geometry
        self.setWindowTitle("Authentication")
        self.setGeometry(100, 100, 300, 200)
        
        # centering window
        qr = self.frameGeometry()
        cp = QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        # Widgets create & spcecify
        
        self.layout = QVBoxLayout(self)
        # general label & error message (hiden)
        self.start_label = QLabel("Authentication")
        self.alert_label = QLabel()
        self.alert_label.setAlignment(Qt.AlignCenter)
        # login widgets
        self.login_label = QLabel("Login: ")
        self.login_input = QLineEdit()

        # password widgets
        self.password_label = QLabel("Password: ")
        self.password_input = QLineEdit()
    
        # buttons
        self.accept_button = QPushButton("Login")
        self.exit_button = QPushButton("Exit")

        # widgets added to layout
        self.layout.addWidget(self.start_label)
        self.layout.addWidget(self.alert_label)
        self.layout.addWidget(self.login_label)
        self.layout.addWidget(self.login_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.accept_button)
        self.layout.addWidget(self.exit_button)
       
        # buttons connection
        self.accept_button.clicked.connect(self.check_login_password)
        self.exit_button.clicked.connect(sys.exit)

    def check_login_password(self, run_next):
        if self.login_input.text() == "admin" and self.password_input.text() == "pass":
            # hide loger
            self.hide()
            self.transform = MainWindow()
            self.transform.show()
            return self.transform
        else:
            # clear inputs & show error message
            self.login_input.clear()
            self.password_input.clear()
            self.alert_label.setText("<font color = red> Incorrect login or password</font>")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # class variables
        self.ip_adress = ""
        
        # variables of pad
        self.x_axis = 0
        self.y_axis = 0
        self.x_right_axis = 0
        self.y_right_axis = 0
        self.left_trigger = 0
        self.right_trigger = 0
        self.left_bumper = 0
        self.right_bumper = 0
        self.UP = 0
        self.DOWN = 0
        self.LEFT = 0
        self.RIGHT = 0
        self.Y_btn = 0
        self.A_btn = 0
        self.X_btn = 0
        self.B_btn = 0

        # window title & geometry
        self.setWindowTitle("Program Główny")
        self.setGeometry(100, 100, 800, 600)
        
        # centering window
        qr = self.frameGeometry()
        cp = QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # Menu settings
        
            # create & show menu 
        tool_bar = QToolBar()
        self.addToolBar(tool_bar)

            # add File page
        file_Menu = self.menuBar().addMenu("&File")

                # add to File page action open
        open_Action = QAction(QIcon.fromTheme("document-open"), "&Open", self, shortcut = QKeySequence.Open, triggered = lambda: print("open"))
        file_Menu.addAction(open_Action)

        file_Menu.addSeparator()

                # add to File page action exit
        exit_Action = QAction(QIcon.fromTheme("application-exit"), "E&xit", self, shortcut = "Escape", triggered = sys.exit)
        file_Menu.addAction(exit_Action)
        
            # add View page
        view_Menu = self.menuBar().addMenu("&View")

            # add Load data page
        load_data_Menu = self.menuBar().addMenu("Load data")

                # add to Load data action Text file
        text_file_Action = QAction(QIcon.fromTheme("text-x-generic"), "Text file", self)
        load_data_Menu.addAction(text_file_Action)

                # add to Load data action Json file
        json_file_Action = QAction(QIcon.fromTheme("text-x-scripts"), "Json file", self)
        load_data_Menu.addAction(json_file_Action)

                # add to Load data action Excel spreadsheet
        excel_Action = QAction(QIcon.fromTheme("x-office-spreadsheet"), "Excel spreadsheet", self)
        load_data_Menu.addAction(excel_Action)

            # add Help page
        help_Menu = self.menuBar().addMenu("&Help")

                # add to Help action Manual
        manual_Action = QAction(QPixmap("Icons/GitHub-Mark/PNG/GitHub-Mark-32px.png"), "Manual", self)
        help_Menu.addAction(manual_Action)

                # add to help action About
        about_Action = QAction(QIcon.fromTheme("help-about"), "About", self)
        help_Menu.addAction(about_Action)

        # make a popup toolbar button
        panels_Action = QToolButton()
        panels_Action.menu()
            # popup function
        panels_Action.setPopupMode(QToolButton.MenuButtonPopup)
        panels_Action.setText("Panels")
            # add to toolbar
        tool_bar.addWidget(panels_Action)
        
        # settings panels

            # position panel
        self.position_panel = QDockWidget("Position panel", self)
        self.position_panel.hide()
        
        self.position_panel_container = QFrame()
        self.position_panel_layout = QVBoxLayout()

        self.left_axis = QLabel("Left trigger")
        self.position_panel_layout.addWidget(self.left_axis)
        self.pad_axis_x = QLabel("pad axis X:\t" + str(self.x_axis))
        self.position_panel_layout.addWidget(self.pad_axis_x)
        self.pad_axis_y = QLabel("pad axis Y:\t" + str(self.y_axis))
        self.position_panel_layout.addWidget(self.pad_axis_y)
        
        self.right_axis = QLabel("Right trigger")
        self.position_panel_layout.addWidget(self.right_axis)
        self.pad_axis_right_x = QLabel("pad axis X:\t" + str(self.x_right_axis))
        self.position_panel_layout.addWidget(self.pad_axis_right_x)
        self.pad_axis_right_y = QLabel("pad axis Y:\t" + str(self.y_right_axis))
        self.position_panel_layout.addWidget(self.pad_axis_right_y)

        self.position_panel_container.setLayout(self.position_panel_layout)
        self.position_panel.setWidget(self.position_panel_container)

            # inputs panel
        self.inputs_panel = QDockWidget("Inputs panel", self)
        self.inputs_panel.hide()
        
        self.inputs_panel_container = QFrame()
        self.inputs_panel_layout = QVBoxLayout()

        self.buttons_label = QLabel("Buttons")
        self.inputs_panel_layout.addWidget(self.buttons_label)
        self.button_Y = QLabel("Y:\t" + str(self.Y_btn))
        self.inputs_panel_layout.addWidget(self.button_Y)
        self.button_A = QLabel("A:\t" + str(self.A_btn))
        self.inputs_panel_layout.addWidget(self.button_A)
        self.button_X = QLabel("X:\t" + str(self.X_btn))
        self.inputs_panel_layout.addWidget(self.button_X)
        self.button_B = QLabel("B:\t" + str(self.B_btn))
        self.inputs_panel_layout.addWidget(self.button_B)

        self.inputs_panel_container.setLayout(self.inputs_panel_layout)
        self.inputs_panel.setWidget(self.inputs_panel_container)

        # panels actions

            # position panel action (visible/not visible)
        position_panel_Action = self.position_panel.toggleViewAction()
        panels_Action.addAction(position_panel_Action)

            # input panel action (visible/not visible
        inputs_panel_Action = self.inputs_panel.toggleViewAction()
        panels_Action.addAction(inputs_panel_Action)
         
        # making a frame
        self.con = QFrame()
            # setting a layout for frame
        self.lay = QGridLayout()

            # adding layout to frame
        self.con.setLayout(self.lay)
            # seting a frame as a central widget of main window
        self.setCentralWidget(self.con)
   
        # IP devices settings

            # list of devices
        self.ip_host_label = QLabel("Host IP:")
        self.lay.addWidget(self.ip_host_label, 0, 0)
        self.ip_host_warrning = QLabel()
        self.lay.addWidget(self.ip_host_warrning, 0, 2)

        self.ip_client_label = QLabel("Client IP:")
        self.lay.addWidget(self.ip_client_label, 1, 0)
        self.ip_client_warrning = QLabel()
        self.lay.addWidget(self.ip_client_warrning, 1, 2)

        self.ip_client_combobox = QComboBox()
        self.lay.addWidget(self.ip_client_combobox, 1, 1)
        
        self.ip_host_warrning.setText("d")
        
      
        self.connection_button = QPushButton("Connect")
        self.lay.addWidget(self.connection_button, 4, 2)
        self.connection_button.clicked.connect(self.connect_devices)

        # Pad control

            # list of devices
        devs = Devices().list_of_devs
        
        self.pads_label = QLabel("Controller")
        self.devs_combobox = QComboBox()
        self.lay.addWidget(self.pads_label, 2, 0)
        self.lay.addWidget(self.devs_combobox, 2, 1)
        for dev in devs:
            self.devs_combobox.addItem(str(dev))
   
        self.pads_warrning = QLabel()
        self.lay.addWidget(self.pads_warrning, 2, 2)

    def connect_devices(self):
        
        if 1==2:
            self.ip_host_warrning.setPixmap(QPixmap("Icons/OK-1.svg"))
        else:
            self.ip_host_warrning.setPixmap(QPixmap("Icons/OK-2.svg"))

        if 1==1:
            self.ip_client_warrning.setPixmap(QPixmap("Icons/OK-1.svg"))
        else:
            self.ip_client_warning.setPixmap(QPixmap("Icons/OK-2.svg"))

        if 1==1:
            self.pads_warrning.setPixmap(QPixmap("Icons/OK-1.svg"))
        else:
            self.pads_warrning.setPixmap(QPixmap("Icons/OK-2.svg"))


def run_main():
    main = MainWindow()
    main.show()

# executing authentication process
def run_auth():
    app = QApplication(sys.argv)
    log = login_window()
    log.show()
    app.exit(app.exec())

    

