from abc import ABC, abstractmethod
import os


class Folder_Operator(ABC):
    @abstractmethod
    def operator_result(self):
        pass


class Folder_Create(Folder_Operator):
    def operator_result(self):
        folder_name = input("请输入想要创建文件夹的文件夹名：")
        folder_road = input("请输入想要创建文件夹的文件夹路径(/开头)：")
        folder_road = "../YunDisk" + folder_road + '/' + folder_name
        mkdir(folder_road)


class Folder_Search(Folder_Operator):
    def operator_result(self):
        flag = 0
        file_name = input("请输入搜索的文件的名字:")
        for root, dirs, files in os.walk(r"..\YunDisk"):
            for file in files:
                if os.path.basename(file) == file_name:
                    flag = 1
                    print(os.path.join(root, file))
        if flag == 0:
            print("未找到该名字的文件。\n")
        else:
            print('\n')


class Factory:
    def operator_make(self, flag):
        if flag == '1':
            return Folder_Create()
        elif flag == '2':
            return Folder_Search()


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("文件已创建。\n")
    else:
        print("文件夹已存在，创建失败。\n")


# 测试
if __name__ == '__main__':
    flag = input("请输入需要创建还是查询(1表示创建，2表示查询):")
    factory = Factory()
    factory.operator_make(flag).operator_result()
