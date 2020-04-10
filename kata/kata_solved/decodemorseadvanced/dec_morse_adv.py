def decodeBits(bits):
    if bits[0] == '0':
        bits = bits[1:]
    if bits[len(bits) - 1] == '0':
        bits = bits[:-1]
    arr = bits.split("0")
    while "" in arr:
        arr.remove("")
    x = len(min(arr))
    y = x
    if '0' in bits:
        arr1 = bits.split("1")
        while "" in arr1:
            arr1.remove("")
        y = len(min(arr1))
    if x == y:
        return bits.replace('111' * x, '-').replace('0000000' * x, '   ').replace('000' * x, ' ').replace('1' * x,
                                                                                                          '.').replace(
            '0', '')
    elif x > y:
        return bits.replace('111' * x, '-').replace('0000000' * x, '   ').replace('000' * x, ' ').replace('1' * x,
                                                                                                          '-').replace(
            '0', '')
    else:
        return bits.replace('111' * x, '.').replace('0000000' * x, '   ').replace('000' * x, ' ').replace('1' * x,
                                                                                                          '.').replace(
            '0', '')


def decodeMorse(morse_code):
    a = []
    s = ''
    count = 0
    first = False
    result = morse_code.split(" ")
    for x in result:
        if x == "":
            if count % 2 == 0 and first:
                s += " "
            count += 1
        else:
            t = str(x)
            x = MORSE_CODE[t]
            s += x
            first = True
    if s[len(s) - 1] == " ":
        return s[:-1]
    return s


MORSE_CODE = {'..-.': 'F', '-..-': 'X',
              '.--.': 'P', '-': 'T', '..---': '2',
              '....-': '4', '-----': '0', '--...': '7',
              '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
              '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
              '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
              '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
              '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
              '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}

