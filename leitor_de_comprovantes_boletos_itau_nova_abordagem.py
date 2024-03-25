import pandas as pd
import re
from PyPDF2 import PdfReader

# Exemplo de extração de texto
reader = PdfReader("C:\\Users\\Gabriel\\Downloads\\Comprovantes ITAUJAN24 _01.pdf")
texto_completo = ''
for page in reader.pages:
    texto_completo += page.extract_text() + '\n'

# Caminho para o arquivo de texto onde você deseja salvar o resultado
caminho_arquivo_texto = "C:\\Users\\Gabriel\\Downloads\\texto_extraido.txt"



#gravação arquivo
# Transformar o texto completo para letras maiúsculas
texto_completo_maiusculas = texto_completo.upper()
# Abrir (ou criar) o arquivo de texto e escrever o conteúdo acumulado
with open(caminho_arquivo_texto, 'w', encoding='utf-8') as arquivo_texto:
    arquivo_texto.write(texto_completo_maiusculas)


#leitura do arquivo
def ler_conteudo_arquivo(caminho_arquivo):
    # Abrir o arquivo para leitura
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    return linhas    

arquivo_conteudo=ler_conteudo_arquivo(caminho_arquivo_texto)



# Lista para armazenar as linhas modificadas
linhas_modificadas = []

''''''
# Iterar sobre cada linha
for linha in arquivo_conteudo:
    # Verificar se a linha contém "COMPROVANTE DE"
    #if "COMPROVANTE DE" in linha:
        # Adicionar a linha modificada à lista, incluindo uma nova linha ao final
        #linhas_modificadas.append(linha + "\n")
    #else:
        # Adicionar a linha não modificada à lista
    linhas_modificadas.append(linha)

# Juntar as linhas modificadas de volta em uma única string
arquivo_conteudo = "\n".join(linhas_modificadas)
print(arquivo_conteudo)



### FAZ CORREÇÕES NO TEXTO PARA HARMONIZAR E PADRONIZAR OS CONTEÚDOS
textos=['VALOR TOTAL:','VALOR:','VALOR RECOLHIDO:','VALOR DA TRANSAÇÃO:']
for i in textos:
    arquivo_conteudo=arquivo_conteudo.replace(i,"VALOR PAGO:")

textos=['DATA DA TRANSFERÊNCIA:','DATA DO PAGAMENTO:','PAGAMENTO REALIZADO EM']
for i in textos:
    arquivo_conteudo=arquivo_conteudo.replace(i,"PAGAMENTO EFETUADO EM")

textos=['NOME DO RECEBEDOR:','NOME DO FAVORECIDO:']
for i in textos:
    arquivo_conteudo=arquivo_conteudo.replace(i,"FORNECEDOR:")

textos=['GRF - GUIA DE RECOLHIMENTO DO FGTS']
for i in textos:
    arquivo_conteudo=arquivo_conteudo.replace(i,"FORNECEDOR:GRF - GUIA DE RECOLHIMENTO DO FGTS")

textos=['TRIBUTOS ESTADUAIS COM CÓDIGO DE BARRAS']
for i in textos:
    arquivo_conteudo=arquivo_conteudo.replace(i,"FORNECEDOR:TRIBUTOS ESTADUAIS COM CÓDIGO DE BARRAS")

textos=['COMPROVANTE DE PAGAMENTO - DARF']
for i in textos:
    arquivo_conteudo=arquivo_conteudo.replace(i,"FORNECEDOR:DARF")

textos=['TRIBUTOS MUNICIPAIS']
for i in textos:
    arquivo_conteudo=arquivo_conteudo.replace(i,"FORNECEDOR:TRIBUTOS MUNICIPAIS")    



# Lista para armazenar as linhas modificadas
linhas_modificadas = []

arquivo_conteudo=arquivo_conteudo.splitlines()

# Iterar sobre cada linha, exceto a última, pois não tem uma próxima linha para juntar Pagamento com código de barras
i = 0
while i < len(arquivo_conteudo):
    # Verificar se a linha contém "COMPROVANTE DE OPERAÇÃO - CONCESSIONÁRIAS"
    if "CONCESSIONÁRIAS" in arquivo_conteudo[i] or "PAGAMENTO COM CÓDIGO DE BARRAS" in arquivo_conteudo[i]:
        # Juntar essa linha com a próxima linha e adicionar à lista
        # Remover espaços extras na expressão para coincidir com qualquer formatação
        if i + 1 < len(arquivo_conteudo):  # Certificar-se de que não é a última linha
            linhas_modificadas.append("FORNECEDOR:"+ arquivo_conteudo[i + 2])
            i += 3  # Pular a próxima linha, pois já foi adicionada
            continue
    # Adicionar linhas que não precisam ser modificadas
    linhas_modificadas.append(arquivo_conteudo[i])
    i += 1

# Juntar as linhas modificadas de volta em uma única string
arquivo_conteudo = "\n".join(linhas_modificadas)







