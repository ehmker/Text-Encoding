import random
from string import ascii_lowercase


class Caesar:
    # lowercase ascii values range from a = 97 to z = 122
    def __init__(self, shift: int = None) -> None:
        if shift is None:
            self._shift = random.choice(range(1, 26))
        else:
            self._shift = shift % 26

    def encipher(self, text, keep_case=True) -> str:
        print(f"shifting text by {self._shift} characters")
        if self._shift == 0:
            if keep_case:
                return text
            return text.lower()

        cipher_text = ""
        for c in text:
            upper_case = False
            if not c.isalpha():
                cipher_text += c
                continue
            if keep_case and c.isupper():
                upper_case = True
            shifted_index = ((ord(c.lower()) - 97) + self._shift) % 26
            if upper_case:
                cipher_text += ascii_lowercase[shifted_index].upper()
            else:
                cipher_text += ascii_lowercase[shifted_index]
        return cipher_text

    def decipher(self, text, shift=None) -> str:
        decipher_text = ""

        for c in text:
            upper_case = False
            if not c.isalpha():
                decipher_text += c
                continue
            if c.isupper():
                upper_case = True
            shifted_index = ((ord(c.lower()) - 97) - self._shift) % 26
            if upper_case:
                decipher_text += ascii_lowercase[shifted_index].upper()
            else:
                decipher_text += ascii_lowercase[shifted_index]
        return decipher_text

    def change_shift(self, shift=None) -> None:
        if shift == None:
            self._shift = random.choice(range(1, 26))
        else:
            self._shift = shift % 26
        print(f"Character shift changed. Cipher set to shift {self._shift} characters")
        if self._shift == 0:
            print("Warning: shift is currently 0.  Input text will not change")
