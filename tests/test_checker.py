import unittest
from checker import (
    password_minimum_length,
    password_maximum_length,
    password_has_lower_char,
    password_has_upper_char,
    password_has_punct_char,
    password_has_digit_char,
    password_has_seq_series,
    password_has_rep_series,
    password_wordlists_xors,
    password_checker_result,
)


class TestChecker(unittest.TestCase):
    def test_password_minimum_length(self):
        password = "1234567812345678"
        result = password_minimum_length(password)
        self.assertEqual(result, True)
        password = "12345678"
        result = password_minimum_length(password)
        self.assertEqual(result, tuple[False, 0])
        password = "1234"
        result = password_minimum_length(password)
        self.assertEqual(result, tuple[False, 0])

    def test_password_maximum_length(self):
        password = "1" * 64
        result = password_maximum_length(password)
        self.assertEqual(result, True)
        password = "1" * 128
        result = password_maximum_length(password)
        self.assertEqual(result, True)
        password = "1" * 129
        result = password_maximum_length(password)
        self.assertEqual(result, tuple[False, 1])
        password = "1" * 500
        result = password_maximum_length(password)
        self.assertEqual(result, tuple[False, 1])

    def test_password_has_lower_char(self):
        # True
        password = "abcdefgh"
        result = password_has_lower_char(password)
        self.assertEqual(result, True)

        password = "1234abcdefgh"
        result = password_has_lower_char(password)
        self.assertEqual(result, True)

        password = "FDHVJFHabcdefgh"
        result = password_has_lower_char(password)
        self.assertEqual(result, True)

        password = "325435SDFDFDG#@!%#@abcdefgh"
        result = password_has_lower_char(password)
        self.assertEqual(result, True)

        # False
        password = "!@#$#$ˆABCDEFGH"
        result = password_has_lower_char(password)
        self.assertEqual(result, tuple[False, 2])

        password = "ABCDEFGH"
        result = password_has_lower_char(password)
        self.assertEqual(result, tuple[False, 2])

        password = "12345678"
        result = password_has_lower_char(password)
        self.assertEqual(result, tuple[False, 2])

        password = "A1B2C3D4E5F6G7H8"
        result = password_has_lower_char(password)
        self.assertEqual(result, tuple[False, 2])

        password = "!@#$%ˆ&*()"
        result = password_has_lower_char(password)
        self.assertEqual(result, tuple[False, 2])

        password = "!A@S#V$%ˆ&*()"
        result = password_has_lower_char(password)
        self.assertEqual(result, tuple[False, 2])

        password = "1!2@456#$%ˆ&*()"
        result = password_has_lower_char(password)
        self.assertEqual(result, tuple[False, 2])

        password = "!@34534ANDBDJ#$%ˆ&*()"
        result = password_has_lower_char(password)
        self.assertEqual(result, tuple[False, 2])

    def test_password_has_upper_char(self):
        # True
        password = "ABCDEFGH"
        result = password_has_upper_char(password)
        self.assertEqual(result, True)

        password = "!@#$#$ˆABCDEFGH"
        result = password_has_upper_char(password)
        self.assertEqual(result, True)

        password = "FDHVJFHabcdefgh"
        result = password_has_upper_char(password)
        self.assertEqual(result, True)

        password = "325435SDFDFDG#@!%#@abcdefgh"
        result = password_has_upper_char(password)
        self.assertEqual(result, True)

        # False
        password = "asddfghjklh"
        result = password_has_upper_char(password)
        self.assertEqual(result, tuple[False, 3])

        password = "1234abcdefgh"
        result = password_has_upper_char(password)
        self.assertEqual(result, tuple[False, 3])

        password = "12345678"
        result = password_has_upper_char(password)
        self.assertEqual(result, tuple[False, 3])

        password = "a1b2c3d4e5f6g7h8"
        result = password_has_upper_char(password)
        self.assertEqual(result, tuple[False, 3])

        password = "!@#$%ˆ&*()"
        result = password_has_upper_char(password)
        self.assertEqual(result, tuple[False, 3])

        password = "!a@s#v$%ˆ&*()"
        result = password_has_upper_char(password)
        self.assertEqual(result, tuple[False, 3])

        password = "1!2@456#$%ˆ&*()"
        result = password_has_upper_char(password)
        self.assertEqual(result, tuple[False, 3])

        password = "!@34534andbdj#$%ˆ&*()"
        result = password_has_upper_char(password)
        self.assertEqual(result, tuple[False, 3])

    def test_password_has_punct_char(self):
        # True
        password = "!@#$%ˆ&*()"
        result = password_has_punct_char(password)
        self.assertEqual(result, True)

        password = "!@#$#$ˆABCDEFGH"
        result = password_has_punct_char(password)
        self.assertEqual(result, True)

        password = "!a@s#v$%ˆ&*()"
        result = password_has_punct_char(password)
        self.assertEqual(result, True)

        password = "325435SDFDFDG#@!%#@abcdefgh"
        result = password_has_punct_char(password)
        self.assertEqual(result, True)

        password = "1!2@456#$%ˆ&*()"
        result = password_has_punct_char(password)
        self.assertEqual(result, True)

        password = "!@34534andbdj#$%ˆ&*()"
        result = password_has_punct_char(password)
        self.assertEqual(result, True)

        # False
        password = "asddfghjklh"
        result = password_has_punct_char(password)
        self.assertEqual(result, tuple[False, 4])

        password = "1234abcdefgh"
        result = password_has_punct_char(password)
        self.assertEqual(result, tuple[False, 4])

        password = "12345678"
        result = password_has_punct_char(password)
        self.assertEqual(result, tuple[False, 4])

        password = "a1b2c3d4e5f6g7h8"
        result = password_has_punct_char(password)
        self.assertEqual(result, tuple[False, 4])

        password = "ABCDEFGH"
        result = password_has_punct_char(password)
        self.assertEqual(result, tuple[False, 4])

        password = "FDHVJFHabcdefgh"
        result = password_has_punct_char(password)
        self.assertEqual(result, tuple[False, 4])

    def test_password_has_digit_char(self):
        # True
        password = "12345678"
        result = password_has_digit_char(password)
        self.assertEqual(result, True)

        password = "1234abcdefgh"
        result = password_has_digit_char(password)
        self.assertEqual(result, True)

        password = "a1b2c3d4e5f6g7h8"
        result = password_has_digit_char(password)
        self.assertEqual(result, True)

        password = "325435SDFDFDG#@!%#@abcdefgh"
        result = password_has_digit_char(password)
        self.assertEqual(result, True)

        password = "1!2@456#$%ˆ&*()"
        result = password_has_digit_char(password)
        self.assertEqual(result, True)

        password = "!@34534andbdj#$%ˆ&*()"
        result = password_has_digit_char(password)
        self.assertEqual(result, True)

        # False
        password = "asddfghjklh"
        result = password_has_digit_char(password)
        self.assertEqual(result, tuple[False, 5])

        password = "ABCDEFGH"
        result = password_has_digit_char(password)
        self.assertEqual(result, tuple[False, 5])

        password = "FDHVJFHabcdefgh"
        result = password_has_digit_char(password)
        self.assertEqual(result, tuple[False, 5])

        password = "!a@s#v$%ˆ&*()"
        result = password_has_digit_char(password)
        self.assertEqual(result, tuple[False, 5])

        password = "!@#$#$ˆABCDEFGH"
        result = password_has_digit_char(password)
        self.assertEqual(result, tuple[False, 5])

        password = "!@#$%ˆ&*()"
        result = password_has_digit_char(password)
        self.assertEqual(result, tuple[False, 5])

    def test_password_has_seq_series(self):
        password = "algnhots"
        result = password_has_seq_series(password)
        self.assertEqual(result, True)
        password = "12345678"
        result = password_has_seq_series(password)
        self.assertEqual(result, tuple[False, 6])
        password = "abcdefgh"
        result = password_has_seq_series(password)
        self.assertEqual(result, tuple[False, 6])
        password = "ABCDEFGH"
        result = password_has_seq_series(password)
        self.assertEqual(result, tuple[False, 6])
        password = "789ahexxumk"
        result = password_has_seq_series(password)
        self.assertEqual(result, tuple[False, 6])
        password = "ahexyzxxumk"
        result = password_has_seq_series(password)
        self.assertEqual(result, tuple[False, 6])
        password = "ahexxuFGHmk"
        result = password_has_seq_series(password)
        self.assertEqual(result, tuple[False, 6])
        password = "123abcABC"
        result = password_has_seq_series(password)
        self.assertEqual(result, tuple[False, 6])

    def test_password_has_rep_series(self):
        password = "algnhots"
        result = password_has_rep_series(password)
        self.assertEqual(result, True)
        password = "11111111"
        result = password_has_rep_series(password)
        self.assertEqual(result, tuple[False, 7])
        password = "aaaaaaaa"
        result = password_has_rep_series(password)
        self.assertEqual(result, tuple[False, 7])
        password = "GGGGGGGG"
        result = password_has_rep_series(password)
        self.assertEqual(result, tuple[False, 7])
        password = "555ahexxumk"
        result = password_has_rep_series(password)
        self.assertEqual(result, tuple[False, 7])
        password = "ahehhhxxumk"
        result = password_has_rep_series(password)
        self.assertEqual(result, tuple[False, 7])
        password = "ahexxuZZZmk"
        result = password_has_rep_series(password)
        self.assertEqual(result, tuple[False, 7])
        password = "111aaaBBB"
        result = password_has_rep_series(password)
        self.assertEqual(result, tuple[False, 7])

    def test_password_wordlists_xors(self):
        password = "YUpb/W@7:h;.x8m6-%[=jC"
        result = password_wordlists_xors(password)
        self.assertEqual(result, True)
        password = "wL9:PHBb=/}Wtze46^87A{"
        result = password_wordlists_xors(password)
        self.assertEqual(result, True)
        password = "L{z;w/#6*9]kP$yZxpuY+b"
        result = password_wordlists_xors(password)
        self.assertEqual(result, True)
        password = "bMG8_9w<Q3mS7$u;:pn@sP"
        result = password_wordlists_xors(password)
        self.assertEqual(result, True)
        password = "KVaQ(gRcs3A5w$UC*tWP.z"
        result = password_wordlists_xors(password)
        self.assertEqual(result, True)
        password = "password123"
        result = password_wordlists_xors(password)
        self.assertEqual(result, tuple[False, 8])
        password = "iloveyou"
        result = password_wordlists_xors(password)
        self.assertEqual(result, tuple[False, 8])

    def test_password_checker_result(self):
        fails = [0]
        result = password_checker_result(fails)
        self.assertEqual(result, ["* A senha precisa ter no mínimo 16 caracteres"])
        fails = [1]
        result = password_checker_result(fails)
        self.assertEqual(result, ["* A senha precisa ter no máximo 128 caracteres"])
        fails = [2]
        result = password_checker_result(fails)
        self.assertEqual(result, ["* A senha precisa ter letras minúsculas"])
        fails = [3]
        result = password_checker_result(fails)
        self.assertEqual(result, ["* A senha precisa ter letras maiúsculas"])
        fails = [4]
        result = password_checker_result(fails)
        self.assertEqual(result, ["* A senha precisa ter caracteres especiais"])
        fails = [5]
        result = password_checker_result(fails)
        self.assertEqual(result, ["* A senha precisa ter números"])
        fails = [6]
        result = password_checker_result(fails)
        self.assertEqual(
            result, ["* A senha não pode conter uma sequência de caracteres"]
        )
        fails = [7]
        result = password_checker_result(fails)
        self.assertEqual(
            result, ["* A senha não pode ter repetições sequenciais de um caracter"]
        )
        fails = [8]
        result = password_checker_result(fails)
        self.assertEqual(
            result, ["* A senha está em listas públicas de senhas conhecidas"]
        )
        fails = [0, 5, 8]
        result = password_checker_result(fails)
        self.assertEqual(
            result,
            [
                "* A senha precisa ter no mínimo 8 caracteres",
                "* A senha precisa ter números",
                "* A senha está em listas públicas de senhas conhecidas",
            ],
        )
