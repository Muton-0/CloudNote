'''
文件夹管理系统
'''

from pathlib import Path
# import Folder_Factory

tree_str = ''

def folder_manage_menu():
    info = '''
===========文件管理系统================
   输入功能编号，你可以选择相应的功能：
      1：查看网盘文件
      2：创建、查询
      3：删除、移动
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
        if code == "2":
            print(22)
        if code == "3":
            print(33)
        if code == "4":
            print(44)
        if code == "5":
            print(info)
        if code == "0":
            print("感谢您使用有道云笔记文件管理系统!")
            break
        print("如果需要再次查看功能编号的对应关系，请输出5")
        code=input("如需系要继续使用该统，请按输入功能编号：")
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
    return

#测试
if __name__ == "__main__":
    folder_manage_menu()