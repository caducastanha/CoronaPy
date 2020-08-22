class Pessoa:
    
    def __init__(self, nome, idade, cidade, sintomas):
        self.__nome = nome
        self.__idade = idade
        self.__cidade = cidade
        self.__sintomas = sintomas
    
    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def get_cidade(self):
        return self.__cidade
    
    def get_sintomas(self):
        return self.__sintomas
    
    def print_pessoa(self):
        return(f'{self.__nome},{self.__idade},{self.__cidade},{self.print_sintomas()}')
    
    def print_sintomas(self):
        return('|'.join(sintoma for sintoma in self.__sintomas))
    
class main:
    def __init__(self):
        self.__pessoas = []
        self.__sintomas = []
        self.__cidades = ['Recife', 'Olinda', 'Paulista', 'Caruaru', 'Belo Jardim', 'Garanhuns', 'São João', 'Petrolina', 'Saloá', 'Outras']
    
    def menu(self):
        self.load_file()
        opcao = -1
        while opcao != 0:
            if opcao == 1:
                self.register()
                self.save_file()
            if opcao == 2:
                self.show()
            self.break_lines()
            opcao = int(input('Selecione uma opção: \n\n1- Cadastro de infectado \n2- Ver dados gerais \n0- Sair\n'))
            self.break_lines()
        
    def load_file(self):
        try:
            pessoas_file = open('pessoas_file.txt', 'r')
            pessoas_list = pessoas_file.readlines()[0].split('\\')
            for pessoa in pessoas_list:
                pessoa_arrayed = pessoa.split(',')
                sintomas_arrayed = pessoa_arrayed[3].split('|')
                new_pessoa = Pessoa(pessoa_arrayed[0], pessoa_arrayed[1], pessoa_arrayed[2], sintomas_arrayed)
                self.__pessoas.append(new_pessoa)
        except : pass
    
    def save_file(self):
        pessoas_file = open('pessoas_file.txt', 'w')
        pessoas = '\\'.join(pessoa.print_pessoa() for pessoa in self.__pessoas)
        pessoas_file.write(pessoas)
        pessoas_file.close()
    
    def register(self):
        print('----Cadastro de infectado Covid-19----\n\n')
        nome = input('Seu Nome: ')
        idade = int(input('Sua idade: '))
        cidade = self.select_city()
        sintomas = []
        if len(sintomas) == 0:
            sintomas.append('Assintomático')
        pessoa_teste = Pessoa(nome, idade, cidade, sintomas)
        self.__pessoas.append(pessoa_teste)
    
    def select_city(self):
        selected = ''
        opcao = -1
        print('Sua Cidade:')
        index = 0
        for cidade in self.__cidades:
            print(index+1,'-', cidade)
            index+=1
        opcao = int(input(''))
        if opcao > 0:
            selected = self.__cidades[opcao-1]
        return selected

    def show(self):
        matriz = []
        print('----Dados Gerais da Covid-19----\n\n')
        for pessoa in self.__pessoas:
            matriz.append([pessoa.get_nome(), pessoa.get_idade(), pessoa.get_cidade()])
        print(matriz)

    def break_lines(self):
        print('\n\n===============================\n\n')

Main = main()

Main.menu()
