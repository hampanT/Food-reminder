
import json
from PyQt5.QtWidgets import *
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtgui
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QFont, QFontDatabase


data = {
    "food_items": [
        {"name": "Hejsan", "expiry_date": "2023-08-31"},
        {"name": "Banana", "expiry_date": "2023-08-28"}
    ]
}

def get_input():
    user_data = {
        "name": input("Enter your name: "),
        "age": int(input("Enter your age: "))
    }
    return user_data


#filename = "user_data.json"

#user_input = get_input()

#with open(filename, 'w') as json_file:
    #json.dump(user_input, json_file, indent=4)

#with open(filename, 'r') as json_file:
    #loaded_data = json.load(json_file)

#print(loaded_data)




class Window(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #program title
        self.setWindowTitle("King ass project")
        self.setGeometry(100, 100, 800, 600)

        #bakgrundsbild
        bg_image = qtgui.QPixmap("spaghetti.jpg")


        palette = qtgui.QPalette()
        palette.setBrush(qtgui.QPalette.Window, qtgui.QBrush(bg_image.scaled(self.size(), QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)))
        self.setPalette(palette)

        #set layout
        self.setLayout(qtw.QVBoxLayout())
        center_layout = qtw.QHBoxLayout()
        center_layout.addStretch(1)

        #Create a label
        my_label = qtw.QLabel("Food saver TM")
        self.layout().addWidget(my_label)

        age_label = qtw.QLabel("")
        age_label.setFont(qtgui.QFont("", 20))
        age_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) #detta sätter label i mitten
        age_label.setStyleSheet("color: white")
        self.layout().addWidget(age_label)

        my_label.setStyleSheet("color: white")

        #ändra font
        my_label.setFont(qtgui.QFont("", 20))
        my_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) #detta sätter label i mitten

        #Skapa en entry box
        name_entry = qtw.QLineEdit()
        name_entry.setObjectName("name_field")
        name_entry.setText("Enter your name")
        self.layout().addWidget(name_entry)

        age_entry = qtw.QLineEdit()
        age_entry.setObjectName("")
        age_entry.setText("Enter your age")
        self.layout().addWidget(age_entry)

        #skapa en knapp
        add_item = qtw.QPushButton("New food object", clicked = lambda: press_it())
        button_icon = QIcon("plus.svg") #en plus-ikon för knappen
        add_item.setIcon(button_icon)
        self.layout().addWidget(add_item)
        add_item.setStyleSheet("background-color: #557A46; padding-right: 100px;")


        custom_font = QFontDatabase.addApplicationFont("Montserrat-SemiBold.ttf")
        custom_font = QFont()
        #custom_font.setBold(True)
        add_item.setFont(QFont("Montserrat", 20))


        self.show()

        def press_it():
            my_label.setText(f"Hello {name_entry.text()}")
            age_label.setText(f"Hello {age_entry.text()}")
            #rensa entry boxen
            name_entry.setText("")

            #så vad jag vill göra är att det som anvä

app = qtw.QApplication([])
mw = Window()

#run the shit
app.exec_()
