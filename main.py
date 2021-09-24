import admin as adm
import time


def main():

    print('\033[0;34;40m=== MENU PRINCIPAL ===\033[m')
    print('===============================')
    print('\033[1m1. Para logar como Administrador\033[m\n\033[1m2. Para Cadastrar\033[m\n\033[1m3. Ver Catálogo (Admin)\033[m\n\033[1;31m0. Para Sair\033[m')
    print('===============================')
    op = int(input('Digite a sua OPÇÃO:'))
    if op == 1:
        adm.admin().login()
    elif op == 2:
        adm.admin().cadastro()
    elif op == 3:
        adm.aeronaves().listarAeronave()
    else:
        print('Finalizando o sistma...')
        time.sleep(2)
        return print('Até breve')


if __name__ == '__main__':
    main()
