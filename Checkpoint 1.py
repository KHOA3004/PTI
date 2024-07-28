class HomeworkList:  
    def __init__(self):  
        self.items = []  

    def add_item(self, item):  
        self.items.append(item)  

    def all_finished(self):  
        return all(item['status'] == 'Hoàn thành' for item in self.items)  


homework_list = HomeworkList()  

 
homework_list.add_item({'title': 'Lập trình App Producer', 'importance': 'Cao', 'status': 'Chưa hoàn thành'})  
homework_list.add_item({'title': 'Lập trình GameMaker', 'importance': 'Trung bình', 'status': 'Chưa hoàn thành'})  
homework_list.add_item({'title': 'Làm văn', 'importance': 'Thấp', 'status': 'Chưa hoàn thành'})  


if homework_list.all_finished():  
    print("All finished")  
else:  
    print("Chưa hoàn thành tất cả")