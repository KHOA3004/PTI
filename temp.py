class HinhChuNhat:
    def __init__(self, chieudai = 6, chieurong = 7):
        self.chieudai = chieudai
        self.chieurong = chieurong
    def TinhChuVi(self):
        return (self.chieudai + self.chieurong )* 2
    def TinhDienTich(self):
        return self.chieudai * self.chieurong
    def Show(self):
        print(self.TinhChuVi())
        print(self.TinhDienTich())

class Accounts:
    def __init__(self,username  = "", password = ""):
        self.us = username
        self.pw = password
    def Show(self):
        print("Username:", self.us)
        print("Password",self.pw)
    def Login(self, inputUS, inputPW):
        if self.us == inputUS and self.pw == inputPW:
            print("Dang nhap thanh cong ")
        else:
            print("Vui long thu lai ")

    def ChangePassword(self, inputUS, inputOldPW, inputNewPW):
        if inputUS == self.us and self.pw == inputOldPW:
            self.pw = inputNewPW
            print("Doi mk thanh cong")
        else:
            print("Sai us or pw")

    def SignUp(self, inputUS, inputPw):
        self.us = inputUS
        self.pw = inputPw

us1 = Accounts()
us1.SignUp("ThaiHung","123")
us1.Show()
us1.Login("ThaiHung", "123")
us1.ChangePassword("ThaiHung", "123", "111")
us1.Show()

