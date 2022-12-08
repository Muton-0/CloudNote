# 文件存储管理信息
import os
import Folder_Manage.Manage
import Menu.test_menu
# 判断是否首次使用系统
def is_first_use():
    if os.path.exists('flag.txt') == False:
        print('首次启动')
        flag = open('flag.txt', 'w+')
        flag.write('1')
        flag.close()  # 关闭文件
        init()  # 初始化资源
        print_login_menu()  # 打印登录菜单
        user_select()  # 选择用户
    else:
        flag = open('flag.txt', 'r')
        word = flag.read()
        if len(word) == 1:
            init()  # 初始化资源
            print_login_menu()  # 打印登录菜单
            user_select()  # 选择用户


# 初始化管理员
def init():
    if os.path.exists('users') == False:
        file = open('u_root.txt', 'w')  # 创建并打开管理员账户文件
        root = {'rnum': 'root', 'rpwd': "123456"}
        file.write(str(root))  # 写入管理员信息
        file.close()  # 关闭管理员账户文件

        os.mkdir('users')  # 创建普通用户文件夹


# 打印登录菜单
def print_login_menu():
    print('----用户登录----')
    print('1-管理员登陆')
    print('2-普通用户登陆')
    print('--------------')
    print('请选择您的登陆身份')



# 用户选择
def user_select():
    while True:
        user_type_select = input('请选择用户类型')
        if user_type_select == '1':  # 管理员登陆验证
            root_login()
            break
        elif user_type_select == '2':  # 普通用户
            while True:
                select = input('是否需要注册？（y/n）：')
                if select == 'y' or select == 'Y':
                    print('----用户注册----')
                    user_register()  # 用户注册
                    break
                elif select == 'n' or select == 'N':
                    print('----用户登录----')
                    break
                else:
                    print('输入有误，请重新选择')
            user_login()  # 用户登录
            break
        else:
            print('输入有误，请重新选择')


# 管理员登陆
def root_login():
    while True:
        print('****管理员登陆****')
        root_number = input('请输入管理员账户名：')
        root_password = input('请输入管理员密码：')
        file_root = open('u_root.txt', 'r')  # 只读打开文件
        root = eval(file_root.read())  # 读取账户信息
        # 信息匹配
        if root_number == root['rnum'] and root_password == root['rpwd']:
            print('管理员登陆成功！')
            Menu.test_menu.user_work()
            break
        else:
            print('很遗憾！验证失败')


# 用户注册 用户信息单独文件保存
def user_register():
    user_id = input('输入账户id：')
    user_pwd = input('输入用户密码：')
    user_name = input('输入用户昵称：')
    user = {'u_id': user_id, 'u_pwd': user_pwd, 'u_name': user_name}
    user_path = "./users/" + user_id # 新建文件夹保存信息
    file_user = open(user_path, 'w')
    file_user.write(str(user))
    file_user.close()


# 普通用户登录
def user_login():
    while True:
        print('****普通用户登录****')
        user_id = input('请输入账户名')
        user_pwd = input('请输入密码：')

        user_list = os.listdir('./users')  # 遍历元组，判断user_id是否在元组中
        flag = 0
        for user in user_list:
            if user == user_id:
                flag = 1
                print('登录中····')
                # 打开文件
                file_name = './users/' + user_id
                file_user = open(file_name)
                # 获取文件内容
                user_info = eval(file_user.read())
                if user_pwd == user_info['u_pwd']:
                    print('登录成功！')
                    # 此处根据需求，可以跳转到登陆成功之后的操作
                    Menu.test_menu.user_work()
                    break

        if flag == 1:
            break
        elif flag == 0:
            print('您并没有注册！请您先注册用户')
            break


if __name__ == '__main__':
    is_first_use()

