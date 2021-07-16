import math


def quadratic_equation(a, b, c):
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    if dis > 0:
        a1 = (-b + sqrt_val)/(2 * a)
        b1 = (-b - sqrt_val)/(2 * a)
        ans = []
        ans.append(int(a1))
        ans.append(int(b1))
        print(tuple(ans))
    elif dis == 0:
        print(tuple(-b / (2 * a),))
    else:
        a2 = (- b / (2 * a), " + i", sqrt_val)
        b2 = (- b / (2 * a), " - i", sqrt_val)
        ans2 = []
        ans2.append(int(a2))
        ans2.append(int(b2))
        print(tuple(ans2))


quadratic_equation(2, 10, 8)


# OUTPUT:-
# (-1, -4)
