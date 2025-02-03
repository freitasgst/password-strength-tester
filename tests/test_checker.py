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
        self.assertEqual(result, False)
        password = "1234"
        result = password_minimum_length(password)
        self.assertEqual(result, False)

    def test_password_maximum_length(self):
        password = "1" * 64
        result = password_maximum_length(password)
        self.assertEqual(result, True)
        password = "1" * 128
        result = password_maximum_length(password)
        self.assertEqual(result, True)
        password = "1" * 129
        result = password_maximum_length(password)
        self.assertEqual(result, False)
        password = "1" * 500
        result = password_maximum_length(password)
        self.assertEqual(result, False)

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
        self.assertEqual(result, False)

        password = "ABCDEFGH"
        result = password_has_lower_char(password)
        self.assertEqual(result, False)

        password = "12345678"
        result = password_has_lower_char(password)
        self.assertEqual(result, False)

        password = "A1B2C3D4E5F6G7H8"
        result = password_has_lower_char(password)
        self.assertEqual(result, False)

        password = "!@#$%ˆ&*()"
        result = password_has_lower_char(password)
        self.assertEqual(result, False)

        password = "!A@S#V$%ˆ&*()"
        result = password_has_lower_char(password)
        self.assertEqual(result, False)

        password = "1!2@456#$%ˆ&*()"
        result = password_has_lower_char(password)
        self.assertEqual(result, False)

        password = "!@34534ANDBDJ#$%ˆ&*()"
        result = password_has_lower_char(password)
        self.assertEqual(result, False)

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
        self.assertEqual(result, False)

        password = "1234abcdefgh"
        result = password_has_upper_char(password)
        self.assertEqual(result, False)

        password = "12345678"
        result = password_has_upper_char(password)
        self.assertEqual(result, False)

        password = "a1b2c3d4e5f6g7h8"
        result = password_has_upper_char(password)
        self.assertEqual(result, False)

        password = "!@#$%ˆ&*()"
        result = password_has_upper_char(password)
        self.assertEqual(result, False)

        password = "!a@s#v$%ˆ&*()"
        result = password_has_upper_char(password)
        self.assertEqual(result, False)

        password = "1!2@456#$%ˆ&*()"
        result = password_has_upper_char(password)
        self.assertEqual(result, False)

        password = "!@34534andbdj#$%ˆ&*()"
        result = password_has_upper_char(password)
        self.assertEqual(result, False)

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
        self.assertEqual(result, False)

        password = "1234abcdefgh"
        result = password_has_punct_char(password)
        self.assertEqual(result, False)

        password = "12345678"
        result = password_has_punct_char(password)
        self.assertEqual(result, False)

        password = "a1b2c3d4e5f6g7h8"
        result = password_has_punct_char(password)
        self.assertEqual(result, False)

        password = "ABCDEFGH"
        result = password_has_punct_char(password)
        self.assertEqual(result, False)

        password = "FDHVJFHabcdefgh"
        result = password_has_punct_char(password)
        self.assertEqual(result, False)

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
        self.assertEqual(result, False)

        password = "ABCDEFGH"
        result = password_has_digit_char(password)
        self.assertEqual(result, False)

        password = "FDHVJFHabcdefgh"
        result = password_has_digit_char(password)
        self.assertEqual(result, False)

        password = "!a@s#v$%ˆ&*()"
        result = password_has_digit_char(password)
        self.assertEqual(result, False)

        password = "!@#$#$ˆABCDEFGH"
        result = password_has_digit_char(password)
        self.assertEqual(result, False)

        password = "!@#$%ˆ&*()"
        result = password_has_digit_char(password)
        self.assertEqual(result, False)

    def test_password_has_seq_series(self):
        password = "algnhots"
        result = password_has_seq_series(password)
        self.assertEqual(result, True)
        password = "12345678"
        result = password_has_seq_series(password)
        self.assertEqual(result, False)
        password = "abcdefgh"
        result = password_has_seq_series(password)
        self.assertEqual(result, False)
        password = "ABCDEFGH"
        result = password_has_seq_series(password)
        self.assertEqual(result, False)
        password = "789ahexxumk"
        result = password_has_seq_series(password)
        self.assertEqual(result, False)
        password = "ahexyzxxumk"
        result = password_has_seq_series(password)
        self.assertEqual(result, False)
        password = "ahexxuFGHmk"
        result = password_has_seq_series(password)
        self.assertEqual(result, False)
        password = "123abcABC"
        result = password_has_seq_series(password)
        self.assertEqual(result, False)

    def test_password_has_rep_series(self):
        password = "algnhots"
        result = password_has_rep_series(password)
        self.assertEqual(result, True)
        password = "11111111"
        result = password_has_rep_series(password)
        self.assertEqual(result, False)
        password = "aaaaaaaa"
        result = password_has_rep_series(password)
        self.assertEqual(result, False)
        password = "GGGGGGGG"
        result = password_has_rep_series(password)
        self.assertEqual(result, False)
        password = "555ahexxumk"
        result = password_has_rep_series(password)
        self.assertEqual(result, False)
        password = "ahehhhxxumk"
        result = password_has_rep_series(password)
        self.assertEqual(result, False)
        password = "ahexxuZZZmk"
        result = password_has_rep_series(password)
        self.assertEqual(result, False)
        password = "111aaaBBB"
        result = password_has_rep_series(password)
        self.assertEqual(result, False)

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
        self.assertEqual(result, False)
        password = "iloveyou"
        result = password_wordlists_xors(password)
        self.assertEqual(result, False)

    def test_password_checker_result(self):
        params = {
            "minimum_length": False,
            "maximum_length": True,
            "has_lower_char": True,
            "has_upper_char": True,
            "has_digit_char": True,
            "has_punct_char": True,
            "has_rep_series": True,
            "has_seq_series": True,
            "wordlists_xors": True
        }
        result = password_checker_result(params)
        self.assertEqual(result, ["* A senha precisa ter no mínimo 16 caracteres"])
        params = {
            "minimum_length": True,
            "maximum_length": False,
            "has_lower_char": True,
            "has_upper_char": True,
            "has_digit_char": True,
            "has_punct_char": True,
            "has_rep_series": True,
            "has_seq_series": True,
            "wordlists_xors": True
        }
        result = password_checker_result(params)
        self.assertEqual(result, ["* A senha precisa ter no máximo 128 caracteres"])
        params = {
            "minimum_length": True,
            "maximum_length": True,
            "has_lower_char": False,
            "has_upper_char": True,
            "has_digit_char": True,
            "has_punct_char": True,
            "has_rep_series": True,
            "has_seq_series": True,
            "wordlists_xors": True
        }
        result = password_checker_result(params)
        self.assertEqual(result, ["* A senha precisa ter letras minúsculas"])
        params = {
            "minimum_length": True,
            "maximum_length": True,
            "has_lower_char": True,
            "has_upper_char": False,
            "has_digit_char": True,
            "has_punct_char": True,
            "has_rep_series": True,
            "has_seq_series": True,
            "wordlists_xors": True
        }
        result = password_checker_result(params)
        self.assertEqual(result, ["* A senha precisa ter letras maiúsculas"])
        params = {
            "minimum_length": True,
            "maximum_length": True,
            "has_lower_char": True,
            "has_upper_char": True,
            "has_digit_char": True,
            "has_punct_char": False,
            "has_rep_series": True,
            "has_seq_series": True,
            "wordlists_xors": True
        }
        result = password_checker_result(params)
        self.assertEqual(result, ["* A senha precisa ter caracteres especiais"])
        params = {
            "minimum_length": True,
            "maximum_length": True,
            "has_lower_char": True,
            "has_upper_char": True,
            "has_digit_char": False,
            "has_punct_char": True,
            "has_rep_series": True,
            "has_seq_series": True,
            "wordlists_xors": True
        }
        result = password_checker_result(params)
        self.assertEqual(result, ["* A senha precisa ter números"])
        params = {
            "minimum_length": True,
            "maximum_length": True,
            "has_lower_char": True,
            "has_upper_char": True,
            "has_digit_char": True,
            "has_punct_char": True,
            "has_rep_series": True,
            "has_seq_series": False,
            "wordlists_xors": True
        }
        result = password_checker_result(params)
        self.assertEqual(
            result, ["* A senha não pode conter uma sequência de caracteres"]
        )
        params = {
            "minimum_length": True,
            "maximum_length": True,
            "has_lower_char": True,
            "has_upper_char": True,
            "has_digit_char": True,
            "has_punct_char": True,
            "has_rep_series": False,
            "has_seq_series": True,
            "wordlists_xors": True
        }
        result = password_checker_result(params)
        self.assertEqual(
            result, ["* A senha não pode ter repetições sequenciais de um caracter"]
        )
        params = {
            "minimum_length": True,
            "maximum_length": True,
            "has_lower_char": True,
            "has_upper_char": True,
            "has_digit_char": True,
            "has_punct_char": True,
            "has_rep_series": True,
            "has_seq_series": True,
            "wordlists_xors": False
        }
        result = password_checker_result(params)
        self.assertEqual(
            result, ["* A senha está em listas públicas de senhas conhecidas"]
        )
        params = {
            "minimum_length": False,
            "maximum_length": True,
            "has_lower_char": True,
            "has_upper_char": True,
            "has_digit_char": False,
            "has_punct_char": True,
            "has_rep_series": True,
            "has_seq_series": True,
            "wordlists_xors": False
        }
        result = password_checker_result(params)
        self.assertEqual(
            result,
            [
                "* A senha precisa ter no mínimo 8 caracteres",
                "* A senha precisa ter números",
                "* A senha está em listas públicas de senhas conhecidas",
            ],
        )
        params = {
            "minimum_length": False,
            "maximum_length": False,
            "has_lower_char": False,
            "has_upper_char": False,
            "has_digit_char": False,
            "has_punct_char": False,
            "has_rep_series": False,
            "has_seq_series": False,
            "wordlists_xors": False
        }
        result = password_checker_result(params)
        self.assertEqual(result, ["A senha é forte!"])
