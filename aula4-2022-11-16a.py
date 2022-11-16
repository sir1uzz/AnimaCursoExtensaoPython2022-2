# 1o. passo: Importar a biblioteca
import sqlite3

# 2o. passo: Estabelecer a conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

# 3o. passo: Criar um objeto do tipo "Cursos"
cursor = conexao.cursor()

# 4o. passo: Comando SQL do banco
sql = "SELECT pessoa_id, nome_civil, tipo FROM pessoas"

# 5o. passo: Executar o comando SQL no SQLlite (no cursor)
cursor.execute(sql)

# 6o. passo: Exibir a consulta com todos os nomes de heróis e vilões do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print (pessoa)