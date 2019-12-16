import hashlib
from con_db import client, con_db
import pymongo



class User(object):
    client.get_collection(collection="info")
    _user_colletion = client.demo_collection  # 连接存储用户信息的集合

    def __init__(self, username, name=""):
        self.username = username
        self.name = name
        self.password = None

    def hash_password(self, password):
        """
        将明文密码加密成hash值
        :param password: 明文密码
        :return:
        """
        pwd_temp = hashlib.sha1(password.encode())
        self.password = pwd_temp.hexdigest()  # 密码hash加密

    def verify_password(self, password, user_colletion=_user_colletion):
        """
        验证用户的用户名和密码正确性
        :param password: hash密码
        :param user_colletion:
        :return:
        """
        hash_pwd = self.hash_password(password)
        qurey_dir = {
            'username': self.username,
            'password': self.password
        }
        qurey_result = user_colletion.find_one(qurey_dir)
        if qurey_result == None:
            return False  # 密码错误
        else:
            self.name = qurey_result['name']
            return True

    def setNewUser(self, user_colletion=_user_colletion):
        """
        注册用户，新建一个用户
        :return:如果不存在，返回False，else 返回True
        """
        info_dir = {
            "username": self.username,
            "password": self.password,
            "name": self.name
        }
        try:
            if user_colletion.insert(info_dir):
                return True  # 成功注册
        except pymongo.errors.DuplicateKeyError:
            print("已存在该用户: ", self.username)
            return False

    def del_a_user(self, user_colletion=_user_colletion):
        """
        删除一个用户，必须输入密码，而不是通过id来删除
        :param user_colletion:
        :return:
        """
        query = {
            "username": self.username,
            "password": self.password,
        }
        try:
            if user_colletion.delete_one(query):
                return True
        except Exception as e:
            return False

    def queryinfo(self, user_colletion =_user_colletion):
        """查询用户信息"""
        info_dir = {
            "username": self.username
        }
        return user_colletion.find_one(info_dir, {"_id": 1, "password": 1})

    def update_a_user(self, user_colletion=_user_colletion, **kwargs):
        query = {"username": self.username}
        try:
            print(kwargs)
            if user_colletion.update(query, kwargs):
                return True
        except Exception as e:
            print(e)
            return False

    def query_a_user(self, user_colletion=_user_colletion, **kwargs): # TODO 为什么字段返回不对
        query = {"username": self.username}
        try:
            if kwargs == {}:
                user_cursor = user_colletion.find(query)
            else:
                user_cursor = user_colletion.find(query, kwargs)
        except Exception as e:
            print(e)
        return con_db.cursor_to_list(user_cursor)

    @staticmethod
    def query_all_user(user_colletion=_user_colletion, limit=0, **kwargs):
        """
        查询所有用户信息
        :param user_colletion: 用户集合数据库连接
        :param limit: 数量限制
        :param kwargs: 返回字段限制
        :return: [
        {'_id': ObjectId('5def81a740e3f0bbab5603e2'),
        'username': '123123123', 'password': '601f1889667efaebb33b8c12572835da3f027f78',
         'name': 'icejm'}
        ]
        """
        try:
            if kwargs == {}:
                user_cursor = user_colletion.find({}, limit=limit)
            else:
                user_cursor = user_colletion.find({}, kwargs, limit=limit)
        except Exception as e:
            print(e)
        return con_db.cursor_to_list(user_cursor)

    @staticmethod
    def setIndex(user_colletion=_user_colletion):
        """设置questionsObject 对象数据库中的索引，只需运行一次"""
        try:
            user_colletion.ensure_index([("username", 1)], unique=True)
        except Exception as e:
            print(e)
            return False
        else:
            return True

if __name__ == '__main__':
    pass
    # query_all_user 查询所有用户
    # print(User.query_all_user())
    # setNewUser 创建一个用户
    new_user = User(username="zjianfa", name="云上有春秋")
    # new_user.hash_password("123456")
    # new_user.del_a_user()
    new_user.update_a_user(username="zjianfa23")

    # del_a_user 删除一个用户
    # user = User(username="")