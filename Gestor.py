class Gestor:

    # Gestão de viaturas
    def __init(self):
        pass

    @property
    def load_viaturas(self):
        # carrega para uma lista as viaturas registadas no ficheiro:
        # «viaturas.csv»
        __texto_viaturas = []
        f = open('viaturas.csv', 'r')
        __texto_viaturas = f.readlines()
        f.close()

    def load_utilizadores(self):
        # carrega para uma lista os utilizadores registadas no ficheiro:
        # «utilizadores.csv»
        __texto_utilizadores = []
        f = open('utilizadores.csv', 'r')
        __texto_utilizadores = f.readlines()
        f.close()

    def load_alugueres_terminados(self):
        # carrega para uma lista os alugueres terminados registadas no ficheiro:
        # «alugueres_terminados.csv»
        __texto_alugueres_terminados = []
        f = open('alugueres.csv', 'r')
        __texto_alugueres_terminados = f.readlines()
        f.close()

    def load_alugueres_abertos(self):
        # carrega para uma lista os alugueres abertos registadas no ficheiro:
        # «alugueres_abertos.csv»
        __texto_alugueres_abertos = []
        f = open('alugueres_abertos.csv', 'r')
        __texto_alugueres_abertos = f.readlines()
        f.close()

    def add_viatura(self):
        for line in self.__texto_viaturas:
            info = line.split(',')
            v = Viatura(info[0], info[1], eval(info[2]), eval(info[3]))


    def exists_viatura(self, name):
        for line in self.__texto_viaturas:
            if line[i] == name:
                return 'A viatura existe.'
            else:
                return 'Não existe viatura registada com esse nome'

    def get_preco_viatura(self, name):
        load_viaturas()
        for line in self.__texto_viaturas:
            if line[i] == nome_viatura:
                return 'O preço base da viatura é €{}'.format(line[i])
            else:
                return 'Essa viatura não se encontra registada.'
        # remove o conteúdo da lista após utilização
        self.__texto_viaturas =[]

    def listar_viaturas(self):
        #for line in self.__texto_viaturas:


    # Gestão de utilizadores
    # 1. (exists_user) Verificar se existe um utilizador com determinado nickname
    def exists_user(self, nickname):
        load_utilizadores()
        for line in __texto_utilizadores:
            print(*line, sep="\n")


            # 2. (add_user) Adicionar um novo utilizador ao sistema. Deverá garantir que não existe outro utilizador com o
    # mesmo nickname no sistema, antes de fazer o seu registo no sistema.
    def add_user(self, nickname):
        #for line in self.__texto_utilizadores:


    # 3. (listar_users) Listar os utilizadores existentes, mostrando os seus detalhes.
    def listar_users(self):
        #for line in self.__texto_utilizadores:

    # 4. Adicionar saldo a um determinado utilizador. Este método recebe dois parâmetros,
    # o nickname do utilizador e o saldo a acrescentar.
    def add_saldo(self, nickname, plus_saldo):
        #for line in self.__texto_utilizadores:

    # 5. Alterar a password de um determinado utilizador, dado o seu nickname
    def new_password_user(self, nickname, password):
        for utilizador in self.__texto_utilizadores:
            if utilizador[i] == nickname:
                resposta = input('Tem a certeza que quer alterar a senha [s/n]:')
                if resposta == 's':
                    utilizador[i] = password
                else:
                    print('A senha não foi alterada.')
            else:
                print('O nickname não existe.')

    # Gestão de alugueres
    # 1. Verificar se uma viatura se encontra disponível, dado o seu nome. Uma viatura está disponível
    # se não existir um aluguer ativo com essa viatura
    def get_viatura_disponível(self,nome):
        #for line in self.__texto_alugueres_abertos:

    # 2. Listar as viaturas disponíveis
    def get_viaturas_csv(self):
        if len(self.__texto_viaturas) > 0:
            print('Nome','Modelo', 'Tipo elétrica', 'Preço base')
            for viaturas in self.__texto_viaturas:
                print(viaturas)
        else:
            print('Não existem viaturas registadas.')

    # 3. Criar um novo aluguer, dado o nickname do utilizador e o nome da viatura,
    # que deverá ser adicionado à lista dos alugueres ativos.
    # Considere que o inicio do aluguer ocorre no momento da sua criação
