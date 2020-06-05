'''
1.现有商品如下打印出以下格式
------- 商品信息 -------
1  iphone	6888　　　　　　
2  MacPro	14800　　　　　
3  小米6　　	6666　　　　　　
4  coffee	31　　　　　　　　
5  Book　	60　　　　　　　　
6  nike　	699　
2.根据上面的商品列表写一个循环，不断询问用户想买什么，用户选择一个商品编号或者商品名称价格，就把对应商品添加到
购物车里最终用户输入q退出时，打印购买的商品列表
'''
orders=[["iphone", 6888], ["MacPro", 14800], ["小米6", 6666], ["coffee", 31], ["Book", 60], ["nike", 699]]
i=1
shopping_cart = []
print('-'*7, '商品信息', '-'*7)
run_flag = True
def is_exist_by_double_list(target, element):#判断某个字符串是否在某个二维列表里
    for line in target:
        if element in line:
            return True
    return False
while run_flag:
    #这下面的打印为第一题，其余所有为第二题
    for index, i in enumerate(orders):
        tpls="{0}  {1:\u3000<5}\t{2:\u3000<10}"
        print(tpls.format(index+1, i[0], i[1], chr(12288)))
    choices=input("请输入你想购买的商品编号：")
    if choices.isdigit():
        choices = int(choices)
        if choices>0 and choices<len(orders)+1:
            shopping_cart.append(orders[choices-1])
            print("\n", "商品---%s---已加入购物车"%(orders[choices-1][0]), "\n")
        elif is_exist_by_double_list(orders, choices):
            for index, i in enumerate(orders):
                if choices == i[1]:
                    shopping_cart.append(i)
                    print("\n", "商品---%s---已加入购物车" % (i[0]), "\n")
        else:
            print("\n", "您输入的商品不存在哟！！", "\n")
#         print(shopping_cart)
    elif choices == 'q':
        if len(shopping_cart) > 0:
            print("购物车的商品", "\n")
            # print(shopping_cart)
            for index, i in enumerate(shopping_cart):
                print("%s.%s %s"%(index+1, i[0], i[1]))#
        else:
            print("您还没有购买商品哦！！！")
        run_flag = False
    else:
        choices = str(choices)
        if is_exist_by_double_list(orders, choices):
            for index, i in enumerate(orders):
                if choices == i[0]:
                    shopping_cart.append(i)
                    print("\n", "商品---%s---已加入购物车" % (i[0]), "\n")
        else:
            print("您输入的商品不存在呦a！！！")

"""
                   判断二维列表中是否存在某个元素
               :param target:目标列表
               :param element:需要判断的元素
               :return:bool类型，是否存在
"""


        # run_flag = False
#         else:
#             choices == str(choices)
# #for index,i in enumerate(orders):
#             if choices == orders[0][0]:
#                 shopping_cart.append(choices)
#                 print"In"."商品%s已加入购物车"%shopping_cart."An")
#                 #shopping_cart.append(orders[index]) #print("In","商品%s已加入购物车"%(orders[index]),"\n"）
#             elif choices == orders[0][1]:
#                 shopping_cart.append(choices)
#                 print("n',"商品%s已加入购物车"%shopping_cart."\n)
#             #shopping_cart.append(orders[index]) #print("In","商品%s已加入购物车"%（orders[index]）."\n"）
#             else:
#                 print"您输入的商品不存在呢”）