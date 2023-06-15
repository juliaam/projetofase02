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
    # print(dic)
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
		    'TEMPERATURA MAXIMA': linha[2], 'TEMPERATURA MINIMA': linha[3], 
		    'HORAS INSOLAÇÃO': linha[4], 'TEMPERATURA MEDIA': linha[5],
			'UMIDADE RELATIVA': linha[6], 'VELOCIDADE DO VENTO': linha[7]}
    return dic


def corrigirDados(lista): # correção de alguns dados que não condizem com a realidade
    for chave in dic.values():
        if chave['VELOCIDADE DO VENTO'] < 0:
            chave['VELOCIDADE DO VENTO'] = 0
        if chave['PRECIPITACAO'] < 0:
            chave['PRECIPITACAO'] = 0
    return lista

# deve indicar o mês e ano iniciais, bem como o mês e ano finais que deseja visualizar os dados. 
# devo permitir reescrever o dado caso esteja errado (validação de dado)
def consultarDados(listaDeDics):
    dadosDtI = []
    dadosDtF = []
    dataInicial = input("Digite o mês e ano inicial (Ex:06/2017): ")
    dataFinal = input("Digite o mês e ano final para pesquisa (Ex:07/2017): ")
    print("Digite se quer ver: ")
    print("1) todos os dados")
    print("2) apenas os de precipitação")
    print("3) apenas os de temperatura")
    print("4) apenas os de umidade e vento para o período informado")
    dadoEscolhido = int(input(": ")) 

    # achar index pelo dicionario
    for value in dic[dataInicial].values():
        dadosDtI.append(value) 
    for value in dic[dataFinal].values():
        dadosDtF.append(value)
    dadosDtI.insert(0, dataInicial)
    dadosDtF.insert(0, dataFinal)
    indexDtI = itensTransformados.index(dadosDtI)
    indexDtF = itensTransformados.index(dadosDtF)
    listaExibicao = itensTransformados [indexDtI: indexDtF]

    # listagem de itens de acordo com o usuário
    for item in listaExibicao:
        if dadoEscolhido == 1:
            print(f"Data: {item[0]}, Temperatura Máxima: {item[1]}, Temp. Máxima: {item[2]}, Temp. Mínima: {item[3]}, Horas Insolação: {item[4]} Temp. Média: {item[5]}, Umidade Relativa': {item[6]}, Velocidade do vento: {item[7]}")
        if dadoEscolhido == 2:
            print(f"Data: {item[0]}, Precipitação: {item[1]}")
        if dadoEscolhido == 3:
            print(f"Data: {item[0]}, Temp. Máxima: {item[2]}, Temp. Mínima: {item[3]}, Temp. Média: {item[5]}")
        if dadoEscolhido == 4:
            print(f"Data: {item[0]}, Umidade: {item[6]}, Vento: {item[7]}")
    return listaDeDics

def mesMaisChuvoso(dic):
    maior = 0
    for key, value in dic.items():
        precipitacaoFloat = value['PRECIPITACAO']
        if precipitacaoFloat > maior:
            maior = precipitacaoFloat
            maiorDado = key, value
    return maiorDado

# Dados base
dadosBrutos = carregarDados("OK_Anexo_Arquivo_Dados_Projeto.csv")
itensTransformados = transformaLista(dadosBrutos)
dic = {}

# Funções 
transformaEmDic(itensTransformados)
corrigirDados(dic)
consultarDados(dic)
mesMaisChuvoso(dic)

# 