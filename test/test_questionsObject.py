from questionsObject import Questions




if __name__ == '__main__':
    # 插入问题demo, q_name 为主键
    q_demo = Questions(q_name="请问川大哪122？", q_tag=["123", "石凳子", "我 "], q_describe="因为今天中午我找了很久都没找到",
                       create_user="zjianfa")  #
    q_demo.crate_a_question()

    # 查询所有问题
    a_list = q_demo.query_all_question()
    print(a_list)

    # 模糊查询问题和tag
    # b_list = q_demo.query_some_question()