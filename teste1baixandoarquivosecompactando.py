import wget
from zipfile import ZipFile, ZIP_DEFLATED

link1 = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN592.pdf'
nome_arquivo = 'Procedimento_ANEXO_I.pdf'
download_primeiro_arquivo = wget.download(link1, nome_arquivo)

link2 = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN596.pdf'
nome_arquivo_2 = 'diretrizes_ANEXO2.pdf'
download_segundo_arquivo = wget.download(link2, nome_arquivo_2)

zip = ZipFile('arquivo_compactado.zip', 'w', compression=ZIP_DEFLATED)
zip.write('Procedimento_ANEXO_I.pdf')
zip.write('diretrizes_ANEXO2.pdf')