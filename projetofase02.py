# Leitura de dados

def carregarDados(nomeArq):
    dadosBrutos = []
    arquivo = open(nomeArq, "r")
    for linha in arquivo:
        linhas1 = linha[:-1]
        linhas2 = linhas1[0: len(linhas1)]
        dadosBrutos.append(linhas2)
    arquivo.close()
    return dadosBrutos

# Organização e transformação dos dados
def transformaLista(lista):
    listaTransformada = []
    cont = 1  
    while cont < len(lista):
        listaTransformada.append(transformaDados(lista[cont]))
        cont = cont + 1
    return listaTransformada


# utilizar somente na pesquisa de dados
def formataData(dic):
    for item in dic:
        item = item[3:len(item)]
    print(dic)
    return dic

def transformaDados(linha):
    itens = linha.split(";")
    linha = [itens[0]]
    cont = 1
    while cont < len(itens):
        linha.append(
            float(itens[cont]))
        cont = cont + 1
    return linha

def transformaEmDic(lista): #transformar em dicionário para uma busca mais fácil
    for linha in lista:
        dic[linha[0]] = {'PRECIPITACAO': linha[1],
		    'MAXIMA': linha[2], 'MINIMA': linha[3], 
		    'HORAS INSOLAÇÃO': linha[4], 'TEMPERATURA MEDIA': linha[5],
			'UMIDADE RELATIVA': linha[6], 'VELOCIDADE DO VENTO': linha[7]}
    return dic


def corrigirDados(lista): # correção de alguns dados que não condizem com a realidade
    for chave in dic.values():
        if chave['VELOCIDADE DO VENTO'] < 0:
            chave['VELOCIDADE DO VENTO'] = 0
        if chave['PRECIPITACAO'] < 0:
            chave['PRECIPITACAO'] = 0
    # print(chave)
    return lista

# deve indicar o mês e ano iniciais, bem como o mês e ano finais que deseja visualizar os dados. 
# devo permitir reescrever o dado caso esteja errado (validação de dado)
def consultarDados(listaDeDics):
    dadosDtI = []
    dadosDtF = []
    dataInicial = input("Digite o mês e ano inicial (Ex:06/2017): ")
    dataFinal = input("Digite o mês e ano final para pesquisa: ")
    print("Digite se quer ver 1 - todos os dados")
    print("2 - apenas os de precipitação")
    print("3 - apenas os de temperatura")
    print("4 - apenas os de umidade e vento para o período informado")
    dadoEscolhido = int(input("1-4:"))

    # achar index pelo dicionario
    for value in formataData(dic[dataInicial].values()):
        dadosDtI.append(value)
    for value in formataData(dic[dataFinal].values()):
        dadosDtF.append(value)
    dadosDtI.insert(0, dataInicial)
    dadosDtF.insert(0, dataFinal)
    indexDtI = formataData(itensTransformados.index(dadosDtI))
    indexDtF = formataData(itensTransformados.index(dadosDtF))
    print(itensTransformados [indexDtI: indexDtF])
    return listaDeDics

dadosBrutos = carregarDados("OK_Anexo_Arquivo_Dados_Projeto.csv")
itensTransformados = transformaLista(dadosBrutos)
dic = {}
# print(dic['07/2016'])
transformaEmDic(itensTransformados)
novoDic = formataData(dic)
print(novoDic)
# consultarDados(itensTransformados)
corrigirDados(dic)
# consultarDados(itensTransformados)
