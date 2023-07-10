import os
import time

# Credenciais de banco de dados PostgreSQL
DB_HOST = 'host'
DB_USER = 'username'
DB_PORT = 'port'

# Array com o nome das suas bases de dados
DB_NAME = ['banco1', 'banco2', 'banco3']

h = 'h'
m = 'm'
s = 's'


# CREDENCIAL DE HORA
hour = f'%H{h}_%M{m}_%S{s}'
day = f'%Y-%m-%d'
current_time = time.strftime(hour)
current_day = time.strftime(day)


# CRIANDO DIRETORIO
diretorio = f"C:\\BackupPost\\Backup-{current_day}"
os.makedirs(diretorio, exist_ok=True)

# PATH PARA ARMAZENAR O BACKUP
backupNovo = f"{diretorio}"

# ARMAZENANDO O BACKUP NA PASTA GERADA
for bancos in DB_NAME:

    # Nome do arquivo de backup
    backup_file = f'{bancos}-{current_time}.sql'

    # Caminho completo do arquivo de backup
    backup_file_path = os.path.join(backupNovo, backup_file)

    # Comando pg_dump para criar o backup do banco de dados atual
    pg_dump_cmd = f'pg_dump -h {DB_HOST} -U {DB_USER} -Fp -p {DB_PORT} -d {bancos} --inserts -f {backup_file_path}'

    # Executa o comando pg_dump
    os.system(pg_dump_cmd)
