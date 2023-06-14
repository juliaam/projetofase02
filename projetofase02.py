# Leitura de dados

def carregarDados(nomeArq):
    dadosBrutos = []
    arquivo = open(nomeArq, "r")
    for linha in arquivo:
        linhas1 = linha[:-1]
        linhas2 = linhas1[1 : len(linhas1)]
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


dadosBrutos = carregarDados("OK_Anexo_Arquivo_Dados_Projeto.csv")
itensTransformados = transformaLista(dadosBrutos)
dic = {}

def transformaEmDic(lista):
    for linha in lista:
        dic[linha[0]] = {'PRECIPITACAO': linha[1],
		    'MAXIMA': linha[2], 'MINIMA': linha[3], 
		    'HORAS INSOLAÇÃO': linha[3], 'TEMPERATURA MEDIA': linha[4],
			'UMIDADE RELATIVA': linha[5], 'VELOCIDADE DO VENTO': linha[6]}
    return dic

def corrigirDados(lista):
    for chave in dic.values():
        if chave['VELOCIDADE DO VENTO'] < 0:
            chave['VELOCIDADE DO VENTO'] = 0
        if chave['PRECIPITACAO'] < 0:
            chave['PRECIPITACAO'] = 0
    # print(chave)
    return lista

# deve indicar o mês e ano iniciais, bem como o mês e ano finais que deseja visualizar os dados. 
def consultarDados(listaDeDics):
    pesquisa = input("")

# print(transformaEmDic(itensTransformados))
transformaEmDic(itensTransformados)
corrigirDados(dic)
# print(dic['0/07/2016']['MAXIMA'])
# for linha in dic['0/07/2016']:
#     print(linha)
