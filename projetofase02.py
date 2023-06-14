# Leitura de dados


def carregarDados(nomeArq):
    dadosBrutos = []
    arquivo = open(nomeArq, "r")
    for linha in arquivo:
        linhas1 = linha[:-1]
        linhas2 = linhas1[1 : len(linhas1)]
        dadosBrutos.append(linhas2)
    arquivo.close()
    # print(dadosBrutos)
    return dadosBrutos


# Organização e transformação dos dados
def transformaLista(lista):
    listaDeItens = []
    cont = 1  # pula o cabecalho
    while cont < len(lista):
        listaDeItens.append(transformaDados(lista[cont]))
        cont = cont + 1
    return listaDeItens


def transformaDados(linha):
    itens = linha.split(";")
    itensTransformados = [itens[0]]  # Municipio foi colocado na lista
    cont = 1
    while cont < len(itens):
        itensTransformados.append(
            float(itens[cont])
        )  # converte para float demais itens
        cont = cont + 1
    return itensTransformados


dadosBrutos = carregarDados("OK_Anexo_Arquivo_Dados_Projeto.csv")
itensTransformados = transformaLista(dadosBrutos)

# def transformaEmDic(lista):
dic = {}
for linha in itensTransformados:
    # print (linha)
    # dic[linha[0]] =
    print(linha)
    dic[linha[0]] = {'DATA': linha[0] ,'PRECIPITACAO': linha[1],
		    'MAXIMA': linha[2], 'MINIMA': linha[3],
		    'HORAS INSOLAÇÃO': linha[3], 'TEMPERATURA MEDIA': linha[4],
			'UMIDADE RELATIVA': linha[5], 'VELOCIDADE DO VENTO': linha[6]}
    print(dic[linha[0]])
    # print(linha)
    # print(linha[0])
	# dic[itensTransformados[0]] = itensTransformados
# print(dic)
# print(itensTransformados)

# def transformarEmDic(dados):
# 	listaDic = []
# 	cont = 1
# 	for linha in dados:
# 		linha1 = linha.split(';')
# 		dic = {}
# 		dic[linha1[0]] = linha1
# 		print(linha1[1])
# 		if float(linha1[1]) < 0:
# 			linha1[1] = 0
# 		dic[linha1[0]] = {'DATA': linha1[0] ,'PRECIPITACAO': linha1[1],
# 		    'MAXIMA': linha1[2], 'MINIMA': linha1[3],
# 		    'HORAS INSOLAÇÃO': linha1[3], 'TEMPERATURA MEDIA': linha1[4],
# 			'UMIDADE RELATIVA': linha1[5], 'VELOCIDADE DO VENTO': linha1[6]}
# 		listaDic.append(dic[linha1[0]])
# 	# print(listaDic[1])
# 	return listaDic


def consultarDados(listaDeDics):
    input = input("")



# print(dadosBrutos)
# transformarEmDic(dadosBrutos)
