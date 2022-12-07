from pathlib import Path

tree_str = ''

def Folder_Manage_Menu():
    info = '''
        '==========文件管理系统==========='
             输入功能编号，你可以选择相应的功能：
                1：查看网盘文件
                2：创建、查询
                3：删除、移动
                4：上传或下载
                0：退出系统
        ========================================
        '''
    print(info)
    while True:
        code = input("请输入功能编号:")
        if code == "1":
            path = '../YunDisk'
            Dile_Tree(Path(path), 0)
            print(tree_str)
        if code == "2":
            print(22)
        if code == "3":
            print(33)
        if code == "4":
            print(44)
        if code == "0":
            print("感谢您使用有道云笔记!")
            break
    return

def Dile_Tree(pathname, n=0):
    global tree_str
    if pathname.is_file():
        tree_str += '    |' * n + '-' * 4 + pathname.name + '\n'
    elif pathname.is_dir():
        tree_str += '    |' * n + '-' * 4 + \
            str(pathname.relative_to(pathname.parent)) + '\\' + '\n'
        for cp in pathname.iterdir():
            Dile_Tree(cp, n + 1)


#测试
if __name__ == "__main__":
    Folder_Manage_Menu()