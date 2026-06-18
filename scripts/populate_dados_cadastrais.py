import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from app import create_app, db
from app.models import DadoFuncional

def to_date_native(valor):
    """Converte Timestamp do pandas para date nativo do Python, ou None se for NaT/NaN."""
    if pd.isna(valor):
        return None
    return valor.date()

def popular_banco(caminho_arquivo):
    # Ligamos o app do Flask para podermos conversar com o banco de dados
    app = create_app()
    with app.app_context():
        print(f"Lendo o arquivo: {caminho_arquivo}...")

        try:
            # O Pandas lê o .xlsx
            df = pd.read_excel(caminho_arquivo, sheet_name="dados_funcionais")
        except FileNotFoundError:
            print("Arquivo não encontrado! Verifique o nome e se ele está na mesma pasta.")
            return
        
        # Tratamento de Datas: Converte texto (DD/MM/AAAA) para formato de data nativo
        # O errors='coerce' faz com que, se tiver uma data inválida, ele vire None em vez de quebrar tudo
        df['Data Completa'] = pd.to_datetime(df['Data Completa'], errors='coerce', dayfirst=True)
        df['Data Exercício'] = pd.to_datetime(df['Data Exercício'], errors='coerce', dayfirst=True)

        cadastrados = 0
        ignorados = 0

        print("Injetando dados no banco... Isso pode levar alguns segundos.")

        # Varre a planilha linha por linha
        for index, row in df.iterrows():
            
            # Verifica se esse servidor já está no banco para não duplicar
            query = db.select(DadoFuncional).where(DadoFuncional.masp == row['MASP'], DadoFuncional.num_admissao == row['Nº Admissão'])
            servidor_existente = db.session.scalar(query)

            if not servidor_existente:
                # Cria o "molde" do servidor com a nossa classe
                novo_servidor = DadoFuncional(
                    masp=row['MASP'],
                    num_admissao=row['Nº Admissão'],
                    nome_servidor=row['Nome Servidor'],
                    data_nascimento=to_date_native(row['Data Completa']), # Atenção: aqui ele puxa a data já tratada
                    data_inicio_exercicio=to_date_native(row['Data Exercício']),
                    cod_idade=row['Cod Idade'],
                    cod_sexo=row['Cod Sexo'],
                    cod_carreira=row['Cod Carreira'],
                    situacao_funcional=row['Situação Funcional'],
                    situacao_servidor=row['Situação Servidor']
                )
                
                # Adiciona na fila do banco
                db.session.add(novo_servidor)
                cadastrados += 1
            else:
                ignorados += 1

        # Salva tudo de uma vez (muito mais rápido do que salvar linha por linha)
        db.session.commit()
        
        print("\nImportação Concluída com Sucesso!")
        print(f"Servidores cadastrados: {cadastrados}")
        print(f"Servidores já existentes (ignorados): {ignorados}")

# COLOQUE AQUI O NOME EXATO DO SEU ARQUIVO CSV
nome_do_arquivo = "data/dados_cadastrais.xlsx" 
popular_banco(nome_do_arquivo)