import csv
from PyQt5 import uic, QtWidgets


# this is the main object
class Account:
    def __init__(self):
        app = QtWidgets.QApplication([])
        # it opens login UI when program starts
        self.loadLogin()
        app.exec()
    
    def loadRegister(self):
        self.register_window = uic.loadUi("register.ui")
        self.register_window.show()
        # the register function calls a function that writes the data
        self.register_window.pushButton.clicked.connect(self.writeData)

    def loadLogin(self):
        self.login_window = uic.loadUi("login.ui")
        self.login_window.show()
        # the login function calls a function that reads the data
        self.login_window.pushButton.clicked.connect(self.readData)
    
    # function that read
    def readData(self):
        with open('users.csv', mode='r') as csv_file:
            writer = csv.reader(csv_file)

            data_name = self.login_window.lineEdit.text()

            for row in writer:
                try:
                    if data_name in row[0]:
                        print(f"Seja bem vindo!, Sr.{data_name.upper()}!")
                except:
                    print("Usuario ainda não foi registrado.")
                    self.loadRegister()
    
    # function that write
    def writeData(self):
        with open('users.csv', mode='w') as csv_file:
            fieldnames = ['user', 'password']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
            writer.writerow({'user': self.register_window.lineEdit.text(), 'password': self.register_window.lineEdit_1.text()})

                    
user = Account()