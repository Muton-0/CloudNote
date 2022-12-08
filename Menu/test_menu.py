"""
目录的实现
"""

# from Folder_Manage.Folder_Manage import folder_manage_menu
import Folder_Manage.Manage
import RecycleBin.Deletefile

def user_work():
    info = '''
======Welcome to use YouDaoYunBiJi========
      输入功能编号，你可以选择相应的功能：
         1：文件管理
         2：回收站管理
         3：文件分享
         4：笔记修改
         0：退出系统
==========================================
    '''
    while True:
        print(info)
        code = input("请输入功能编号:")
        if code == "1":
            Folder_Manage.Manage.folder_manage_menu()
        if code == "2":
            flag = input("请输入需要删除还是恢复(1表示删除，2表示恢复)：")
            if flag == "1":
                RecycleBin.Deletefile.deletefile()
            else:
                RecycleBin.Deletefile.recover()
        if code == "3":
            print(33)
        if code == "0":
            print("感谢您使用有道云笔记!")
            break


if __name__ == "__main__":
    login()
