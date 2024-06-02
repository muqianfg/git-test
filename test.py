# test.py

def add_arrays(a, b):
    """
    ��������Ԫ�ؼ�����ӡ�

    ����:
    a -- �б����ͣ���һ�����顣
    b -- �б����ͣ��ڶ������顣

    ����:
    �б� -- ����`a`��`b`Ԫ�ؼ�����ӽ�������б�

    �׳��쳣:
    TypeError -- ���`a`��`b`�����б�
    ValueError -- ���`a`��`b`���Ȳ�ͬ��
    """
    # ��������Ƿ�Ϊ�б�
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("������붼���б�")

    # �����һ�б�Ϊ�գ���������
    # ����б��Ƿ�Ϊ��
    if not a or not b:
        print("���棺�����б�֮һΪ�ա�")

    # ȷ�������б�����ͬ
    # ����б����Ƿ����
    if len(a) != len(b):
        raise ValueError("�����б���������ͬ�ĳ��ȡ�")

    # ʹ���б��Ƶ�ʽʵ�ָ�ЧԪ�ؼ�����Ӳ����ؽ��
    return [x + y for x, y in zip(a, b)]

def input_arrays():
    """
    �����������顣

    ����:
    �������顣
    """
    a = raw_input("�������һ�����飺")
    a = eval(a)

    b = raw_input("������ڶ������飺")
    b = eval(b)

    return a, b

# ��������������ȡ�û����벢���� add_arrays ����
if __name__ == '__main__':
    a, b = input_arrays()
    try:
        result = add_arrays(a, b)
        print "�������:", result
    except Exception as e:
        print "��������:", e

    
