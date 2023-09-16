import xmltodict
import os
import pandas as pd

def pegar_infos(nome_arquivo, valores):
    # print(f"Pegou as informações {nome_arquivo}")
    with open(f'C:/Users/Anderson/OneDrive/Documentos/XMLs_NFe/{nome_arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)

        infos_nf = dic_arquivo["nfeProc"]["NFe"]['infNFe']
        numero_nfe = infos_nf['ide']['nNF']
        data_emissao = infos_nf['ide']['dhEmi']
        empresa_emissora = infos_nf['emit']['xNome']
        CNPJ_emissor = infos_nf['emit']['CNPJ']
        nome_cliente = infos_nf['dest']['xNome']
        CNPJ_cliente = infos_nf['dest']['CNPJ']

        if "NFref" in infos_nf['ide']:
            nf_referenciada = infos_nf['ide']['NFref']['refNFe']
        else:
            nf_referenciada = "Sem NF Referencia"
        
        valor_nfe = infos_nf["total"]["ICMSTot"]["vProd"]

        if "vol" in infos_nf["transp"]:
            qtde_nfe = infos_nf['transp']['vol']['qVol']
        else:
            qtde_nfe = "Qtde NF não encontrado"

        if "vol" in infos_nf["transp"]:
            um_nfe = infos_nf['transp']['vol']['esp']
        else:
            um_nfe = "UM não encontrada"

        valores.append([numero_nfe, data_emissao, empresa_emissora, 
                       CNPJ_emissor, nome_cliente, CNPJ_cliente, 
                       nf_referenciada, valor_nfe, 
                       qtde_nfe, um_nfe]
                       )

lista_arquivos = os.listdir("C:/Users/Anderson/OneDrive/Documentos/XMLs_NFe")

colunas = ["numero_NFe", "Data_emissao", "Emissor", 
           "CNPJ_Emissor", "Destinatario", "CNPJ_Dest", 
           "NF_Referenciada", "Valor_NFe", "Qtde_NFe", 
           "UM_NFe"
           ]

valores = []

for arquivo in lista_arquivos:
    pegar_infos(arquivo, valores)
    
tabela = pd.DataFrame(columns=colunas, data=valores)
tabela.to_excel(f"C:/Users/Anderson/OneDrive/Documentos/XMLs_NFe/NFDs.xlsx", index=False)


# print(tabela)
