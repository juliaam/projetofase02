import matplotlib.pyplot as plt
import numpy as np

# Leitura de dados, seguindo o modelo dos últimos exercícios
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

def corrigirDados(lista): # correção de alguns dados que não condizem com a realidade
    for chave in dic.values():
        if chave['VELOCIDADE DO VENTO'] < 0:
            chave['VELOCIDADE DO VENTO'] = 0
        if chave['PRECIPITACAO'] < 0:
            chave['PRECIPITACAO'] = 0
    return lista

def formatarDataDic(dic):
    for key in list(dic.keys()):
        novoK = key[3:len(key)]
        dic[novoK] = dic.pop(key)
    return dic

def transformaEmDic(lista): #transformar em dicionário para uma busca mais fácil
    for linha in lista:
        dic[linha[0]] = {'PRECIPITACAO': linha[1],
		    'TEMPERATURA MAXIMA': linha[2], 'TEMPERATURA MINIMA': linha[3], 
		    'HORAS INSOLAÇÃO': linha[4], 'TEMPERATURA MEDIA': linha[5],
			'UMIDADE RELATIVA': linha[6], 'VELOCIDADE DO VENTO': linha[7]}
    return dic

def tirarData(lista):
    for linha in lista:
        linha[0] = linha[0][3:10]
    return lista
        
def consultarDados(dic):
    dadosDtI = []
    dadosDtF = []
    dataInicial = input("Digite o mês e ano inicial (Ex:06/2014): ")
    dataFinal = input("Digite o mês e ano final para a pesquisa (Ex:11/2015): ")
    print("Digite se quer ver: ")
    print("1) todos os dados")
    print("2) apenas os de precipitação")
    print("3) apenas os de temperatura")
    print("4) apenas os de umidade e vento para o período informado")
    dadoEscolhido = int(input(": ")) 

        # temperatura média dos ultimos 11 anos 

    # achar index pelo dicionario
    for value in novoDic[dataInicial].values():
        dadosDtI.append(value) 
    for value in novoDic[dataFinal].values():
        dadosDtF.append(value)
    dadosDtI.insert(0, dataInicial)
    dadosDtF.insert(0, dataFinal)
    indexDtI = novaLista.index(dadosDtI)
    indexDtF = novaLista.index(dadosDtF)
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
    return 

def mesMaisChuvoso(dic):
    maior = 0
    for key, value in dic.items():
        precipitacaoFloat = value['PRECIPITACAO']
        if precipitacaoFloat > maior:
            maior = precipitacaoFloat
            maiorDado = key, value
    return print((f"Mês com maior precipitação considerando todos: {maiorDado}"))

def consultarTempMin(dic):
    valido = False
    mes = 0
    media = 0
    while valido == False:
        mes = str(input("Digite um mês(01 a 12) para consultar sua temperatura mínima e temperatura mínima dos últimos anos: "))
        if int(mes) > 0 and int(mes) < 13:
            valido = True
            anos = ['2006', '2007', '2008', '2009', '201'] 
            anosMedia = []
            anoReferencia = '2005'
            somaGeral = 0 
            pesoGeral = 0
            somaAno = 0
            pesoAno = 0
            
            for key, value in dic.items():
                for ano in anos: 
                # temperatura média dos ultimos 11 anos
                    if ano in key and mes in key[3: 5]:
                        somaGeral = somaGeral + value['TEMPERATURA MINIMA']
                        pesoGeral = pesoGeral+ 1

                #temperatura média do mês nos ultimos 11 anos
                    if  int(key[6:10])>=2006:  
                         if key[6:10] != anoReferencia:
                            anosMediaObject = {'Temperatura mínima': somaAno/pesoAno, 'ano':key[6:10]}
                            anosMedia.append(anosMediaObject)
                            anoReferencia = key[6:10]
                            somaAno = 0
                            pesoAno = 0
                         
                    somaAno += value['TEMPERATURA MINIMA']
                    pesoAno += 1
            mediaG = somaGeral // pesoGeral
            mediaA = somaAno // pesoAno 
        else:
            print("Digite o mês corretamente")
        return mediaA, mediaG, mes, anosMedia

# def grafico(dic):
    # print(dic)

# Dados base
dadosBrutos = carregarDados("OK_Anexo_Arquivo_Dados_Projeto.csv")
itensTransformados = transformaLista(dadosBrutos)
dic = {}
dic = transformaEmDic(itensTransformados)
novoDic = formatarDataDic(dic)
novaLista = tirarData(itensTransformados)

# Funções 
consultarDados(novoDic)
mesMaisChuvoso(dic)
dadosTemp = consultarTempMin(dic)
print(f"Média da temperatura anual no mês {dadosTemp[2]}: {dadosTemp[0]}")
print(f"Média da temperatura nos últimos 11 anos no mês {dadosTemp[2]}: {dadosTemp[3]}")