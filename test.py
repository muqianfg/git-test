# test.py

def add_arrays(a, b):
    """
    两个数组元素级联相加。

    参数:
    a -- 列表类型，第一个数组。
    b -- 列表类型，第二个数组。

    返回:
    列表 -- 包含`a`和`b`元素级联相加结果的新列表。

    抛出异常:
    TypeError -- 如果`a`或`b`不是列表。
    ValueError -- 如果`a`和`b`长度不同。
    """
    # 检查输入是否为列表
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("输入必须都是列表。")

    # 如果任一列表为空，给出警告
    # 检查列表是否为空
    if not a or not b:
        print("警告：输入列表之一为空。")

    # 确保两个列表长度相同
    # 检查列表长度是否相等
    if len(a) != len(b):
        raise ValueError("输入列表必须具有相同的长度。")

    # 使用列表推导式实现高效元素级联相加并返回结果
    return [x + y for x, y in zip(a, b)]

def input_arrays():
    """
    输入两个数组。

    返回:
    两个数组。
    """
    a = raw_input("请输入第一个数组：")
    a = eval(a)

    b = raw_input("请输入第二个数组：")
    b = eval(b)

    return a, b

# 如果是主程序，则获取用户输入并调用 add_arrays 函数
if __name__ == '__main__':
    a, b = input_arrays()
    try:
        result = add_arrays(a, b)
        print "结果数组:", result
    except Exception as e:
        print "发生错误:", e

    
