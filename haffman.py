

# Поиск пары, двух самых редких символа
def rariest_duo(probabilities):
    def sort_query(item):
        return (item[1], item[0])

    sorted_probs = sorted(probabilities.items(), key=sort_query)
    result = (sorted_probs[0][0], sorted_probs[1][0])
    return result


# Разбирает строку в соответствии с кодами для символов
def decode_str(chars_dict, encoded_str):
    result = ""
    while encoded_str:
        for char, code in chars_dict.items():
            if encoded_str.startswith(code):
                result += char
                encoded_str = encoded_str[len(code):]
    return result


# Собирает строку в соответствии со словарём кодов для символов
def encode_str(chars_dict, str_to_enc):
    encoded_chars = (chars_dict[char] for char in str_to_enc)
    return ''.join(encoded_chars)


# Алгоритм Хаффмана
def run_huffman(probabilities):
    # Случай для оставшейся пары
    if len(probabilities) == 2:
        special_case = zip(probabilities.keys(), ['0', '1'])
        return dict(special_case)

    # Объединяем пару самых редких букв в слово
    probabilities_prime = probabilities.copy()
    rchar1, rchar2 = rariest_duo(probabilities)
    prob1 = probabilities_prime.pop(rchar1)
    prob2 = probabilities_prime.pop(rchar2)
    # Суммируем их частоты появления
    probabilities_prime[rchar1 + rchar2] = prob1 + prob2

    # Рекурсивно выполняем алгоритм Хаффмана
    result = run_huffman(probabilities_prime)

    # Разбиваем слова на буквы
    resulted_chars = result.pop(rchar1 + rchar2)

    # Добавляем 0 и 1 в конец
    result[rchar2] = resulted_chars + '1'
    result[rchar1] = resulted_chars + '0'

    return result


primer38 = {'а': 15, 'н': 9, 'о': 28, 'е': 25, 'т': 8, 'и': 15}
print(run_huffman(primer38))
# {'о': '10', 'е': '01', 'и': '111', 'а': '110', 'н': '001', 'т': '000'}

zadacha33 = {'а': 16, 'н': 8, 'о': 24, 'е': 27, 'т': 9, 'и': 16}
print(run_huffman(zadacha33))
# {'е': '10', 'о': '01', 'и': '111', 'а': '110', 'т': '001', 'н': '000'}

primer39 = {'е': '10', 'н': '110', 'о': '01', 'т': '111'}
print(encode_str(primer39, 'енот'))
# 1011001111

zadacha34 = run_huffman(zadacha33)
print(encode_str(zadacha34, 'тина'))
# 001111000110

primer40 = {'а': '000', 'и': '001', 'о': '01', 'е': '10', 'н': '110', 'т': '111'}
print(decode_str(primer40, '1100101111'))
# ноот
