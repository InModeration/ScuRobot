import hashlib
from con_db import con_db # 连接数据库
import pymongo

con_db = con_db(collection='info').demo_collection #  连接存储用户信息的集合

class User(object):

    def __init__(self, username):
        self.username = username
        self.name = None
        self.password = None

    def del_user(self):
        info_dir = {
            "username": self.username,
            "password": self.password,
            "name": self.name
        }
        con_db.delete_one()


    def hash_password(self, password):
        pwd_temp = hashlib.sha1(password.encode())
        self.password = pwd_temp.hexdigest() # 密码hash加密


    def verify_password(self, password):
        hash_pwd = self.hash_password(password)
        qurey_dir = {
            'username': self.username,
            'password': self.password
        }
        qurey_result = con_db.find_one(qurey_dir)
        if qurey_result == None:
            return False  # 密码错误
        else:
            self.name = qurey_result['name']
            return True


    def setNewUser(self):
        """
        注册用户
        :return:如果不存在，返回False，else 返回True
        """
        info_dir = {
            "username": self.username,
            "password": self.password,
            "name": self.name
        }
        try:
            if con_db.insert(info_dir):
                return True  # 成功祖册
        except pymongo.errors.DuplicateKeyError:
            print("已存在该用户: ", self.username)
            return False

    def queryinfo(self):
        info_dir = {
            "username": self.username
        }
        return con_db.find_one(info_dir,{"_id":0,"password":0})