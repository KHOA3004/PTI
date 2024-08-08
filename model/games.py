import webbrowser, json
# Movie Object
class Game:
    def __init__(self, id_game, name_game, date, score_ranking, link_game):
        self.id_game = id_game
        self.name_game = name_game
        self.date = date
        self.score_ranking = score_ranking
        self.link_game = link_game
    #get properties 
    def getId(self):
        return self.id_game
    def getName(self):
        return self.name_game
    def getDate(self):
        return self.date
    def getScore(self):
        return self.score_ranking
    def getLink(self):
        return self.link_game
    
    def show(self):
        print(self.id_game, "-", self.name_game, "-", self.date, "-", self.score_ranking, "-", self.link_game)
    # def update(self, id, name, date, score_ranking, link_movie):
    #     ...
    def open_game(self):
        webbrowser.open(self.link_game)


class ListGame:
    def __init__(self):
        self.list = []
        self.loadAllGames()
    def getAllGames(self):
        return self.list
    def add_games(self, Game):
        self.list.append(Game)
        self.saveAllGames()
    def getGameByName(self, name_game):
        for game in self.list:
            if game.getName() == name_game:
                return game
    def delete_games_by_name(self,name_game):
        for game in self.list:
            if game.getName() == name_game:
                self.list.remove(game)
        self.saveAllGames()
    def edit_game_by_name(self,name_old_game:str,new_game:Game):
        for game in self.list:
            if game.getName() == name_old_game:
                self.list.remove(game)
                self.list.append(new_game)
        self.saveAllGames()
    def show_all_game(self):
        for i in self.list:
            i.show()
    def loadAllGames(self):
        try:
            with open("./data/games.json", "r") as file:
                jsonfile = json.load(file)
                for game in jsonfile:
                    game = Game(game["id_game"], game["name_game"], game["date"], game["score_ranking"], game["link_game"])
                    self.add_games(game)
        except FileNotFoundError:
            print("The file 'data/games.json' was not found.")
        except json.JSONDecodeError:
            print("The file 'data/games.json' does not contain valid JSON data.")
    def saveAllGames(self):
        jsonfile = list()
        for game in self.list:
            jsonfile.append(game.__dict__)
        with open("data/games.json", "w") as file:
            json.dump(jsonfile, file, indent = 5)
    def searchGameaByName(self,name)->list:
        result = []
        for game in self.list:
            if name in game.getName():
                result.append(game)
                game.show()
        return result

L = ListGame()
L.edit_game_by_name("1",Game("1","Conan","29/10/2004","2","https://www.youtube.com/playlist?list=PLKvoOwlacRoLbAmCd_0HsADRTCD4oo0Mv"))
L.searchGameaByName("Co")