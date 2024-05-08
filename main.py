from caesar import Caesar
from string import ascii_lowercase
from fourSquare import FourSquare
import random
import re


def check_len(text):
    if len(text) % 2 == 1:
        text += "x"


def main():
    random.seed(9)
    # text = "the quIck brown fox"
    # cipher = Caesar()
    # cipher_text = cipher.encipher(text)
    # print(cipher_text, "\n")
    # print(cipher.decipher(cipher_text))

    # print(-4 % 26)

    # text = "ter thes and # 231, 23511.."
    # pattern = r"[^a-zA-Z\s]"
    # text = re.sub(pattern, "", text)
    # text = text.replace(" ", "")
    # if len(text) % 2 == 1:
    #     text += "x"
    # print(re.sub(pattern, "", text))
    # partitons = []
    # for i in range(0, len(text), 2):
    #     partitons.append((text[i], text[i + 1]))
    # print(partitons)
    key_mx = []
    x = "abcdefghijklmnoprstuvwxyz"
    for i in range(0, 25, 5):
        key_mx.append(x[i : i + 5])

    # print(key_mx)
    # alphabet = "abcdefghijklmnoprstuvwxyz"
    # print(random.sample(alphabet, len(alphabet)))

    # c = FourSquare()
    # for i in key_mx:
    #     print(i)
    c = FourSquare("testing", "woroods")
    text1 = "roecrettext"
    # p = c._partition(text1)
    # print(c.encipher(text1))
    cipher_text = c.encipher(text1)

    print(c.decipher(cipher_text))


main()
