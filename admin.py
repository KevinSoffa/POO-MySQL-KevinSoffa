import time
import pymysql.cursors
import main


class admin():
    def __init__(self):
        pass

    def conexao(self):
        try:
            self.banco = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='projetoaeronave',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('ERRO ao conectar com o Banco de Dados !')


    def login(self):
        global autenticado
        self.conexao()
        email = input('E-mail: ')
        senha = input('Senha: ')
        try:
            with self.banco.cursor() as cursos:
                cursos.execute('SELECT * FROM admin')
                resultados = cursos.fetchall()
                print('Conectado')
        except:
            print('ERRO ao fazer a consulta com o bd admin')
        for i in resultados:
            if email == i['email'] and senha == i['senha']:
                autenticado = True
                break
            else:
                autenticado = False
                pass
        if autenticado:
            self.menuAdmin()
        else:
            print('Dados incorretos! Tente novamente')
            self.login()

    def VerificarEmail(self, email):
        self.conexao()
        try:
            with self.banco.cursor() as cursos:
                cursos.execute('SELECT * FROM admin')
                resultados = cursos.fetchall()
                print('Conectado')
                self.menuAdmin()
        except:
            print('ERRO ao fazer a consulta com o bd admin')
        for i in resultados:
            if email == i['email']:
                return 1
            else:
                pass
            return 0


    def cadastro(self):
        cod = '123'
        codigo = input('Digi o código de verificação:')
        if codigo == cod:
            nome = input('Nome: ')
            email = input('E-mail: ')
            senha = input('Senha: ')
            dados = [nome, email, senha, 1]
            self.conexao()
            n = self.VerificarEmail(email)
            if n == 1:
                print('E-mail já cadastrado!!! Tente Novamente')
                self.login()
            else:
                with self.banco.cursor() as cursos:
                    sql = "INSERT INTO admin (nome, email, senha, status) VALUES (%s, %s, %s, %s)"
                    cursos.execute(sql, dados)
                    self.banco.commit()
                    print('Novo usuário CADASTRADO COM SUCESSO!!!')
                    self.login()

    def menuAdmin(self):
        print('------------------------------')
        print('\n \033[0;34;40m== Área do Administrador ==\033[m')
        print('------------------------------')
        print('1. Cadastrar nova aeronave\n2. Alterar dados da aeronaves\n3. Deletar Aeronave\n4. Listar Aeronave\n\033[1;31m0. Sair\033[m')
        op = int(input('Digite sua escolha: '))
        if op == 0:
            print('Finalizando o sistma...')
            time.sleep(2)
            return print('Até breve')
        elif op == 1:
            modelo = input('Modelo: ')
            ano = int(input('Ano do modelo: '))
            cor = input('Cor da Aeronave: ')
            tipo = int(input('Tipo (1. Avião | 2. Helicóptero | 3. Drone): '))
            dadosAeronaves = [modelo, ano, cor, tipo]
            aeronaves().cadastrarAeronave(dadosAeronaves)
        elif op == 2:
            aeronaves().alterarAeronave()

        elif op == 3:
            aeronaves().deletarAeronave()

        elif op == 4:
            aeronaves().listarAeronave()


class aeronaves(admin):
    def __init__(self):
        pass

    def cadastrarAeronave(self, dadosAeronave):
        self.conexao()
        with self.banco.cursor() as cursos:
            sql = "INSERT INTO aeronaves (modelo, ano, cor, tipo) VALUES (%s, %s, %s, %s)"
            cursos.execute(sql, dadosAeronave)
            self.banco.commit()
            print('Aeronave CADASTRADA!!!')
            self.menuAdmin()

    def listarAeronave(self):
        self.conexao()
        try:
            with self.banco.cursor() as cursos:
                cursos.execute('SELECT * FROM aeronaves')
                aeronaves = cursos.fetchall()
        except:
            print('Erro ao consultar com DB aeronaves')
        print('\n=-=-=-=-==-=-=-=-=-=-=-=\n=> Lista de Aeronaves <=\n=-=-=-=-==-=-=-=-=-=-=-=')
        for i in aeronaves:
            if i['tipo'] == 1:
                tipo = 'Avião'

            elif i['tipo'] == 2:
                tipo = 'Helicóptero'

            else:
                tipo = 'Drone'
            time.sleep(1)
            print('id: {} | Modelo: {} | Ano: {} | Cor: {} | Tipo: {}'.format(i['idAeronave'], i['modelo'], i['ano'], i['cor'], tipo))

        try:
            if autenticado:
                self.menuAdmin()
        except:
            main.main()

    def deletarAeronave(self):
        self.conexao()
        id = int(input('Digite o ID da Aeronave a ser deletada: '))
        with self.banco.cursor() as cursos:
            cursos.execute("DELETE FROM aeronaves WHERE idAeronave={}".format(id))
            self.banco.commit()
            print('\nDeletado')
            self.menuAdmin()

    def alterarAeronave(self):
        self.conexao()
        id = int(input('Digite o ID da Aeronave para editar seus DADOS: '))
        try:
            with self.banco.cursor() as cursos:
                cursos.execute('SELECT * FROM aeronaves WHERE idAeronave={}'.format(id))
                aeronave = cursos.fetchall()
        except:
            print('Erro ao consultar com DB aeronaves')
            self.menuAdmin()
        modelo = input('Modelo ({}): '.format(aeronave[0]['modelo']))
        ano = int(input('Ano ({}):'.format(aeronave[0]['ano'])))
        cor = input('Cor ({}):'.format(aeronave[0]['cor']))
        tipo = int(input('Tipo ({}):'.format(aeronave[0]['tipo'])))
        with self. banco.cursor() as cursos:
            cursos.execute("UPDATE aeronaves SET modelo='{}', ano={}, cor='{}', tipo={} WHERE idAeronave={}".format(modelo, ano, cor, tipo, id))
            self.banco.commit()
            print('\n \033[0;32m ===Alterado com SUCESSO!!!===\033[m')
            time.sleep(2)
            self.menuAdmin()
