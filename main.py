import csv
from PyQt5 import uic, QtWidgets


def read_data():
    with open('users.csv', mode='r') as csv_file:
        writer = csv.reader(csv_file)

        data = login_window.lineEdit.text()
        
        for row in writer:
            if data in row:
                print(f"O usuario {data} já tem uma conta!")
            else:
                print("Usuario ainda não registrado.")
                login_window.close()
                register_window = uic.loadUi("register.ui")
                register_window.show()

def write_data():
    with open('users.csv', mode='w') as csv_file:
        fieldnames = ['user', 'password']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writerow({'user': login_window.lineEdit.text(), 'password': login_window.lineEdit_1.text()})


app = QtWidgets.QApplication([])
login_window = uic.loadUi("login.ui")
login_window.show()

login_window.pushButton.clicked.connect(read_data)

app.exec()
