import json
class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    
    def show(self):
        print("US:", self.username, "-PW:", self.password)
    def setNewPassword(self, password):
        self.password = password
    def getUserName(self):
        return self.username
    def getPassWord(self):
        return self.password

class ListAccounts:
    def __init__(self):
        self.list = []
        self.loadAllAccounts()
    
    def addAccount(self, account):
        self.list.append(account.getUserName()+":"+account.getPassWord())
        self.l.saveAllAccounts()
    def showAllAccount(self):
        print(self.list)
    def changePasswordAccount(self, username, oldpassword, newpassword):
        for account in self.list:
            if account.username == username:
                if account.password == oldpassword:
                    account.setNewPassword(newpassword)
                else:
                    print("Wrong password!!!!")
    def saveAllAccounts(self):
        jsonfiles = list()
        for account in self.list:
            pos = account.find(":")
            us = account[:pos]
            ps = account[pos+1:]
            newAccount = Account(us, ps)
            jsonfiles.append(newAccount.__dict__)
        with open("data/accounts.json", "w") as file:
            json.dump(jsonfiles, file, indent=2)

    def loadAllAccounts(self):
        with open("data/accounts.json", "r") as file:
            jsonFile =  json.load(file)

            for account in jsonFile:
                self.list.append(account["username"] +":"+ account["password"])
    def checkAccounts(self, account:Account):
        return (account.getUserName() + ":" + account.getPassWord()) in self.list

