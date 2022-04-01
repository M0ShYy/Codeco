alphabet = "abcdefghijklmnopqrstuvwxyz"


def code_alphanumeric(text):
    code = []
    text = str(text)
    for i in range(len(text)):
        for j in range(len(alphabet)):
            if text[i] == alphabet[j]:
                a = j + 1
                code.append(str(a))
    return code


def decode_alphanumeric(code):
    text = ""
    if type(code) != type([]):
        code = code.split()
    for i in code:
        i = int(i) - 1
        text = text + alphabet[i]
    return text


def code_caesar(text):
    code = []
    text = code_alphanumeric(text)
    for i in range(len(text)):
        code.append((int(text[i]) + 3) % 26)
    code = decode_alphanumeric(code)
    return code


def decode_caesar(code):
    text = []
    code = code_alphanumeric(code)
    for i in range(len(code)):
        text.append((int(code[i]) - 3) % 26)
    text = decode_alphanumeric(text)
    return text


def code_keyed(text, key):
    code = []
    text = code_alphanumeric(text)
    key = code_alphanumeric(key)
    for i in range(len(text)):
        code.append((int(text[i]) + int((key[i % len(key)]))) % 26)
    code = decode_alphanumeric(code)
    return code


def decode_keyed(code, key):
    text = []
    code = code_alphanumeric(code)
    key = code_alphanumeric(key)
    for i in range(len(code)):
        text.append((int(code[i]) - int((key[i % len(key)]))) % 26)
    text = decode_alphanumeric(text)
    return text


secret = "my secret"
clef = 'my key'
print(decode_alphanumeric(code_alphanumeric(secret)))
print(decode_caesar(code_caesar(secret)))
print(decode_keyed(code_keyed(secret, clef), clef))