#gravação arquivo
# Transformar o texto completo para letras maiúsculas
texto_completo_maiusculas = arquivo_conteudo.upper()
# Abrir (ou criar) o arquivo de texto e escrever o conteúdo acumulado
with open(caminho_arquivo_texto, 'w', encoding='utf-8') as arquivo_texto:
    arquivo_texto.write(texto_completo_maiusculas)






#leitura arquivo
def ler_conteudo_arquivo(caminho_arquivo):
    # Abrir o arquivo para leitura
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    return linhas    

arquivo_conteudo=ler_conteudo_arquivo(caminho_arquivo_texto)



#************VALORES*****************

# Lista para armazenar as linhas que contêm "VALOR PAGO:"
linhas_valor_pago = []
# Dividir o texto em linhas e iterar sobre cada linha
for linha in arquivo_conteudo:
    # Verificar se "VALOR PAGO:" está presente na linha
    if "VALOR PAGO:" in linha:
        # Adicionar a linha à lista de resultados
        linha=linha.replace('VALOR PAGO:',"")
        linha=linha.replace('R',"")
        linha=linha.replace('$',"")
        linha=linha.replace(' ',"")
        linha=linha.replace('\n',"")
        linha=linhas_valor_pago.append(linha)
#gravação arquivo
        
# Abrir o arquivo para escrita
with open("C:\\Users\\Gabriel\\Downloads\\esse\\linhas_valor_pago.txt", 'w', encoding='utf-8') as arquivo:
    # Iterar sobre cada item da lista
    for item in linhas_valor_pago:
        # Escrever o item no arquivo, seguido por uma quebra de linha
        arquivo.write(item + '\n')

#FIM ************VALORES*****************      



#************DATAS *****************
linhas_data_pagto = []
# Dividir o texto em linhas e iterar sobre cada linha
for linha in arquivo_conteudo:
    # Verificar se "VALOR PAGO:" está presente na linha
    if "PAGAMENTO EFETUADO EM" in linha:
        # Adicionar a linha à lista de resultados
        
        # Substituindo o padrão encontrado por uma string vazia
        regex_data = r"\b\d{2}[./]\d{2}[./]\d{4}\b"
        # Encontrando a primeira ocorrência no texto
        match = re.search(regex_data, linha)

        # Se uma correspondência for encontrada, obter a string correspondente
        if match:
            linha = match.group()
            linha = linha.replace(".",'/')
        
        
        linhas_data_pagto.append(linha)

with open("C:\\Users\\Gabriel\\Downloads\\esse\\linhas_data_pagto.txt", 'w', encoding='utf-8') as arquivo:
    # Iterar sobre cada item da lista
    for item in linhas_data_pagto:
        # Escrever o item no arquivo, seguido por uma quebra de linha
        arquivo.write(item + '\n')

#FIM ************DATAS*****************
        

#************FORNECEDORES*****************
        
linhas_fornecedor = []
# Dividir o texto em linhas e iterar sobre cada linha
for linha in arquivo_conteudo:
    # Verificar se "VALOR PAGO:" está presente na linha
    if "FORNECEDOR:" in linha:
        # Adicionar a linha à lista de resultados
        linha=linha.replace("FORNECEDOR:",'')
        linha=linha.lstrip()
        linhas_fornecedor.append(linha)

with open("C:\\Users\\Gabriel\\Downloads\\esse\\linhas_fornecedor.txt", 'w', encoding='utf-8') as arquivo:
    # Iterar sobre cada item da lista
    for item in linhas_fornecedor:
        # Escrever o item no arquivo, seguido por uma quebra de linha
        arquivo.write(item + '\n')


#FIM ************FORNECEDORES*****************



# Suas listas de dados (ex.: datas, fornecedores, valores_pagos)
lista1 = linhas_data_pagto
lista2 = linhas_fornecedor
lista3 = linhas_valor_pago

max_len=max(len(lista1), len(lista2), len(lista3))
# Se quiser adicionar valores de preenchimento em vez de truncar, você pode fazer algo assim:
# max_len = max(len(lista1), len(lista2), len(lista3))

lista1 += [None] * (max_len - len(lista1))
lista2 += [None] * (max_len - len(lista2))
lista3 += [None] * (max_len - len(lista3))

# Criando um DataFrame com as listas como colunas
df = pd.DataFrame({'DATA': lista1, 'FORNECEDOR': lista2, 'VALOR': lista3})

# Especifique o nome do arquivo Excel desejado
nome_arquivo_excel = 'C:\\Users\\Gabriel\\Downloads\\esse\\minhas_listas.xlsx'

# Gravando o DataFrame no arquivo Excel, usando openpyxl como engine
df.to_excel(nome_arquivo_excel, index=False, engine='openpyxl')

print(f'Dados gravados com sucesso no arquivo {nome_arquivo_excel}')
