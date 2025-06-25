import pandas as pd

# Altere aqui os nomes, adicione no arquivo de entrada o nome salvo da lista.
arquivo_entrada = "lista.csv"
arquivo_saida = "lista_corrigida.csv"

df = pd.read_csv(arquivo_entrada, encoding="latin1", sep=";")
df.columns = df.columns.str.strip()

def tentar_corrigir(texto):
    if isinstance(texto, str):
        try:
            return texto.encode("latin1").decode("utf-8")
        except UnicodeDecodeError:
            return texto
    return texto

for coluna in df.select_dtypes(include=['object']).columns:
    df[coluna] = df[coluna].apply(tentar_corrigir)

df.to_csv(arquivo_saida, index=False, encoding="utf-8", sep=";")

print(f"✅ Arquivo corrigido salvo como '{arquivo_saida}'")
