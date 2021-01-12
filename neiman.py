
# Метод Неймана для получения последовательности ПСЧ
def neiman(r0, r0_exponent, k, n):
    # Запись числа производится в формате 1234 * 10^-4
    e10 = -r0_exponent
    result = []
    while n:
        # Отступ "с краю"
        m = (e10-k) / 2
        # Выделяем среднюю часть из числа
        r0 = (r0 % pow(10, 2*k-m)) // pow(10, m)
        e10 = k
        result.append(r0)
        # Возводим в квадрат
        e10 *= 2
        r0 *= r0

        n -= 1
    # Применяем экспоненту
    exponent_inv = pow(10, k)
    return list(r / exponent_inv for r in result)


# primer29
print(neiman(8374, -4, 4, 4))
# [0.8374, 0.1238, 0.5326, 0.3662]

# zadacha24
print(neiman(9147, -4, 4, 4))
# [0.9147, 0.6676, 0.5689, 0.3647]
