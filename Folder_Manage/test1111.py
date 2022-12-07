"""
上传和下载只不过是在不同地方进行下载，其实功能大差不差
"""

def folder_download(source_road,target_road):
    return

class Adapter(object):
    def __init__(self,adaptee):
        self.adaptee=adaptee

    def download(self):
        self.adaptee.upload()

class Target(object):
    def download(self):
        print('download')

class Adaptee(object):
    def upload(self):
        print('upload')

if __name__=='__main__':
    objects=[]
    a=Target()
    b=Adaptee()

    objects.append(a)
    objects.append(Adapter(b))

    for obj in objects:
        obj.download()
