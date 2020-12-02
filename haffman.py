from typing import Dict, Tuple


def huffman(probs: Dict[str, int]) -> Dict[str, str]:
    """
    Возвращает для каждого символа соответствующий ему код, на основе его частоты.
    """
    # Частный случай оставшейся пары, просто добавляем 0 и 1 соотв.
    if(len(probs) == 2):
        return dict(zip(probs.keys(), ['0', '1']))

    # Объединяем две буквы и складываем их частоты
    probs_prime = probs.copy()
    char1, char2 = lowest_two_probs(probs)
    p1, p2 = probs_prime.pop(char1), probs_prime.pop(char2)
    probs_prime[char1 + char2] = p1 + p2

    # Рекурсивно собираем код для каждого слова
    codes = huffman(probs_prime)
    # Разъединяем обратно буквы и добавляем остаточные 0 и 1
    code_chars12 = codes.pop(char1 + char2)
    codes[char1], codes[char2] = code_chars12 + '0', code_chars12 + '1'

    return codes


def lowest_two_probs(probs: Dict[str, int]) -> Tuple[str, str]:
    """
    Возвращает пару наиболее редких символов в словаре.
    """
    sorted_probs = sorted(probs.items(), key=lambda i: (i[1], i[0]))
    return sorted_probs[0][0], sorted_probs[1][0]


def huffman_decode(symbol_code: Dict[str, str], encoded: str):
    res = ""
    while encoded:
        for symbol, code in symbol_code.items():
            if encoded.startswith(code):
                res += symbol
                encoded = encoded[len(code):]
    return res


def huffman_encode(symbol_code: Dict[str, str], line: str):
    return ''.join(symbol_code[char] for char in line)


# Примеры
example1 = {'a': 2, 'b': 1, 'c': 1}
#print(huffman(example1))
# {'a': '0', 'b': '10', 'c': '11'}

example2 = {'a': 3, 'b': 3, 'c': 2, 'd': 1, 'e': 1}
#print(huffman(example2))
# {'a': '10', 'b': '11', 'c': '00', 'd': '010', 'e': '011'}

ex38 = {'а': 15, 'н': 9, 'о': 28, 'е': 25, 'т': 8, 'и': 15}
#print(huffman(ex38))

no33 = {'а': 16, 'н': 8, 'о': 24, 'е': 27, 'т': 9, 'и': 16}
#print(huffman(no33))

ex39 = {'е': '10', 'н': '110', 'о': '01', 'т': '111'}
#print(huffman_encode(ex39, 'енот'))

no34 = huffman(no33)
#print(huffman_encode(no34, 'тина'))

ex40 = {'а': '000', 'и': '001', 'о': '01', 'е': '10', 'н': '110', 'т': '111'}
#print(huffman_decode(ex40, '1100101111'))
