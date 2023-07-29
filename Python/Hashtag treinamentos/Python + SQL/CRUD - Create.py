import pyodbc
print(pyodbc.drivers())

dados_conexao = ("Driver={SQLite3 ODBC Driver};""Server=localhost;""Database=salarios.sqlite")
#caso precise de login e senha:
#       ..."UID=Login;""PWD=Senha;")

conexao = pyodbc.connect(dados_conexao)
print("Conexão bem sucedida")
