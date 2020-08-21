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
    
    def menu(self):
        self.load_file()
        
        # EXECUTA PRIMEIRO SÓ A LINHA 36, DEPOIS SÓ A LINHA 37
        
        # pessoa_teste = Pessoa('Caio', '18', 'Garanhuns', ['dor de cabeça', 'febre'])
        # pessoa_teste = Pessoa('Lucas', '25', 'Recife', ['diarréia', 'falta de paladar'])
        self.__pessoas.append(pessoa_teste)
        self.save_file()
        
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
    
Main = main()

Main.menu()