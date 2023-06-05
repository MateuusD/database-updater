import pymysql

# Conexão do banco
conn = pymysql.connect(host='localhost', user='seu_usuario', password='sua_senha', database='seu_banco_de_dados')
cursor = conn.cursor()

# Percorrendo todas as tabelas
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

# Aqui se executa o script SQL em todas as colunas e tabelas do banco, insira os valores que quer encontrar e substituir
for table in tables:
    table_name = table[0]

    # Percorrendo todas as colunas
    cursor.execute(f"DESCRIBE {table_name}")
    columns = cursor.fetchall()

    # Gerando a consulta SQL dinamicamente para cada coluna
    for column in columns:
        column_name = column[0]
        query = f"UPDATE {table_name} SET {column_name} = REPLACE({column_name}, 'encontra-isso', 'substitui-por-isso')"
        cursor.execute(query)

# Confimarndo as alterações
conn.commit()

# Fechando as conexões com o banco 
conn.close()
