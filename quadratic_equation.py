def discriminant(a, b, c):
    return (b ** 2 - 4*a*c)
def solution(a, b, c):
    if discriminant(a, b, c) > 0:
        x1 = ((-b + (discriminant(a, b, c))**(1/2))/(2 * a))
        x2 = ((-b - (discriminant(a, b, c))**(1/2))/(2 * a))
        return x1, x2
    elif discriminant(a, b, c) == 0:
        x1 = -b/(2 * a)
        return x1
    else:
        return "корней нет"
if __name__ == '__main__':
    print(solution(1, 8, 15))
    print(solution(1, -13, 12))
    print(solution(-4, 28, -49))
    print(solution(6, 7, 7))
