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
    pass


def main():  # pragma: no cover
    params = {
        "minimum_length": True,
        "maximum_length": True,
        "has_lower_char": True,
        "has_upper_char": True,
        "has_digit_char": True,
        "has_punct_char": True,
        "has_rep_series": True,
        "has_seq_series": True,
        "wordlists_xors": True 
    }


if __name__ == "__main__":  # pragma: no cover
    main()
