import sympy


class Point:
    def __init__(self, name: str, x=None, y=None):
        """
        点
        :param name: 名字
        :param x: 横坐标，None代表未知数
        :param y: 纵坐标，None代表未知数
        """
        self.name = name
        if x is None:
            x = sympy.Symbol(f'x_{self.name}')
        if y is None:
            y = sympy.Symbol(f'y_{self.name}')
        self.x = x
        self.y = y

    def coordinate(self) -> tuple:
        """
        获取该点的坐标
        :return: 元组，点的坐标
        """
        return self.x, self.y

    def __str__(self):
        return f'{self.name}{self.coordinate()}'


class Line:
    def __init__(self, p1: Point, p2: Point):
        """
        线段/射线/直线
        :param p1: 线上一点
        :param p2: 线上另一点
        """
        self.p1 = p1
        self.p2 = p2

    @property
    def abc(self) -> tuple:
        """
        直线的一般式(ax + by + c = 0)方程的a,b,c
        :return: 元组(a, b, c)
        """
        # 已知直线上两点求直线的一般式方程
        # 已知直线上的两点P1(X1,Y1) P2(X2,Y2)， P1 P2两点不重合。则直线的一般式方程AX+BY+C=0中，A B C分别等于：
        # A = Y2 - Y1
        # B = X1 - X2
        # C = X2*Y1 - X1*Y2
        x1, y1 = self.p1.coordinate()
        x2, y2 = self.p2.coordinate()
        a = y2 - y1
        b = x1 - x2
        c = x2 * y1 - x1 * y2
        return a, b, c


class Intersection(Point):
    def __init__(self, name: str, l1: Line, l2: Line):
        """
        两条线的交点
        :param name: 名字
        :param l1: 一条线
        :param l2: 另一条线
        """
        # 两直线交点的计算公式：
        # 直线一：A1x+B1y+C1=0，
        # 直线二：A2x+B2y+C2=0，
        # 则两直线交点计算方法为：
        # x=(B1C2-B2C1)/(B2A1-B1A2) 。
        # y=(A1C2-C1A2)/(B1A2-A1B2)。
        a1, b1, c1 = l1.abc
        a2, b2, c2 = l2.abc
        x = (b1 * c2 - b2 * c1) / (b2 * a1 - b1 * a2)
        y = (a1 * c2 - c1 * a2) / (b1 * a2 - a1 * b2)
        super().__init__(name, x, y)


class PointOnLine(Point):
    def __init__(self, name: str, x, l: Line):
        """
        线上的点
        :param name: 名字
        :param x: 横坐标，None代表未知数
        :param l: 点所在的线
        """
        a, b, c = l.abc
        # 特殊情况：竖线
        if b == 0:
            # ax + c = 0
            # x = -c / a
            x = -c / a
            super().__init__(name, x, None)
            return
        # ax + by + c = 0
        # by = -ax - c
        # y = (-ax - c) / b
        if x is None:
            x = sympy.Symbol(f'x_{name}')
        y = (-a * x - c) / b
        super().__init__(name, x, y)


def distance(p1: Point, p2: Point):
    """
    获取两点间距离
    :param p1: 一点
    :param p2: 另一点
    :return: 距离
    """
    return sympy.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


class Angle:
    def __init__(self, p1: Point, vertex: Point, p2: Point):
        """
        角
        :param p1: 一边上的点
        :param vertex: 顶点
        :param p2: 另一边上的点
        """
        self.p1 = p1
        self.vertex = vertex
        self.p2 = p2
        self.val = self._get_value()

    def _get_value(self):
        """
        计算这个角的角度
        :return: 角度的表达式
        """
        # 已知三点坐标：A (X1,Y1) B (X2,Y2) C (X3,Y3)
        # AB向量：(X2-X1,Y2-Y1)
        # AC向量：(X3-X1,Y3-Y1)
        # BC向量：(X3-X2,Y3-Y2)
        # COS∠A=[(X2-X1)(X3-X1)+(Y2-Y1)(Y3-Y1)]/|AB||AC|
        # 其中：|AB|=[(X2-X1)^2+(Y2-Y1)^2]^0.5
        # |AC|=[(X3-X1)^2+(Y3-Y1)^2]^0.5
        # ∠A = Arccos {[(X2-X1)(X3-X1)+(Y2-Y1)(Y3-Y1)]/|AB||AC|}
        return sympy.acos(((self.p1.x - self.vertex.x) * (self.p2.x - self.vertex.x) + (self.p1.y - self.vertex.y) * (
                self.p2.y - self.vertex.y)) / (distance(self.p1, self.vertex) * distance(self.p2, self.vertex)))


if __name__ == '__main__':
    from sympy import Integer

    p1 = Point('A', Integer(1), Integer(0))
    p2 = Point('B', Integer(1), Integer(1))
    l = Line(p1, p2)
    print(l.abc)
    p3 = PointOnLine('C', None, l)
    print(p3)
