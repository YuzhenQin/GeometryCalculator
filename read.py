import re

from sympy import rad, pi, Integer, sqrt, sin, cos, tan

from classes import *


def to_line_object(s: str, points: dict) -> Line:
    """
    读取线名转化为线的对象
    :param s: 名字，长度为2
    :param points: 点的字典
    :return: 线的对象
    """
    p1 = points[s[0]]
    p2 = points[s[1]]
    return Line(p1, p2)


def to_expr(s, points: dict):
    """
    将字符串转化为表达式
    :param s: 用户输入的字符串
    :param points: 点的字典
    :return: 表达式
    """
    # 处理线段
    pattern = r'\b([A-Z])([A-Z])\b'
    repl = r"distance(points['\1'], points['\2'])"
    s = re.sub(pattern, repl, s)
    # 三角函数
    pattern = r'\b(sin|cos|tan)(∠[A-Z]{3})'
    repl = r'\1(\2)'
    s = re.sub(pattern, repl, s)
    # 处理角
    pattern = r'∠([A-Z])([A-Z])([A-Z])\b'
    repl = r"Angle(points['\1'], points['\2'], points['\3']).val"
    s = re.sub(pattern, repl, s)
    # 角度制转弧度制
    pattern = r'\b(\d+)°'
    repl = r'rad(\1)'
    s = re.sub(pattern, repl, s)
    # π转pi
    s = s.replace('π', 'pi')
    # 处理整数与分数
    pattern = r'\b(\d+)\b'
    repl = r'Integer(\1)'
    s = re.sub(pattern, repl, s)
    return eval(s)


if __name__ == '__main__':
    print(to_expr('1/3', {}))
    print(to_expr('tan∠AOB', {'A': Point('A', 5, 5), 'O': Point('O', 0, 0), 'B': Point('B', 5, 0)}))
    print(to_expr('sqrt(2)', {}))
