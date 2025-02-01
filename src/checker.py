def password_minimum_length(password: str) -> tuple[bool, int] | bool:
    pass


def password_maximum_length(password: str) -> tuple[bool, int] | bool:
    pass


def password_has_lower_char(password: str) -> tuple[bool,int] | bool:
    pass


def password_has_upper_char(password: str) -> tuple[bool,int] | bool:
    pass


def password_has_digit_char(password: str) -> tuple[bool,int] | bool:
    pass


def password_has_punct_char(password: str) -> tuple[bool,int] | bool:
    pass


def password_has_rep_series(password: str) -> tuple[bool, int] | bool:
    pass


def password_has_seq_series(password: str) -> tuple[bool, int] | bool:
    pass


def password_checker_result(fails: list[int]) -> list[str]:
    pass


def password_wordlists_xors(password: str) -> tuple[bool, int] | bool:
    with open('assets/worldlists/rockyou.txt') as file:
        known_passwords = [leak.split() for leak in file]
    pass


def main():  # pragma: no cover
    pass


if __name__ == "__main__":  # pragma: no cover
    main()
