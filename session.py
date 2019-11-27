from con_db import con_db# 连接数据库

con_db = con_db(collection='session').demo_collection #  连接存储用户信息的集合

class Session(object):
    def __init__(self, username):
        self.token = None
        self.username = username

    def add(self):
        """
        在session 里面添加一个用户
        :return:
        """
        insert_dir = {
            'username': self.username,
            'token': self.token
        }
        con_db.insert_one(insert_dir)
        return True

    def update(self):
        update_dir ={
            'username': self.username,
            'token': self.token
        }
        # upsert=True 如果找不到查询的结果是否插入一条数据
        con_db.update_one({"username": self.username}, {"$set": update_dir}, upsert=False)
        return True

    def query(self):
        query_dir = {
            'username': self.username
        }
        print(query_dir)
        query_info = con_db.find_one(query_dir)
        return query_info

    def delete(self):
        dir = {
            'useranme':self.username
        }
        con_db.delete_one(dir)


# if __name__ == '__main__':
#     insert_dir = {
#         'username': "1312",
#         'token': "12312312"
#     }
#     con_db.insert_one(insert_dir)
#     con_db.create_index([("username", pymongo.ASCENDING)], unique=True)
#     sort = sorted(list(con_db.index_information()))
