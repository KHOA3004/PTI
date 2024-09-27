from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,QLineEdit, QLabel, QDialog,QMessageBox
from PyQt6 import uic,QtCore,QtGui,QtWidgets
from PyQt6.QtCore import QDate, QDateTime
import sys
import os
from model.games import Game, ListGame
from model.accounts import Account, ListAccounts
from ui_py.ui_sortingpage import Ui_Sorting
from ui_py.ui_Library import Ui_Library
from ui_py.ui_homedashboardform import Ui_MainWindow
from AI.listen_and_speak import speech_to_text

class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/LoginPage.ui",self) # Load Giao diện từ file .ui
        ListAcc = ListAccounts()

        # ====== Kết nối sự kiện ở đây
        self.btnLogin.clicked.connect(self.checkLogin)
        self.pushButton_createAccount.clicked.connect(self.showSignupPage)
    def showSignupPage(self):
        signupPage.show()  # Hiển thị trang đăng ký
        self.close()       # Ẩn đi trang đăng nhập
    # Hàm kiểm tra đăng nhập
    def checkLogin(self):

       print(ListAcc.checkAccounts(Account(self.txtUserName.text(), self.txtPassWord.text(),)))
       print(self.txtUserName.text() , self.txtPassWord.text() ) 
       if ListAcc.checkAccounts(Account(self.txtUserName.text(), self.txtPassWord.text(),)) == True:
           home.show()
           self.close()

               

class SigninPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/SigninPage.ui",self) 
        
               
              # ====== Kết nối sự kiện ở đây
        self.pushButton_goLogin.clicked.connect(self.showLoginPage)
        self.btn_SignIn.clicked.connect(self.registerAccount)
    def showLoginPage(self):
        loginPage.show()  # Hiển thị trang đăng nhập
        self.close()      # Ẩn đi trang đăng ký
 # Hàm đăng ký tài khoản
    def registerAccount(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        confirmPassword = self.lineEdit_confirm_password_.text()
    
        if not username or not password or not confirmPassword:
            return

        if password != confirmPassword:
            return

        ListAcc.addAccount(Account(username,password))
        ListAcc.saveAllAccounts()
     # Hàm lưu tài khoản vào file users.txt
    def saveAccount(self, username, password):
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                for line in file:
                    stored_username, _ = line.strip().split(",")
                    if username == stored_username:
                        return False  # Tài khoản đã tồn tại

        with open("users.txt", "a") as file:
            file.write(f"{username},{password}\n")
        return True
    

class AddDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("./ui/adddialog.ui", self)
        self.btnBox.accepted.connect(self.addGame)
        self.btn_Browse.clicked.connect(self.browseImage)
    def browseImage(self):
        filePath,_= QtWidgets.QFileDialog.getOpenFileName(self,"Select an Image", "","Image Files(*.png *.jpg *.jpeg *.bmp)")
        if filePath:
            self.txtImage.setText(filePath)

    def addGame(self):
        self.l = ListGame()
        self.l.add_games(Game("Null",self.lineEdit_NameGame.text(),self.lineEdit_ReleaseDate.text(),self.lineEdit_ScoreRank.text(),self.lineEdit_URL.text(),self.txtImage.text(),self.lineEdit_Trailer.text()))
        home.callAfterInit()
        library.loadDataObjects()
        self.close()

class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.oldGame = None
        uic.loadUi("./ui/editdialog.ui",self)
        self.btnBox.accepted.connect(self.setNewGame)
        self.btn_Browse.clicked.connect(self.browseImage)

    def browseImage(self):
            filePath,_= QtWidgets.QFileDialog.getOpenFileName(self,"Select an Image", "","Image Files(*.png *.jpg *.jpeg *.bmp)")
            if filePath:
                self.txtImage.setText(filePath)

    def setOldGame(self, game:Game):
        # Dat Ten Objects cho dung
        self.oldGame = game
        self.lineEdit_NewNameGame.setText(game.getName())
        date_str = game.getDate()
        date = QDate.fromString(date_str, "yyyy-MM-dd")
        self.lineEdit_NewReleaseDate.setDate(date)
        self.lineEdit_ScoreRanking.setText(game.getScore())
        self.txtImage.setText(game.getImg())
        self.lineEdit_EditURL.setText(game.getLink())
        self.lineEdit_Trailer.setText(game.getLinkTrailer())

    def setNewGame(self):
        # Xoa Movie cu
        self.l = ListGame()
        self.l.delete_games_by_name(self.oldGame.getName())
        # Them Movie Moi
        self.l.add_games(Game("Null", self.lineEdit_NewNameGame.text(), self.lineEdit_NewReleaseDate.text(), self.lineEdit_ScoreRanking.text(), self.lineEdit_EditURL.text(),self.txtImage.text(), self.lineEdit_Trailer.text()))
        home.callAfterInit()
        library.loadDataObjects()
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
        self.btnSearch.clicked.connect(self.searchGame)
        self.btn_GAMES.clicked.connect(self.showGames)
        self.btn_INTRO.clicked.connect(self.showIntro)
        self.btn_LOGOUT.clicked.connect(self.showLogout)
        self.btnVoice.clicked.connect(self.searchGameByVoice)  
    def showGames(self):
        library.show()
        self.close()

    def showIntro(self):
        intro.show()
        self.close()


    def showLogout(self):
        loginPage.show()
        self.close()
    
    def searchGameByVoice(self):
        valueSearch = speech_to_text()
        dataSearch = self.l.searchGameaByName(valueSearch)
        self.test.clear()
        for mov in dataSearch:
            self.test.addItem(mov.getName())
    def searchGame(self):
        valueSearch = self.txtValueSearch.text()
        dataSearch = self.l.searchGameaByName(valueSearch)
        self.test.clear()
        for mov in dataSearch:
            self.test.addItem(mov.getName())
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

        
import webbrowser, json
class Library(QMainWindow,Ui_Library):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.l = ListGame()
        self.loadDataObjects()
        self.callAfterInit()
        self.list_game.itemDoubleClicked.connect(self.showInfoGames)
        self.btn_Home.clicked.connect(self.showHome)
        self.btnInstall.clicked.connect(self.openlinkInstall)
        self.pushButton_5.clicked.connect(self.openlinktrailer)
        self.btn_ADMIN.clicked.connect(self.showAdmin)
        self.btn_INTRO.clicked.connect(self.showIntro)
        self.btn_LOGOUT.clicked.connect(self.showLogout)
        self.pushButton_3.clicked.connect(self.searchGame)
        self.btnVoice.clicked.connect(self.searchGameByVoice)
        self.pushButton_2.clicked.connect(self.sort)
        self.type_sort = "name"
        
    
    def sort(self):
        self.x = ListGame()
        # clear value into list Widget
        self.list_game.clear()
        if self.type_sort == "name":
            self.x.sortByName()
            self.type_sort = "score"
        elif self.type_sort == "score":
            self.x.sortByScore()
            self.type_sort = "date"
        elif self.type_sort == "date":
            self.x.sortByDate()
            self.type_sort = "name"    
        # add Items
        for game in self.x.getAllGames():
            self.list_game.addItem(game.getName())


    def openlinktrailer(self):
        self.stackedWidget.setCurrentIndex(1)
        namegame = self.list_game.currentItem().text()
        game = self.l.getGameByName(namegame)
        game.open_trailer()

    def openlinkInstall(self):
        self.stackedWidget.setCurrentIndex(1)
        namegame = self.list_game.currentItem().text()
        game = self.l.getGameByName(namegame)
        game.open_game()

    def showInfoGames(self):
        self.stackedWidget.setCurrentIndex(1)
        namegame = self.list_game.currentItem().text()
        game = self.l.getGameByName(namegame)
        # doi hinh
        self.label_8.setPixmap(QtGui.QPixmap(game.getImg()))
        # doi ten game
        self.btnNameGame.setText(game.getName())
                               
    def showHome(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def showAdmin(self):
        home.show()
        self.close()

    def showIntro(self):
        intro.show()
        self.close()


    def showLogout(self):
        loginPage.show()
        self.close()
    
    def searchGameByVoice(self):
        valueSearch = speech_to_text()
        dataSearch = self.l.searchGameaByName(valueSearch)
        self.list_game.clear()
        for mov in dataSearch:
            self.list_game.addItem(mov.getName())
    def searchGame(self):
        valueSearch = self.txtValueSearch.text()
        dataSearch = self.l.searchGameaByName(valueSearch)
        self.list_game.clear()
        for mov in dataSearch:
            self.list_game.addItem(mov.getName())
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
        self.list_game.clear()
        for game in self.l.getAllGames():
            self.list_game.addItem(game.getName())
    
    def loadDataObjects(self):
        self.setupUi(self)
        self.l = ListGame()
        self.callAfterInit()
        self.list_game.itemDoubleClicked.connect(self.showInfoGames)
        self.btn_Home.clicked.connect(self.showHome)
        self.btnInstall.clicked.connect(self.openlinkInstall)
        self.pushButton_5.clicked.connect(self.openlinktrailer)
        self.btn_ADMIN.clicked.connect(self.showAdmin)
        self.btn_INTRO.clicked.connect(self.showIntro)
        self.btn_LOGOUT.clicked.connect(self.showLogout)
        self.pushButton_3.clicked.connect(self.searchGame)
        self.btnVoice.clicked.connect(self.searchGameByVoice)
        self.pushButton_2.clicked.connect(self.sort)
        self.type_sort = "name"

        for x in self.l.getAllGames():
            self.widget_3 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_3)
            self.widget_3.setMinimumSize(QtCore.QSize(435, 636))
            self.widget_3.setMaximumSize(QtCore.QSize(435, 636))
            self.widget_3.setObjectName("widget_3")
            self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.widget_4 = QtWidgets.QWidget(parent=self.widget_3)
            self.widget_4.setObjectName("widget_4")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.label_2 = QtWidgets.QLabel(parent=self.widget_4)
            self.label_2.setMaximumSize(QtCore.QSize(300, 450))
            self.label_2.setText("")
            self.label_2.setPixmap(QtGui.QPixmap(x.getImg()))
            self.label_2.setScaledContents(True)
            self.label_2.setObjectName("label_2")
            self.horizontalLayout_2.addWidget(self.label_2)
            self.verticalLayout_2.addWidget(self.widget_4)
            self.widget_7 = QtWidgets.QWidget(parent=self.widget_3)
            self.widget_7.setObjectName("widget_7")
            self.label_3 = QtWidgets.QLabel(parent=self.widget_7)
            self.label_3.setGeometry(QtCore.QRect(60, 10, 191, 21))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.label_3.setFont(font)
            self.label_3.setStyleSheet("color: rgb(175, 175, 162);")
            self.label_3.setObjectName("label_3")
            self.label_3.setText(x.getName())
            self.verticalLayout_2.addWidget(self.widget_7)
            self.widget_6 = QtWidgets.QWidget(parent=self.widget_3)
            self.widget_6.setObjectName("widget_6")
            self.widget_5 = QtWidgets.QWidget(parent=self.widget_6)
            self.widget_5.setGeometry(QtCore.QRect(-10, 80, 383, 127))
            self.widget_5.setObjectName("widget_5")
            self.label_4 = QtWidgets.QLabel(parent=self.widget_6)
            self.label_4.setGeometry(QtCore.QRect(100, 10, 191, 21))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.label_4.setFont(font)
            self.label_4.setStyleSheet("color: rgb(175, 175, 162);")
            self.label_4.setObjectName("label_4")
            self.label_4.setText(str("Score:" + str(x.getScore()) +"/10"))
            self.verticalLayout_2.addWidget(self.widget_6)
            self.horizontalLayout.addWidget(self.widget_3)

class SortingPage(QMainWindow,Ui_Sorting):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.l = ListGame()
        self.loadDataObjects()
        self.btn_ADMIN.clicked.connect(self.showAdmin)
        self.btn_INTRO.clicked.connect(self.showIntro)
        self.btn_LOGOUT.clicked.connect(self.showLogout)
    def loadDataObjects(self):
        self.setupUi(self)
        self.l = ListGame()
        self.btn_ADMIN.clicked.connect(self.showAdmin)
        self.btn_INTRO.clicked.connect(self.showIntro)
        self.btn_LOGOUT.clicked.connect(self.showLogout)
        for x in self.l.getAllGames():
            self.widget_2 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
            self.widget_2.setMinimumSize(QtCore.QSize(450, 646))
            self.widget_2.setObjectName("widget_2")
            self.widget_3 = QtWidgets.QWidget(parent=self.widget_2)
            self.widget_3.setGeometry(QtCore.QRect(11, 11, 322, 472))
            self.widget_3.setObjectName("widget_3")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
            self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.label_2 = QtWidgets.QLabel(parent=self.widget_3)
            self.label_2.setMaximumSize(QtCore.QSize(300, 450))
            self.label_2.setText("")
            self.label_2.setPixmap(QtGui.QPixmap(x.getImg()))
            self.label_2.setScaledContents(True)
            self.label_2.setObjectName("label_2")
            self.horizontalLayout_2.addWidget(self.label_2)
            self.widget_7 = QtWidgets.QWidget(parent=self.widget_2)
            self.widget_7.setGeometry(QtCore.QRect(11, 490, 408, 44))
            self.widget_7.setObjectName("widget_7")
            self.label_3 = QtWidgets.QLabel(parent=self.widget_7)
            self.label_3.setGeometry(QtCore.QRect(60, 10, 191, 21))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.label_3.setFont(font)
            self.label_3.setStyleSheet("color: rgb(175, 175, 162);")
            self.label_3.setObjectName("label_3")
            self.widget_6 = QtWidgets.QWidget(parent=self.widget_2)
            self.widget_6.setGeometry(QtCore.QRect(11, 541, 408, 44))
            self.widget_6.setObjectName("widget_6")
            self.widget_5 = QtWidgets.QWidget(parent=self.widget_6)
            self.widget_5.setGeometry(QtCore.QRect(-10, 80, 383, 127))
            self.widget_5.setObjectName("widget_5")
            self.label_4 = QtWidgets.QLabel(parent=self.widget_2)
            self.label_4.setGeometry(QtCore.QRect(100, 530, 191, 21))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.label_4.setFont(font)
            self.label_4.setStyleSheet("color: rgb(175, 175, 162);")
            self.label_4.setObjectName("label_4")
            self.btn_play1 = QtWidgets.QPushButton(parent=self.widget_2)
            self.btn_play1.setGeometry(QtCore.QRect(90, 570, 111, 51))
            self.btn_play1.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("ui\\../img/play-button.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.btn_play1.setIcon(icon)
            self.btn_play1.setIconSize(QtCore.QSize(50, 50))
            self.btn_play1.setObjectName("btn_play1")
            self.btn_play1.clicked.connect(lambda _,item=x: self.openlink(item))
            self.horizontalLayout.addWidget(self.widget_2)   

    def openlink(self,a):
        a.open_game()
    
    def showAdmin(self):
        home.show()
        self.close()

    def showIntro(self):
        intro.show()
        self.close()

    def showLogout(self):
        loginPage.show()
        self.close()

        


    
class Intro(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Intro.ui",self)

        self.btn_ADMIN.clicked.connect(self.showAdmin)
        self.btn_GAMES.clicked.connect(self.showGames)
        self.btn_LOGOUT.clicked.connect(self.showLogout)

    
    # Hàm chuyển trang phim
    def showAdmin(self):
        home.show()
        self.close()

    def showGames(self):
        library.show()
        self.close()

    def showLogout(self):
        loginPage.show()
        self.close()


if __name__ == "__main__":
    ListAcc = ListAccounts()
    app = QApplication(sys.argv)
    loginPage = LoginPage()
    signupPage = SigninPage()
    home = HomeMenuDashboard()
    library = Library()
    add = AddDialog()
    edit = EditDialog()
    sort = SortingPage()
    intro = Intro()
    library.show()
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