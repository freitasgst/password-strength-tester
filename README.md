[![Python](https://img.shields.io/badge/python-3.12-green)](https://www.python.org)
[![Tests](https://github.com/freitasgst/password-strength-tester/workflows/Tests/badge.svg)](https://github.com/freitasgst/password-strength-tester/actions)
# Password Strength Tester
Tests a password's strength according to [OWASP Guidelines for enforcing secure passwords](https://github.com/OWASP/ASVS/blob/master/4.0/en/0x11-V2-Authentication.md#v21-password-security-requirements) and [Cartilha de Segurança para Internet, Fascículo SENHAS do cert.br](https://www.nic.br/media/docs/publicacoes/13/fasciculo-senhas.pdf)

Inspired by the [owasp-password-strength-test](https://github.com/nowsecure/owasp-password-strength-test)

## Requirements
- Make
- Python 3.13
- Pip >= 21.0.1
- Other requirements: 
    - requirements.txt 
    - requirements-dev.txt (development dependencies)

## Usage
```
make install
```

## Contributing

### Installing dev environment requirements:
```
make install-dev
```

### Testing
```
make coverage
```
