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
        self.__sintomas = ['Febre', 'Tosse seca', 'Cansaço', 'Dor de cabeça', 'Dores e desconfortos', 'Perda de paladar', 'Dificuldade de respirar', 'Dor no peito', 'Diarréia']
        self.__cidades = ['Recife', 'Olinda', 'Paulista', 'Caruaru', 'Belo Jardim', 'Garanhuns', 'São João', 'Petrolina', 'Saloá', 'Outras']
    
    def menu(self):
        self.load_file()
        opcao = -1
        while opcao != 0:
            if opcao == 1:
                self.register()
                self.save_file()
            if opcao == 2:
                self.estatisticas()
            self.break_lines()
            opcao = int(input('Selecione uma opção: \n\n1- Cadastro de infectado \n2- Ver estatísticas \n0- Sair\n'))
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
        idade = self.set_idade()
        cidade = self.select_city()
        sintomas = self.select_sintomas([], self.__sintomas.copy())
        if len(sintomas) == 0:
            sintomas.append('Assintomático')
        new_pessoa = Pessoa(nome, idade, cidade, sintomas)
        self.__pessoas.append(new_pessoa)
    
    def set_idade(self):
        idade_integer = True
        idade_positive = True
        while idade_integer:
            try:
                while idade_positive:
                    idade = int(input('Sua idade: '))
                    if idade < 0 or idade > 120:
                        print('Digite uma idade válida!')
                    else: idade_positive = False
                idade_integer = False
            except:
                print('Digite uma idade válida!')
        
        return idade
    
    def select_city(self):
        selected = ''
        opcao = -1
        print('Sua Cidade:')
        index = 0
        for cidade in self.__cidades:
            print(index+1,'-', cidade)
            index+=1
        opcao = int(input('Digite o número referente a sua cidade: '))
        if opcao > 0:
            selected = self.__cidades[opcao-1]
        elif opcao not in '123456789' and opcao != '10':
            selected = self.__cidades[-1]
        return selected
    
    def select_sintomas(self, sintomas_listados, sintomas_nao_listados):
        
        print('Sintomas já relacionados:')
        for sintoma in sintomas_listados:
            print(sintoma)
        print('')
        
        print('Sintomas não relacionados:')
        index = 0
        for sintoma in sintomas_nao_listados:
            print(index + 1, '-', sintoma)
            index += 1
        print('\n0 - Concluir\n')
        
        sintoma = input('Digite o número referente a um de seus sintomas: ')
        if sintoma not in '123456789' and sintoma != '0':
            print('Sintoma inválido')
            self.select_sintomas(sintomas_listados, sintomas_nao_listados)
            return sintomas_listados
        elif sintoma == '0':
            return sintomas_listados
        else:
            sintomas_listados.append(sintomas_nao_listados[int(sintoma) - 1])
            sintomas_nao_listados.pop(int(sintoma) - 1)
            one_more = input('Deseja inserir mais algum sintoma? (s/n)\n')
            if one_more == 'S'or one_more == 's':
                self.select_sintomas(sintomas_listados, sintomas_nao_listados)
                return sintomas_listados
            else:
                return sintomas_listados

    def estatisticas(self):
        opcao = -1
        while opcao != 0:
            if opcao == 1:
                self.infecteds()
            if opcao == 2:
                self.symptoms()
            self.break_lines()
            opcao = int(input('Selecione uma opção: \n\n1 - Quantidade de infectados por cidade \n2 - Recorrência de sintomas\n0 - Voltar \n'))
            self.break_lines()

    def infecteds(self):
        opcao = -1
        while opcao != 0:
            
            if opcao == 1:
                print('QUANTIDADE DE INFECTADOS POR CIDADE: (FILTRO: GERAL)')
                print('QUANTIDADE | PERCENTUAL | CIDADE')
                quantidades = []
                total = 0
                for cidade in self.__cidades:
                    count = 0
                    for pessoa in self.__pessoas:
                        if pessoa.get_cidade() == cidade:
                            count += 1
                            total += 1
                    quantidades.append(count)
                for cidade in range(len(self.__cidades)):
                    print(quantidades[cidade - 1], 'infectados |', round((quantidades[cidade - 1]*100)/total),'% |', self.__cidades[cidade - 1])
            
            if opcao == 2:
                try:
                    de = int(input('A partir de quantos anos? \n'))
                    ate = int(input('Até quantos anos? \n'))
                    print(f'QUANTIDADE DE INFECTADOS POR CIDADE: (FILTRO: IDADE(DE {str(de)} ATÉ {str(ate)}))')
                    quantidades = []
                    total = 0
                    for cidade in self.__cidades:
                        count = 0
                        for pessoa in self.__pessoas:
                            if pessoa.get_cidade() == cidade and int(pessoa.get_idade()) >= de and int(pessoa.get_idade()) <= ate:
                                count += 1
                                total += 1
                        quantidades.append(count)
                    if total == 0:
                        print('\nNão há registros segundo esses parâmetros.')
                    else:
                        print('QUANTIDADE | PERCENTUAL | CIDADE')
                        for cidade in range(len(self.__cidades)):
                            print(quantidades[cidade - 1], 'infectados |', (quantidades[cidade - 1]*100)/total, '% |', self.__cidades[cidade - 1])
                except:
                    print('Insira idades válidas!')

            self.break_lines()
            opcao = int(input('QUANTIDADE DE INFECTADOS POR CIDADE: \n\n1 - Geral \n2 - Por idade\n0 - Voltar\n'))
            self.break_lines()
            
    def symptoms(self):
        opcao = -1
        while opcao != 0:
            
            if opcao == 1:
                print('RECORRÊNCIA DE SINTOMAS: (FILTRO: GERAL)')
                print('RECORRÊNCIA | PERCENTUAL | SINTOMA')
                recorrencias = []
                total = 0
                for sintoma in self.__sintomas:
                    count = 0
                    for pessoa in self.__pessoas:
                        for sintoma_pessoa in pessoa.get_sintomas():
                            if sintoma_pessoa == sintoma:
                                count += 1
                                total += 1
                    recorrencias.append(count)
                for sintoma in range(len(self.__sintomas)):
                    print(recorrencias[sintoma - 1], 'recorrencias |', round((recorrencias[sintoma - 1]*100)/total),'% |', self.__sintomas[sintoma - 1])
            
            if opcao == 2:
                try:
                    de = int(input('A partir de quantos anos? \n'))
                    ate = int(input('Até quantos anos? \n'))
                    print(f'RECORRÊNCIA DE SINTOMAS: (FILTRO: IDADE(DE {str(de)} ATÉ {str(ate)}))')
                    recorrencias = []
                    total = 0
                    for sintoma in self.__sintomas:
                        count = 0
                        for pessoa in self.__pessoas:
                            for sintoma_pessoa in pessoa.get_sintomas():
                                if sintoma_pessoa == sintoma and int(pessoa.get_idade()) >= de and int(pessoa.get_idade()) <= ate:
                                    count += 1
                                    total += 1
                        recorrencias.append(count)
                    if total == 0:
                        print('\nNão há registros segundo esses parâmetros.')
                    else:
                        print('RECORRÊNCIA | PERCENTUAL | SINTOMA')
                        for sintoma in range(len(self.__sintomas)):
                            print(recorrencias[sintoma - 1], 'recorrencias |', round((recorrencias[sintoma - 1]*100)/total),'% |', self.__sintomas[sintoma - 1])
                except:
                    print('Insira idades válidas!')

            if opcao == 3:
                print('RECORRÊNCIA DE SINTOMAS: (FILTRO: CIDADE')
                for cidade in self.__cidades:
                    recorrencias = []
                    total = 0
                    isCity = False
                    for sintoma in self.__sintomas:
                        count = 0
                        for pessoa in self.__pessoas:
                            for sintoma_pessoa in pessoa.get_sintomas():
                                if sintoma_pessoa == sintoma and pessoa.get_cidade() == cidade:
                                    count += 1
                                    total += 1
                                    isCity = True
                        recorrencias.append(count)
                    if isCity:
                        if total == 0:
                            print('\nNão há registros segundo esses parâmetros.')
                        else:
                            print(f'\n| {str(cidade.upper())} |\n')
                            print('RECORRÊNCIA | PERCENTUAL | SINTOMA')
                            for sintoma in range(len(self.__sintomas)):
                                print(recorrencias[sintoma - 1], 'recorrencias |', round((recorrencias[sintoma - 1]*100)/total),'% |', self.__sintomas[sintoma - 1])
               

            self.break_lines()
            opcao = int(input('RECORRÊNCIA DE SINTOMAS: \n\n1 - Geral \n2 - Por idade\n3 - Por cidade\n0 - Voltar\n'))
            self.break_lines()
            
    def break_lines(self):
        print('\n\n===============================\n\n')

main = main()

main.menu()
