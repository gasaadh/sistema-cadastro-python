def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Tipo de dado informado está incorreto.\033[31m')
            continue

        except (KeyboardInterrupt):
            print(f'\nO usuário preferiu não informar um número.')
            return 0

        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))

        except (ValueError, TypeError):
            print('Tipo de dado informado está incorreto.')
            continue
        except (KeyboardInterrupt):
            print(f'\nO usuário preferiu não informar um número.')
            return 0

        else:
            return num

