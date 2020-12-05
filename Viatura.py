class Viatura:
    # Teoria:
    # O construtor é o que define os atributos da classe
    def __init__(self,
                 nome,
                 modelo,
                 tipo_eletrica,
                 preco_base):
        # Não deverá ser possível alterar nenhum dos atributos além do preco_base
        self.__nome = nome                          # imutável
        self.__modelo = modelo                      # imutável
        self.__tipo_eletrica = tipo_eletrica        # imutável
        self.preco_base = preco_base

    # Teoria:
    # No caso de classes de objetos imutáveis é útil definir/garantir que os atributos não são alterados
    # definindo propriedades para atributos escondidos
    @property
    def get_nome(self):
        return 'O nome da viatura é {}.'.format(self.__nome)

    @property
    def get_modelo(self):
        return 'A viatura {} tem o modelo {}.'.format(self.__nome, self.__modelo)

    @property
    def get_tipo_eletrica(self):
        if self.__tipo_eletrica == True:
            msg = 'é elétrica'
        else:
            msg = 'não é elétrica'
        return 'A viatura {} {}.'.format(self.__nome, msg)

    @property
    def get_preco_base(self):
        return 'A viatura {} tem o preço base de €{}.'.format(self.__nome, self.preco_base)

    # Alterar o preço base da viatura
    def set_preco_base(self, novo_preco):

        # Valida o preço inserido
        if novo_preco < 0:
            print('O preço indicado ({}€) não é válido.'.format(float(novo_preco)))
        elif novo_preco == 0:
            print('Atenção, o novo preço é zero.')

            while True:
                ins = input('Confirma o preço zero [sS|nN]:')
                if ins == 's' or ins == 'S':
                    self.preco_base = float(0)
                    print('O preço foi atualizado com sucesso.\n'
                          'O novo valor é (€): ' + str(float(0)))
                    break
                elif ins == 'n' or ins == 'N':
                    print('O preço base não sofreu alteração.')
                    break
        elif novo_preco > 0:
            self.preco_base = float(novo_preco)
            print('O preço foi atualizado com sucesso.\n'
                  'O novo valor é (€): ' + str(float(novo_preco)))
        elif self.preco_base == novo_preco:
            print('O preço antigo e o novo preço são iguais.')

    # Comparar adequadamente objetos deste tipo, sabendo que
    # duas viaturas são iguais se o seu tipo e preço forem iguais
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__tipo_eletrica == other.__tipo_eletrica and self.preco_base == other.preco_base

    # Mostrar os seus detalhes no ecrã , usando a função print()
    def __str__(self):
        p_base = str(self.preco_base)
        t_eletrica = str(self.__tipo_eletrica)
        return 'Nome da viatura: ' + self.__nome + '\n' + 'Modelo da viatura: ' + self.__modelo + '\n' +\
               'Tipo da viatura: ' + t_eletrica + '\n' + 'Preço base (€): ' + p_base

    def save_to_csv(self):
        try:
            f = open('viaturas.csv', 'a')
            f.write('{},{},{},{}\n'.format(self.__nome, self.__modelo, self.__tipo_eletrica, self.preco_base))
            f.close()
            print('Dados da viatura gravados no ficheiro com sucesso')
        except:
            print('Ocorreu um problema com a gravação dos dados da viatura no ficheiro.')


v1 = Viatura('vespa', 'Haibike Sduro All Mountain 7.0', False, 0.50)

v2 = Viatura('mosca', 'Btwin Rockrider 5.2 S', False, 0.50)

v3 = Viatura('melro', 'Bike Giant Sduro All Mountain 7.0', False, 0.50)

v4 = Viatura('moscardo', 'Specialized Patanistic Speedo 1.2', True, 0.75)

v5 = Viatura('cavalo', 'Specialized Fatboy', True, 0.50)
