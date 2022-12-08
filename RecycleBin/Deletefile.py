import os
import numpy as np
from shutil import copyfile
from sys import exit


flag = 0;
def deletefile():

    file_path = input("请输入删除的文件的路径:")
    target = os.path.basename(file_path)
    f = open('Bin','w+')
    f.write(target)
    f.write('\n')
    f.write(file_path)
    f.write('\n')
    copy(file_path, target)
    os.remove(file_path)
    print("File removed successfully")
def copy(source,target):
    # adding exception handling
    try:
        copyfile(source, target)
    except IOError as e:
        print("Unable to copy file. %s" % e)
        exit(1)
    except:
        print("error")
        exit(1)
    print("\nFile copy done!\n")
def recover():
    flag1 = flag2 = ''
    file_name = input("请输入要恢复的文件的文件名:")
    file = open('Bin', 'r')  # 打开目标文件
    file_contents = file.readlines()  # 按行读取全部内容
    file_contents = np.array(file_contents)
    for i in range(0, len(file_contents)):
        if file_name in file_contents[i]:
            file_path = file_contents[i+1].strip('\n')
            flag1 = i;
            flag2 = i+1;
        break
    copy(file_name, file_path)
    os.remove(file_name)

    transit = ""  # 创立空的字符串用于储存文件
    line_number = 1  # 记录文本文件的行号
    for line in file:  # 使用迭代器读取每一段文本文件的内容
        if (line_number == flag1) or (line_number == flag2):
            line_number += 1
            continue
        else:
            transit += line  # 将数据写入过渡的字符串中
            line_number += 1
    file.close()
    onfile = open('Bin', 'w')  # 以清空原文本文件内容的方式打开文件写入
    onfile.write(transit)
    onfile.close()

def binmanage():
    flag = input("请输入需要删除还是恢复(1表示删除，2表示恢复)：")
    if flag == "1":
        deletefile()
    else:
        recover()

if __name__=='__main__':
    binmanage()



