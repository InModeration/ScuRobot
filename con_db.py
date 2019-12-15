import pymongo

class con_db():
    def __init__(self, ip='49.235.105.136', port=27017, username="scubot", password="123456"):
        """
        :type collection: str
        """
        self.ip = ip
        self.port = port
        self.client = pymongo.MongoClient(ip, port=port, connect=False, username=username, password=password)
        self.demo_collection = None

    def get_collection(self, db_name="scubot_v1", collection=''):
        mongo_db = self.client[db_name]
        self.demo_collection = mongo_db[collection]

    def closedb(self):
        self.client.close()

    @staticmethod
    def cursor_to_list(cursor_obj):
        """游标对象 遍历成 列表"""
        list_obj = []
        for iter in cursor_obj:
            list_obj.append(iter)
        return list_obj

# 一个连接
client = con_db()

if __name__ == '__main__':

    # client = con_db()
    client.get_collection(collection="questions")
    db_collection = client.demo_collection

    db_collection.insert({"title": 'MongoDB 教程',
                    "description": 'MongoDB 是一个 Nosql 数据库'
                 })


