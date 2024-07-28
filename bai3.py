import webbrowser
import json
from accounts import A           
    
newlist = ListAccounts()
newlist.showAllAccount()
newlist.addAccount(Account("quanlh1","123"))
newlist.saveAllAccounts()


    
newlist = ListMovie()
newlist.add_movie(Movie("1", "Conan", "29/10/2004", 10, "https://www.youtube.com/playlist?list=PLKvoOwlacRoLbAmCd_0HsADRTCD4oo0Mv"))
newlist.add_movie(Movie("2", "Dragonball ", "29/10/2004", 10, "https://dragonballwiki.net/xemphim/"))
newlist.saveAllMovies()


# while True:
#     newlist.show_all_movie()
#     x = input("Nhap id phim muon xem")
#     for i in newlist.getAllMovies():
#         if x == i.getId():
#             i.open_movie()
    
