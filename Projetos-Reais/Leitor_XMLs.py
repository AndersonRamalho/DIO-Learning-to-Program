import xmltodict
import os
import json


def pegar_infos(nome_arquivo):
    print(f"Pegou as informações {nome_arquivo}")
    with open(f'C:/Users/Anderson/OneDrive/Documentos/XMLs_NFe/{nome_arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        try:
            infos_nf = dic_arquivo["nfeProc"]["NFe"]['infNFe']
            numero_nfe = infos_nf['ide']['nNF']
            data_emissao = infos_nf['ide']['dhEmi']
            empresa_emissora = infos_nf['emit']['xNome']
            CNPJ_emissor = infos_nf['emit']['CNPJ']
            nome_cliente = infos_nf['dest']['xNome']
            CNPJ_cliente = infos_nf['dest']['CNPJ']
            # valor_nfe = infos_nf['total']['vProd']
            # qtde_nfe = infos_nf['transp']['vol']['qvol']
            # um_nfe = infos_nf['transp']['vol']['esp']
            nf_referenciada = infos_nf['ide']['NFref']['refNFe']
            print(numero_nfe, empresa_emissora, nf_referenciada, sep="\n")
        except Exception as e:
            print(e)
            # print(json.dumps(dic_arquivo, indent=4))



lista_arquivos = os.listdir("C:/Users/Anderson/OneDrive/Documentos/XMLs_NFe")

for arquivo in lista_arquivos:
    pegar_infos(arquivo)
    break