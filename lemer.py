

def lemer(k, r, x0, n, precision=None):
    k = 1 << k
    result = []
    while n:
        x0 = r * x0 % k
        if precision is not None:
            result.append(round(x0 / k, precision))
        else:
            result.append(x0 / k)

        n -= 1
    return result


# primer30
print(lemer(7, 5, 3, 3, precision=4))
# [0.1172, 0.5859, 0.9297]


# zadacha25
print(lemer(7, 5, 9, 3, precision=4))
# [0.3516, 0.7578, 0.7891]
