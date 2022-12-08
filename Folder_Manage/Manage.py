"""
文件夹管理系统
"""

from pathlib import Path
import Folder_Manage.Folder_Factory
import RecycleBin.Deletefile
tree_str = ''

def folder_manage_menu():
    info = '''
===========文件管理系统================
   输入功能编号，你可以选择相应的功能：
      1：查看网盘文件
      2：创建、查询、修改
      3：删除
      4：上传或下载
      5：功能编号说明
      0：退出系统
=====================================
    '''
    print(info)
    path = '../YunDisk'
    folder_tree(Path(path), 0)
    code = input("请输入功能编号:")
    while True:
        if code == "1":
            print(tree_str)
        elif code == "2":
            folder_factory()
        elif code == "3":
            RecycleBin.Deletefile().deletefile()
        elif code == "4":
            print(44)
        elif code == "5":
            print(info)
        elif code == "0":
            print("感谢您使用有道云笔记文件管理系统!")
            break
        else:
            code = input("输入错误，请重新输入:")
            continue
        print("如果需要再次查看功能编号的对应关系，请输出5")
        code = input("如需系要继续使用该统，请按输入功能编号：")
    return


def folder_tree(pathname, n=0):
    global tree_str
    if pathname.is_file():
        tree_str += '    |' * n + '-' * 4 + pathname.name + '\n'
    elif pathname.is_dir():
        tree_str += '    |' * n + '-' * 4 + \
                    str(pathname.relative_to(pathname.parent)) + '\\' + '\n'
        for cp in pathname.iterdir():
            folder_tree(cp, n + 1)


def folder_factory():
    flag = input("请输入需要创建还是查询(1表示创建，2表示查询、3表示修改)：")
    factory = Folder_Manage.Folder_Factory.Factory()
    factory.operator_make(flag).operator_result()
    return


# 测试
if __name__ == "__main__":
    folder_manage_menu()
