#Superclasse Usuario
class Usuario:
    
    #Construtor
    def __init__(self,nome,idade,maioridade,sexo,nacionalidade,endereco,nomemae,nomepai,cpf,rg):
        self.nome = nome
        self.idade = idade
        self.maioridade = maioridade
        self.sexo = sexo
        self.nacionalidade = nacionalidade
        self.endereco = endereco
        self.nomemae = nomemae
        self.nomepai = nomepai
        self.cpf = cpf
        self.rg = rg
    
    #Sets
    def set_nome(self, nome):
        self.nome = nome
    def set_idade(self, idade):
        self.idade = idade
    def set_maioridade(self, maioridade):
        self.maioridade = maioridade
    def set_sexo(self, sexo):
        self.sexo = sexo
    def set_nacionalidade(self, nacionalidade):
        self.nacionalidade = nacionalidade
    def set_endereco(self, municipio, estado):
        self.endereco.municipio = municipio
        self.endereco.estado = estado
    def set_nomemae(self, nomemae):
        self.nomemae = nomemae
    def set_nomepai(self, nomepai):
        self.nomepai = nomepai
    def set_cpf(self, cpf):
        self.cpf = cpf

    #Gets
    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    def get_maioridade(self):
        return self.maioridade
    def get_sexo(self):
        return self.sexo
    def get_nacionalidade(self):
        return self.nacionalidade
    def get_nomemae(self):
        return self.nomemae
    def get_nomepai(self):
        return self.nomepai
    def get_cpf(self):
        return self.cpf
    def get_rg(self):
        return self.rg
         
    #Imprime os dados de um usuário no sistema
    def pesquisar(self):
        print('\n{} é {}, nasceu em {} e define seu gênero como {}. Mora em {}, {}.'.format(self.nome,self.nacionalidade,self.idade,self.sexo,self.endereco.municipio,self.endereco.estado))
        print('\nOutros dados cadastrados:')
        print(' RG: {}'.format(self.rg))
        if not (self.cpf == '-1'):
            print(' CPF: {}'.format(self.cpf))
        if not (self.nomemae == '-1'):
            print(' Nome da mãe: {}'.format(self.nomemae))
        if not (self.nomepai == '-1'):
            print(' Nome do pai: {}'.format(self.nomepai))

#Subclasse de Usuario
class Dupla_nac(Usuario):
    
    #Herança
    def __init__(self,nome,idade,maioridade,sexo,nacionalidade,endereco,nomemae,nomepai,cpf,rg,dupla):
        Usuario.__init__(self,nome,idade,maioridade,sexo,nacionalidade,endereco,nomemae,nomepai,cpf,rg)
        self.dupla = dupla

    #Polimorfismo
    def pesquisar(self):
        print('\n{} possui dupla nacionalidade como {} e {}, nasceu em {} e define seu gênero como {}. Mora em {}, {}.'.format(self.nome,self.nacionalidade,self.dupla,self.idade,self.sexo,self.endereco.municipio,self.endereco.estado))
        print('\nOutros dados cadastrados:')
        print(' RG: {}'.format(self.rg))
        if not (self.cpf == '-1'):
            print(' CPF: {}'.format(self.cpf))
        if not (self.nomemae == '-1'):
            print(' Nome da mãe: {}'.format(self.nomemae))
        if not (self.nomepai == '-1'):
            print(' Nome do pai: {}'.format(self.nomepai))
      
    #Set
    def set_dupla(self, dupla):
        self.dupla = dupla
    
    #Get
    def get_dupla(self):
        return self.dupla
    
#Classe Nascimento
class Nascimento:
    
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    #Faz parte da Associação com Usuario
    def calculo_idade(self):
        idade = str(str(self.dia)+'/'+str(self.mes)+'/'+str(self.ano))
        
        return idade
     
    #Também faz parte da Associação com Usuario
    def calculo_maioridade(self):
        
        contidade = self.ano*365 + self.mes*30 + self.dia
        
        if (738129 - contidade) >= 6570:
            maioridade = True
        else:
            maioridade = False
       
        return maioridade
        

#Classe Endereco
class Endereco:
    
    #Faz parte da Agregação com Usuario
    def __init__(self,municipio,estado):
        self.municipio = municipio
        self.estado = estado
