'''
文件夹工厂模式：
根据不同需求，对文件夹进行操作
'''

class Folder_Operator:
    def operator_result(self):
        pass

class Folder_Create(Folder_Operator):
    def operator_result(self):
        print("create")
        return

class Folder_Search(Folder_Operator):
    def operator_result(self):
        print("Search")
        return

class Factory:
    @staticmethod
    def factory_result(Operator):
        if Operator == 1:
            return Folder_Create(Operator)
        elif Operator == 2:
            return Folder_Search(Operator)

A=1
Factory.factory_result(A)

