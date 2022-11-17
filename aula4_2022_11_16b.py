# 1o. passo: Importar a biblioteca
import sqlite3

# 2o. passo: Estabelecer a conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

# 3o. passo: Criar um objeto do tipo "Cursos"
cursor = conexao.cursor()

# 4o. passo: Comando SQL do banco
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'Ravena', 'Rachel Roth', 'Herói(na)')"

# 5o. passo: Executar o comando SQL no SQLlite (no cursor)
cursor.execute(sql)

# 6o. passso: Confirma o INSERT com commit() e fecha o banco
conexao.commit()
conexao.close()