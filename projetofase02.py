import matplotlib.pyplot as plt

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

def transformaDados(linha):
    itens = linha.split(";")
    linha = [itens[0]]
    cont = 1
    while cont < len(itens):
        linha.append(
            float(itens[cont]))
        cont = cont + 1
    return linha

def formatarDataDic(dic):
    for key in list(dic.keys()):
        novoK = key[3:len(key)]
        dic[novoK] = dic.pop(key)
    return dic

def consultarTempMin(dic):
    valido = False
    mes = 0
    media = 0
    while valido == False:
        mes = str(input("Digite um mês(01 a 12): "))
        if int(mes) > 0 and int(mes) < 13:
            valido = True
            anos = ['2006', '2007', '2008', '2009', '201']
            anosMedia = []
            somaGeral = 0 
            pesoGeral = 0
            somaAno = 0
            pesoAno = 0
            
            for key, value in dic.items():
                for ano in anos:
                    # print(ano)
                    # temperatura média dos ultimos 11 anos
                    if ano in key and mes in key[3: 5]:
                        somaGeral = somaGeral + value['TEMPERATURA MINIMA']
                        pesoGeral = pesoGeral+ 1
                #temperatura média do mês nos ultimos 11 anos
                    if anos and mes in key[3:5]:  
                            somaAno = somaAno + value['TEMPERATURA MINIMA']
                            pesoAno = pesoAno + 1
                            anosMedia.append(somaAno)
                            anosMedia.append(pesoAno)

                            
            mediaG = somaGeral // pesoGeral
            mediaA = somaAno // pesoAno 
        else:
            print("Digite o mês corretamente")
        # print(mediaG, mediaA)
        return mediaG, mediaA, mes

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
dicData = formatarDataDic(dic)
# Funções 
transformaEmDic(itensTransformados)
corrigirDados(dic)
mesMaisChuvoso(dic)

coisas = consultarTempMin(dic)
print(coisas)
# print(formatarDataDic(dic))
# consultarDados(dic)
# consultarTempMin(dicData)
# print(dicData)
# print(dicData)

