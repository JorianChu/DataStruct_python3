#encoding = utf-8
"""
@version:0.1
@author: jorian
@time: 2020/12/4  13:30
"""


def gcd(a, b):
    while b:
        r = a % b
        # 经过一次求余数，进入第二轮相除，即b的值扮演了被除数的角色
        a = b
        # r的值扮演了余数的角色
        b = r
    # 这里return a的原因是，b作为在最后一轮的除数已经幅值给了a
    return a


def lcm(a, b):
    return a*b // gcd(a, b)


def three_gcd(a, b, c):
    return gcd(gcd(a, b), c)


def three_lcm(a, b, c):
    return lcm(a, lcm(b,c))


def main():
    a = 2
    b = 7
    c = 6
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("gcd(", a, ", ", b, ", ", c, "):", three_gcd(a, b, c))
    print("lcm(", a, ", ", b, ", ", c, "):", three_lcm(a, b, c))


if __name__ == '__main__':
    main()