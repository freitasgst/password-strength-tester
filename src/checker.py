def password_minimum_length(password: str) -> bool:
    pass


def password_maximum_length(password: str) -> bool:
    pass


def password_has_lower_char(password: str) -> bool:
    pass


def password_has_upper_char(password: str) -> bool:
    pass


def password_has_digit_char(password: str) -> bool:
    pass


def password_has_punct_char(password: str) -> bool:
    pass


def password_has_rep_series(password: str) -> bool:
    pass


def password_has_seq_series(password: str) -> bool:
    pass


def password_wordlists_xors(password: str) -> bool:
    # with open('assets/worldlists/rockyou.txt') as file:
    #     known_passwords = [leak.split() for leak in file]
    pass


def password_checker_result(fails: dict[str, bool]) -> list[str]:
    feedback = {
        "minimum_length": "* A senha precisa ter no mínimo 16 caracteres",
        "maximum_length": "* A senha precisa ter no máximo 128 caracteres",
        "has_lower_char": "* A senha precisa ter letras minúsculas",
        "has_upper_char": "* A senha precisa ter letras maiúsculas",
        "has_digit_char": "* A senha precisa ter números",
        "has_punct_char": "* A senha precisa ter caracteres especiais",
        "has_rep_series": "* A senha não pode conter repetição de um caracter em sequência",
        "has_seq_series": "* A senha não pode conter uma sequência de caracteres",
        "wordlists_xors": "* A senha está em listas públicas de senhas conhecidas"
    }
    pass


def main():  # pragma: no cover
    password = input("Digite a senha: ")

    minimum_length = password_minimum_length(password)
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
        "minimum_length": minimum_length | True,
        "maximum_length": maximum_length | True,
        "has_lower_char": has_lower_char | True,
        "has_upper_char": has_upper_char | True,
        "has_digit_char": has_digit_char | True,
        "has_punct_char": has_punct_char | True,
        "has_rep_series": has_rep_series | True,
        "has_seq_series": has_seq_series | True,
        "wordlists_xors": wordlists_xors | True 
    }

    password_checker_result(params)


if __name__ == "__main__":  # pragma: no cover
    main()
