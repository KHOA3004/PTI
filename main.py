from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,QLineEdit, QLabel, QDialog
from PyQt6 import uic
from PyQt6.QtCore import QDate, QDateTime
import sys

from model.games import Game, ListGame
from model.accounts import Account, ListAccounts
from ui_py.ui_homedashboardform import Ui_MainWindow

class AddDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("./ui/adddialog.ui", self)
        self.btnBox.accepted.connect(self.addMovie)
    def addMovie(self):
        self.l = ListGame()
        self.l.add_games(Game("Null",self.lineEdit_NameGame.text(),self.lineEdit_ReleaseDate.text(),self.lineEdit_ScoreRank.text(),self.lineEdit_URL.text()))
        home.callAfterInit()
        self.close()

class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.oldGame = None
        uic.loadUi("./ui/editdialog.ui",self)
        self.btnBox.accepted.connect(self.setNewGame)

    def setOldGame(self, game:Game):
        # Dat Ten Objects cho dung
        self.oldGame = game
        self.lineEdit_NewNameGame.setText(game.getName())
        date_str = game.getDate()
        date = QDate.fromString(date_str, "yyyy-MM-dd")
        self.lineEdit_NewReleaseDate.setDate(date)
        self.lineEdit_ScoreRanking.setText(game.getScore())
        self.lineEdit_EditURL.setText(game.getLink())

    def setNewGame(self):
        # Xoa Movie cu
        self.l = ListGame()
        self.l.delete_games_by_name(self.oldGame.getName())
        # Them Movie Moi
        self.l.add_games(Game("Null", self.lineEdit_NewNameGame.text(), self.lineEdit_NewReleaseDate.text(), self.lineEdit_ScoreRanking.text(), self.lineEdit_EditURL.text()))
        home.callAfterInit()
        self.close()

    def exit(self):
        self.close()

class HomeMenuDashboard(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.callAfterInit()
        self.btnDelete.clicked.connect(self.deleteGame)
        self.btnEditDialog.clicked.connect(self.showEditDialog)
        self.btnAddDialog.clicked.connect(self.showAddDialog)
    def deleteGame(self):
        nameGameDetete = self.test.currentItem().text()
        self.test.takeItem(self.test.currentRow())
        self.l.delete_games_by_name(nameGameDetete)
        self.callAfterInit()
    def showAddDialog(self):
        add.show()
    def showEditDialog(self):
        if self.test.currentRow():
            edit.show()
            edit.setOldGame(self.l.getGameByName(self.test.currentItem().text()))
        
    def callAfterInit(self):
        self.l = ListGame()
        # thêm tất cả tên của đối tương Movie vào List
        self.test.clear()
        for mov in self.l.getAllGames():
            self.test.addItem(mov.getName())
        

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home = HomeMenuDashboard()
    add = AddDialog()
    edit = EditDialog()
    home.show()
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
#     sys.exit(app.exec())