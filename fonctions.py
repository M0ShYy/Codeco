import base64

alphabet = "abcdefghijklmnopqrstuvwxyz"


def code_alphanumeric(text):
    code = ""
    text = str(text)
    for i in range(len(text)):
        for j in range(len(alphabet)):
            if text[i] == alphabet[j]:
                a = j + 1
                code = code + "," + str(a)
    return code[1:]


def decode_alphanumeric(code):
    text = ""
    # if type(code) != type([]):
    if not isinstance(code, list):
        code = code.split(",")
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


def code_ascii(text):
    code = ""
    for i in text:
        code = code + " " + format(ord(str(i)), "x")
    return code


def decode_ascii(code):
    text = ""
    code = code.split(":")
    for i in code:
        text = text + i + ' '
    text = bytearray.fromhex(text)
    text = text.decode()
    return text


def code_ascii_key(text, key):
    code = ""
    final = ''
    asc_secret = code_ascii(text)
    asc_key = code_ascii(key)
    asc_key = asc_key.split()
    asc_secret = asc_secret.split()
    for i in range(len(asc_secret)):
        calc = hex((int(asc_secret[i], 16) + int(asc_key[i % len(asc_key)], 16)) % int("7f", 16))
        code = code + " " + calc[2:]
    test = int("10", 16)
    code = str(code)
    code = code.split()
    for i in range(len(code)):
        if int(code[i], 16) < test:
            code[i] = "0" + code[i]
    for i in code:
        final = final + " " + i
    final = decode_ascii(final)
    return final


def decode_ascii_key(code, key):
    text = ""
    final = ''
    asc_secret = code_ascii(code)
    asc_key = code_ascii(key)
    asc_key = asc_key.split()
    asc_secret = asc_secret.split()
    for i in range(len(asc_secret)):
        calc = hex((int(asc_secret[i], 16) - int(asc_key[i % len(asc_key)], 16)) % int("7f", 16))
        text = text + " " + calc[2:]
    test = int("10", 16)
    text = str(text)
    text = text.split()
    for i in range(len(text)):
        if int(text[i], 16) < test:
            text[i] = "0" + text[i]
    for i in text:
        final = final + " " + i
    final = decode_ascii(final)
    return final


def code_base16(text):
    return str(base64.b16encode(text.encode("utf-8")), "utf-8")


def decode_base16(code):
    return str(base64.b16decode(code), "utf-8")


def code_base32(text):
    return str(base64.b32encode(text.encode("utf-8")), "utf-8")

def decode_base32(code):
    return str(base64.b32decode(code), "utf-8")


def code_base64(text):
    return str(base64.b64encode(text.encode("utf-8")), "utf-8")


def decode_base64(code):
    return str(base64.b64decode(code), "utf-8")


def code_base85(text):
    return str(base64.b85encode(text.encode("utf-8")), "utf-8")


def decode_base85(code):
    return str(base64.b85decode(code), "utf-8")


