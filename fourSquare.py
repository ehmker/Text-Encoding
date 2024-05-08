import random
import re


class FourSquare:
    def __init__(self, key1: str = None, key2: str = None, exclude_q=True) -> None:
        # If q is ignored or i&j are combined
        if exclude_q:
            self.exclude_q = True
            self.alphabet = "abcdefghijklmnoprstuvwxyz"
        else:
            self.exclude_q = False
            self.alphabet = "abcdefghiklmnopqrstuvwxyz"

        self.key = [
            self._build_key_matrix(list(self.alphabet)),
            None,
            None,
            self._build_key_matrix(list(self.alphabet)),
        ]

        if key1 is None:
            self.key[1] = self._build_key_matrix(
                random.sample(self.alphabet, len(self.alphabet))
            )
        else:
            self.key[1] = self._build_key_matrix(list(key1), True)

        if key2 is None:
            self.key[2] = self._build_key_matrix(
                random.sample(self.alphabet, len(self.alphabet))
            )
        else:
            self.key[2] = self._build_key_matrix(list(key2), True)

    def encipher(self, text):
        cipher_text = ""
        text = self._prep_text(text)
        partion_pairs = self._partition(text)

        for pair in partion_pairs:
            # print(f"Applying cipher to pair: {pair}")
            i = self.alphabet.index(pair[0]) // 5
            j = self.alphabet.index(pair[0]) % 5
            k = self.alphabet.index(pair[1]) // 5
            l = self.alphabet.index(pair[1]) % 5
            # print(f"{pair[0]} => ({i},{j}) ==>> ({i},{l}) {self.key[1][i][l]}")
            # print(f"{pair[1]} => ({k},{l}) ==>> ({k},{j}) {self.key[2][k][j]}")
            # print("====================================")
            cipher_text += self.key[1][i][l] + self.key[2][k][j] + " "
        # self._print_key_matrix()
        return cipher_text

    def decipher(self, text):
        deciphered = ""
        text = self._prep_text(text)
        partion_pairs = self._partition(text)
        key1 = "".join(char for row in self.key[1] for char in row)
        key2 = "".join(char for row in self.key[2] for char in row)

        for pair in partion_pairs:
            print(f"Applying cipher to pair: {pair}")
            i = key1.index(pair[0]) // 5
            j = key1.index(pair[0]) % 5
            k = key2.index(pair[1]) // 5
            l = key2.index(pair[1]) % 5
            # print(f"{pair[0]} => ({i},{j}) ==>> ({i},{l}) {self.key[0][i][l]}")
            # print(f"{pair[1]} => ({k},{l}) ==>> ({k},{j}) {self.key[3][k][j]}")
            # print("====================================")
            deciphered += self.key[0][i][l] + self.key[3][k][j]
        self._print_key_matrix()
        return deciphered

    def _prep_text(self, text):
        # removing punctuation, whitespace, and ensuring the resulting string is even in length
        pattern = r"[^a-zA-Z\s]"
        text = text.lower()
        text = re.sub(pattern, "", text)
        text = text.replace(" ", "")
        if len(text) % 2 == 1:
            text += "x"
        if self.exclude_q:
            text = text.replace("q", "x")
        else:
            text = text.replace("j", "i")
        return text

    def _partition(self, text):
        partitons = []
        for i in range(0, len(text), 2):
            partitons.append((text[i], text[i + 1]))
        return partitons

    def _build_key_matrix(self, key, user_generated=False):
        key_mx = []

        if user_generated:
            formated = ""
            unused = self.alphabet
            for char in key:
                if char in formated:
                    if len(formated) == 25:
                        break
                    continue
                formated += char
                unused = unused.replace(char, "")

            formated += unused
            for i in range(0, 25, 5):
                key_mx.append(list(formated[i : i + 5]))
            return key_mx

        for i in range(0, 25, 5):
            key_mx.append(key[i : i + 5])
        return key_mx

    def _print_key_matrix(self):
        for i in range(0, 4, 2):
            for j in range(len(self.key[i])):
                print(f"{self.key[i][j]}  {self.key[i + 1][j]}")
            print()

    # def get_keys(self):
    #     return
