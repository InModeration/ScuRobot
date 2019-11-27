import pymongo

class con_db():
    def __init__(self, ip='49.235.105.136', port=27017,
                 db_name='scubot_v1', collection="questions"):
        self.ip = ip
        self.port = port
        self.client = pymongo.MongoClient(ip, port=port, connect=False)
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
