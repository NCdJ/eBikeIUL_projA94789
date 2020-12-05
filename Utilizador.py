class Utilizador:
    def __init__(self, nickname, password, nome, e_mail, curso, saldo=0.0):
        # O saldo é opcional
        # Não deverá ser possível alterar nickname e nome
        self.__nickname = nickname  # imutável
        self.password = password
        self.__nome = nome # imutável
        self.e_mail = e_mail
        self.curso = curso
        self.saldo = saldo
        print('Não esquecer de adicionar ao ficheiro o novo utilizador com o método: «save_to_csv()')

    @property
    def get_nickname(self):
        return 'O utilizador tem o nickname \"{}\".'.format(self.__nickname)

    @property
    def get_password(self):
        return 'A senha é {}.'.format('*' * len(self.password))

    # Testa a senha
    def test_password(self, new_password):
        if self.password == new_password:
            print('As passwords são iguais.')
        else:
            print('As passwords não sã iguais.')

    @property
    def get_nome(self):
        return 'O nickname \"{}\" pertence ao {}.'.format(self.__nickname, self.__nome)

    @property
    def get_email(self):
        return 'O nickname \"{}\" tem o e-mail {}.'.format(self.__nickname, self.e_mail)

    @property
    def get_curso(self):
        return '{} está no curso {}.'.format(self.__nome, self.curso)

    @property
    def get_saldo(self):
        return 'O nickname \"{}\" tem €{} de saldo.'.format(self.__nickname, self.saldo)


    def __str__(self):
        crdt = str(self.saldo)
        return 'O/A utilizador/a ' + self.__nome + ' tem o nickname \"' + self.__nickname + '\", ' + \
                'e o e-mail ' + self.e_mail + '.\nEstá inscrito/a no curso ' + self.curso + '.\n' \
                'O saldo disponível é de €' + crdt

    def save_to_csv(self):
        try:
            f = open('utilizadores.csv', 'a')
            f.write('{},{},{},{}\n'.format(self.__nickname, \
                                           self.password, \
                                           self.__nome, \
                                           self.e_mail, \
                                           self.curso, \
                                           self.saldo))
            f.close()
            print('Dados do utilizador gravados no ficheiro com sucesso')
        except:
            print('Ocorreu um problema com a gravação dos dados do utilizador no ficheiro.')

u1 = Utilizador('gost', 'rider', 'Pedro Mota', 'pedro@iscte-iul.pt', 'LCD', 25.0)

u2 = Utilizador('maria', 'itsme', 'Maria Mercedes', 'maria@iscte-iul.pt', 'LEI', 40.0)
