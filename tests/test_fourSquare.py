import unittest
from fourSquare import FourSquare
import random


class testFourSquare(unittest.TestCase):

    def test__build_key_matrix(self):
        self.maxDiff = None
        random.seed(9)
        c = FourSquare()
        self.assertEqual(
            c.key,
            [
                [
                    ["a", "b", "c", "d", "e"],
                    ["f", "g", "h", "i", "j"],
                    ["k", "l", "m", "n", "o"],
                    ["p", "r", "s", "t", "u"],
                    ["v", "w", "x", "y", "z"],
                ],
                [
                    ["o", "u", "l", "i", "e"],
                    ["f", "a", "k", "r", "z"],
                    ["p", "j", "b", "y", "w"],
                    ["n", "t", "g", "m", "x"],
                    ["d", "v", "s", "c", "h"],
                ],
                [
                    ["b", "d", "e", "r", "t"],
                    ["c", "m", "y", "j", "g"],
                    ["k", "s", "l", "p", "z"],
                    ["x", "n", "v", "u", "h"],
                    ["a", "o", "f", "w", "i"],
                ],
                [
                    ["a", "b", "c", "d", "e"],
                    ["f", "g", "h", "i", "j"],
                    ["k", "l", "m", "n", "o"],
                    ["p", "r", "s", "t", "u"],
                    ["v", "w", "x", "y", "z"],
                ],
            ],
        )

        b = FourSquare("testing", "woroods")
        self.assertEqual(
            b.key,
            [
                [
                    ["a", "b", "c", "d", "e"],
                    ["f", "g", "h", "i", "j"],
                    ["k", "l", "m", "n", "o"],
                    ["p", "r", "s", "t", "u"],
                    ["v", "w", "x", "y", "z"],
                ],
                [
                    ["t", "e", "s", "i", "n"],
                    ["g", "a", "b", "c", "d"],
                    ["f", "h", "j", "k", "l"],
                    ["m", "o", "p", "r", "u"],
                    ["v", "w", "x", "y", "z"],
                ],
                [
                    ["w", "o", "r", "d", "s"],
                    ["a", "b", "c", "e", "f"],
                    ["g", "h", "i", "j", "k"],
                    ["l", "m", "n", "p", "t"],
                    ["u", "v", "x", "y", "z"],
                ],
                [
                    ["a", "b", "c", "d", "e"],
                    ["f", "g", "h", "i", "j"],
                    ["k", "l", "m", "n", "o"],
                    ["p", "r", "s", "t", "u"],
                    ["v", "w", "x", "y", "z"],
                ],
            ],
        )

        a = FourSquare("testing", "woroods", exclude_q=False)
        self.assertEqual(
            a.key,
            [
                [
                    ["a", "b", "c", "d", "e"],
                    ["f", "g", "h", "i", "k"],
                    ["l", "m", "n", "o", "p"],
                    ["q", "r", "s", "t", "u"],
                    ["v", "w", "x", "y", "z"],
                ],
                [
                    ["t", "e", "s", "i", "n"],
                    ["g", "a", "b", "c", "d"],
                    ["f", "h", "k", "l", "m"],
                    ["o", "p", "q", "r", "u"],
                    ["v", "w", "x", "y", "z"],
                ],
                [
                    ["w", "o", "r", "d", "s"],
                    ["a", "b", "c", "e", "f"],
                    ["g", "h", "i", "k", "l"],
                    ["m", "n", "p", "q", "t"],
                    ["u", "v", "x", "y", "z"],
                ],
                [
                    ["a", "b", "c", "d", "e"],
                    ["f", "g", "h", "i", "k"],
                    ["l", "m", "n", "o", "p"],
                    ["q", "r", "s", "t", "u"],
                    ["v", "w", "x", "y", "z"],
                ],
            ],
        )

    def test__prep_text(self):
        c = FourSquare()
        text1 = "ter th4es and # 231, 23511.."
        self.assertEqual(c._prep_text(text1), "terthesand")

    def test__partition(self):
        c = FourSquare()
        text1 = "secrettext"
        self.assertEqual(
            c._partition(text1),
            [("s", "e"), ("c", "r"), ("e", "t"), ("t", "e"), ("x", "t")],
        )
