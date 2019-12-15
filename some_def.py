from con_db import client, con_db

class Tag(object):
    client.get_collection(collection="tags")
    _tag_colletion = client.demo_collection

    def __init__(self, tag):
        self.tag = tag
        self.num = 1


    def creat_tag(self, tag_colletion=_tag_colletion):
        try:
            tag_colletion.insert(self.__dict__)
        except Exception as e:
            if str(e)[0:6] == "E11000":
                myquery = {"tag": self.tag}
                data = con_db.cursor_to_list(tag_colletion.find(myquery))[0]
                data_of_num = data['num']
                self.num = data_of_num + 1
                newvalues = {"$set": {"num": self.num}}
                tag_colletion.update(myquery, newvalues, upsert=False)

    @staticmethod
    def query_fre_tag(num=8):
        tag_colletion = Tag._tag_colletion
        a = tag_colletion.find({}, {"_id": 0}, limit=num).sort("num", -1)
        # find({likes: {$gt: 100}})
        return con_db.cursor_to_list(a)

    @staticmethod
    def setIndex(tag_colletion=_tag_colletion):
        """设置tags 对象数据库中的索引，只需运行一次"""
        try:
            tag_colletion.ensure_index([("tag", 1)], unique=True)
        except Exception as e:
            print(e)
            return False
        else:
            return True

    @staticmethod
    def init_tag_db():
        from questionsObject import Questions
        a = Questions.query_all_question(_id=0, q_tag=1)
        for iter in a:
            list_data = iter["q_tag"]
            for j in list_data:
                new_tag = Tag(tag=j)
                new_tag.creat_tag()

if __name__ == '__main__':
    # a = Tag.query_fre_tag()
    # for i in a:
    #     print(i)
    import Data_migration
