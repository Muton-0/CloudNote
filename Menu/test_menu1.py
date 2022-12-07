"""
目录的实现
"""

# from Folder_Manage.Folder_Manage import folder_manage_menu
import Folder_Manage.Folder_Manage

def login():
    print('==========Welcome to YouDaoYunBiJi==========')
    while True:
        user_name = input("请输入用户名:")
        if user_name == "admin":
            password = input("请输入密码:")
            if password == "1":
                print("欢迎您,亲爱的用户")
                break
            else:
                print("密码错误哦！请重新输入账号和密码")
        else:
            print("不存在该用户名，请重新输入。")
    user_work()


def user_work():
    info = '''
======Welcome to use YouDaoYunBiJi========
      输入功能编号，你可以选择相应的功能：
         1：文件管理
         2：
         3：
         4：
         0：退出系统
==========================================
    '''
    while True:
        print(info)
        code = input("请输入功能编号:")
        if code == "1":
            Folder_Manage.Folder_Manage.folder_manage_menu()
        if code == "2":
            print(22)
        if code == "3":
            print(33)
        if code == "0":
            print("感谢您使用有道云笔记!")
            break


if __name__ == "__main__":
    login()
