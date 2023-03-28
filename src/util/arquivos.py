import io
import csv
import os
from src.scrapers.imobiliario.entidades.imovel import Imovel

def escrever_html(saida, nome_arquivo):
    # Cria um objeto StringIO que funciona como um arquivo em memória
    file = io.StringIO()
    
    # Escreve a saída no objeto StringIO
    file.write(saida)
    
    # Obtém o conteúdo do objeto StringIO como uma string
    conteudo = file.getvalue()
    
    # Grava o conteúdo em um arquivo HTML
    with open(f"html/{nome_arquivo}", 'w') as f:
        f.write(conteudo)
        
def adicionar_objeto_a_arquivo_csv(objeto, nome_arquivo_sem_extensao):
    
    # Verificar se a pasta data existe, caso contrário, criar
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Definir o caminho completo do arquivo CSV
    file_path = os.path.join("data", f"{nome_arquivo_sem_extensao}.csv")

    # Verificar se o arquivo já existe
    file_exists = os.path.exists(file_path)

    # Abrir o arquivo CSV em modo de escrita e criar um objeto escritor
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)

        # Se o arquivo não existir, escrever o cabeçalho com os nomes dos atributos
        if not file_exists:
            header = [attr for attr in objeto.__dict__.keys()]
            writer.writerow(header)

        # Escrever uma nova linha com os valores dos atributos
        row = [value for value in objeto.__dict__.values()]
        writer.writerow(row)