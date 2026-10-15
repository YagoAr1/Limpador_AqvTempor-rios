import os
import time

print("A limpeza começará em 5 segundos...")

for i in range(1, 6):
    time.sleep(1)
    print(f"Começando em: {i}")

pasta_temp = Caminho do arquivo temporário
pasta_temp2 = os.path.expandvars(Caminho do arquivo temporário)
pasta_prefetch = Caminho do arquivo temporário

arquivos_temp = os.listdir(pasta_temp)
arquivos_temp2 = os.listdir(pasta_temp2)
arquivos_prefetch = os.listdir(pasta_prefetch)

for arquivo in arquivos_temp:
    caminho = os.path.join(pasta_temp, arquivo)

    if os.path.isfile(caminho):

        try:
            os.remove(caminho)
            print("Arquivos do temp excluídos")

        except PermissionError:
            print("sem permissão")

        except OSError:
            print("Erro")

for arquivo in arquivos_temp2:
    caminho = os.path.join(pasta_temp2, arquivo)

    if os.path.isfile(caminho):

        try:
            os.remove(caminho)
            print("Arquivos do temp excluídos")

        except PermissionError:
            print("sem permissão")

        except OSError:
            print("Erro")


for arquivo in arquivos_prefetch:
    caminho = os.path.join(pasta_prefetch, arquivo)

    if os.path.isfile(caminho):

        try:
            os.remove(caminho)
            print("Arquivos do temp excluídos")

        except PermissionError:
            print("sem permissão")

        except OSError:
            print("Erro")



print("Tudo excluído perfeitamente")
    

