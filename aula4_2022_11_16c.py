# 1o. passo: Importar a biblioteca
import sqlite3

# Passos 2o. e 3o. virão funcionar conectar()
def conectar():
# 2o. passo: Estabelecer a conexão com o banco de dados
  conexao = sqlite3.connect("dc_universe.db")
# 3o. passo: Criar um objeto do tipo "Cursos"
  cursor = conexao.cursor()
  return conexao, cursor