# # arr = [[1, 2, 3, 4], [5, 6, 7, 8]]
# # for row in range(len(arr)):# 0 1
# #     for col in range(len(arr[row])):# 0 1 2 3
# #         print(arr[row][col])
# # print('----------------------------------------------------------------------------------------')
# # 元组是一种不可变的序列类型
# tuple1 = ()# 元组符号是圆括号
# tuple2 = tuple('abcd')
# print(tuple2)
#
# tuple3 = (1,2,3,4,5,6)
# # 元组是一种有序列的数据类型
# print(tuple3[-1])
# print(tuple3[0:3])
# # 创建只有一个元素的元组,要加逗号
# tuple4 = (1,)
# print(type(tuple4))

array = [1, 2, 3, 4, 5, 6]
# """在列表末尾增加数据"""
# array.append(7)
# print(array)
# # 指定位置处添加索引,列表操作都是操作的列表本身
# """第一个参数是你要在列表的哪里插入数据，第二个是你要插入什么数据"""
# array.insert(0,'a')
# array.insert(1,9)
# print(array)
"""删除数据"""
# array.pop(0)  # 默认删除列表最后一个元素
# print(array)
'''指定元素删除'''
# array.remove(3)
# print(array)
"""查找数据index"""
# print(array.index(3))
# """列表合并"""
# a = [1,2,3]
# b = [4,5,6]
# a.extend(b)
# print(a)

"""字典"""
# 通过大括号定义字典，通过键值对赋值
# dict1 = {}
dict2 = {
    'name': '魏冰',
    'age' : 18,
    'height': 162,
    'hobby': 'depend on boyfrind'
}
# """字典的取值用键值对"""
# # 字典是可变的
# print(dict2['name'])
# print(dict2['age'])
# print(dict2['hobby'])
# dict2['age'] = 20
# print(dict2['age'])
# 当键值对不存在时就新增一个键值对
# 当键值对不存在可以用get方法可以不报错
print(dict2.get('and1'))






