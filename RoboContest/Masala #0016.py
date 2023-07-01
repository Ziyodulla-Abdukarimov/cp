def convert_to_uzbek_latin(number):
    singles = ['', 'bir', 'ikki', 'uch', "to'rt", 'besh', 'olti', 'yetti', 'sakkiz', "to'qqiz"]
    tens = ['', 'o\'n', 'yigirma', 'o\'ttiz', "qirq", 'ellik', 'oltmish', 'yetmish', 'sakson', "to'qson"]

    if number == 0:
        return 'nol'

    result = ''
    if number // 1000000000 > 0:
        result += convert_to_uzbek_latin(number // 1000000000) + " milliard "
        number %= 1000000000

    if number // 1000000 > 0:
        result += convert_to_uzbek_latin(number // 1000000) + " million "
        number %= 1000000

    if number // 1000 > 0:
        result += convert_to_uzbek_latin(number // 1000) + " ming "
        number %= 1000

    if number // 100 > 0:
        result += convert_to_uzbek_latin(number // 100) + " yuz "
        number %= 100

    if number >= 20:
        result += tens[number // 10] + ' '
        number %= 10

    if number > 0:
        result += singles[number] + ' '

    return result.strip()


n = int(input())
print(convert_to_uzbek_latin(n))
