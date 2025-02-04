# True: a condição está ok
# False: a condição não foi atingida


def password_minimum_length(password: str) -> bool:
    if len(password) < 16:
        return False
    return True


def password_maximum_length(password: str) -> bool:
    if len(password) >= 129:
        return False
    return True


def password_has_lower_char(password: str) -> bool:
    lower = "abcdefghijklmnopqrstuvwxyz"

    for char in password:
        if char in lower:
            return True
    return False


def password_has_upper_char(password: str) -> bool:
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in password:
        if char in upper:
            return True
    return False


def password_has_digit_char(password: str) -> bool:
    digit = "0123456789"

    for char in password:
        if char in digit:
            return True
    return False


def password_has_punct_char(password: str) -> bool:
    # raw string
    punct = r"""!@#$%^&*()-_=+[]{}|\;:'",.<>?/`~"""

    for char in password:
        if char in punct:
            return True
    return False


def password_has_rep_series(password: str) -> bool:
    rep_number = 3

    for i in range(len(password) - rep_number):
        rep = password[i:i + rep_number]
        rep_letters = set(rep)
        if len(rep_letters) == 1:
            return False
    return True


def password_has_seq_series(password: str) -> bool:
    allchars = "abcdefghijklmnopqrstuvwxyz"
    numerals = "0123456789"
    seq_number = 3

    password = password.lower()

    for i in range(len(password) - seq_number):
        chunck = password[i:i+seq_number]
        if chunck in allchars or chunck in numerals:
            return False
    return True


def password_wordlists_xors(password: str) -> bool:
    known_passwords = []
    with open("assets/worldlists/rockyou-1.txt", "r", encoding="utf-8") as file:
        known_passwords_1 = file.read().splitlines()
    with open("assets/worldlists/rockyou-2.txt", "r", encoding="utf-8") as file:
        known_passwords_2 = file.read().splitlines()
    known_passwords = known_passwords_1 + known_passwords_2

    if password in known_passwords:
        return False
    return True


def password_checker_result(fails: dict[str, bool]) -> list[str]:
    feedback_dict = {
        "minimum_length": "* A senha precisa ter no mínimo 16 caracteres",
        "maximum_length": "* A senha precisa ter no máximo 128 caracteres",
        "has_lower_char": "* A senha precisa ter letras minúsculas",
        "has_upper_char": "* A senha precisa ter letras maiúsculas",
        "has_digit_char": "* A senha precisa ter números",
        "has_punct_char": "* A senha precisa ter caracteres especiais",
        "has_rep_series": "* A senha não pode ter repetições sequenciais de um caracter",
        "has_seq_series": "* A senha não pode conter uma sequência de caracteres",
        "wordlists_xors": "* A senha está em listas públicas de senhas conhecidas",
    }
    feedback_list = []

    if all(fails.values()):
        return ["A senha é forte!"]
    else:
        for fail, value in fails.items():
            if not value:
                warning = feedback_dict.get(fail)
                feedback_list.append(warning)
        return feedback_list


def main():  # pragma: no cover
    password = input("Digite a senha: ")

    minimum_length = password_minimum_length(password)
    maximum_length = password_maximum_length(password)
    has_lower_char = password_has_lower_char(password)
    has_upper_char = password_has_upper_char(password)
    has_punct_char = password_has_punct_char(password)
    has_digit_char = password_has_digit_char(password)
    has_seq_series = password_has_seq_series(password)
    has_rep_series = password_has_rep_series(password)
    wordlists_xors = password_wordlists_xors(password)

    params = {
        "minimum_length": minimum_length | False,
        "maximum_length": maximum_length | False,
        "has_lower_char": has_lower_char | False,
        "has_upper_char": has_upper_char | False,
        "has_digit_char": has_digit_char | False,
        "has_punct_char": has_punct_char | False,
        "has_rep_series": has_rep_series | False,
        "has_seq_series": has_seq_series | False,
        "wordlists_xors": wordlists_xors | False,
    }

    password_checker_result(params)


if __name__ == "__main__":  # pragma: no cover
    main()
