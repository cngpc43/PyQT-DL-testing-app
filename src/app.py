from PyQt5 import QtWidgets, QtCore, QtGui, QtSql
from loginUI import Ui_Form
# from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sys

class myApp(QtWidgets.QWidget,Ui_Form): 
    def __init__(self):
        super(myApp,self).__init__()
        self.setupUi(self)
        self.openDB()
        self.pushButton.clicked.connect(self.checkUser)
    def openDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('db.sqlite')
        if not db.open():
            print("Cannot open database")
        self.query = QtSql.QSqlQuery()

    def checkUser(self):
        username1 = self.lineEdit.text()
        password1 = self.lineEdit_2.text()
        print(username1, password1)
        self.query.exec_("select * from users where username = '%s' and password = '%s'" % (username1, password1))
        self.query.first()
        if self.query.value("username") != None and self.query.value("password") != None:
            print("Login successfully")
        else:
            print("Login failed")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = myApp()
    Form.show()
    sys.exit(app.exec_())