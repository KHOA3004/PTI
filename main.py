from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6 import uic
import sys

from model.accounts import Account, ListAccounts
from model.games import Game,ListGame
from ui_py.ui_homedashboardform import Ui_MainWindow

class HomeMenuDashBoard(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.callAfterInit()
    def callAfterInit(self):
        self.l = ListGame()
        for mov in self.l.getAllGames():
            self.test.addItem(mov.getName())
        self.test.addItem("Object1")
        self.test.addItems(["Object2",'Object3'])



class LoginView(QMainWindow):
    def __init__(self) :
        super().__init__()
        uic.loadUi("./ui/LoginPage.ui", self)
        self.l = ListAccounts()
        self.btnLogin.clicked .connect(self.checklogin)
    def checklogin(self):
        if self.l.checkAccounts(Account(self.txtUserName.text(), self.txtPassWord.text(),)) == True:
            #hien trang chu
            self.close()
        else:
            print("Sai Tk hoac MK")

class SignInView(QMainWindow):
    def __init__(self):
        self.l = ListAccounts()
        self.btnSignIn.connect(self.addAccount)
    def addAccount(self):
        self.l.addAccount(Account(self.txtUserName.text(), self.txtPassWord.text()))
        

# import pygame 
# pygame. init()
# my_sound = pygame. mixer. Sound('D:/BiBongBenh/Downloads/Nhạc nền vui của Độ mixi.mp3')



# l.showAllAccount()

if __name__ == "__main__":
    # my_sound.play()
    app = QApplication(sys.argv)
    home = HomeMenuDashBoard()
    home.show()# login = LoginView()
    # login.show()
    app.exec()





# from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
# from PyQt6 import uic
# import sys

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("ui/main_window.ui", self)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())\