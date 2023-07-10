
# Dump Postgres
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

## A final de contas, o que é 'Dump'? <br >

<p>Um dump de banco de dados, ou database dump, contém um registro da estrutura de tabela e ou dados de um banco de dados, e normalmente está na forma de uma lista de declarações SQL.<br> Em resumo um 'Dump', é um backup da estrutura de uma base de dados, copiando o Schema informado.</p>

Nesse caso, vamos fazer um dump do 
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
<br>
# Utilização
<br>
Antes de qualquer coisa, é necessário alterar os parametros de conexão com o seu Serviço do postgres.

Para alterar a conexão, atualize as variáveis:

<ul>
  <li><b>DB_HOST</b> - Link do servidor para conexão com o SGBD (CONEXÃO LOCAL: 127.0.0.1).</li>
  <li><b>DB_USER</b> - Nome de usuario do Banco.</li>
  <li><b>DB_PORT</b> - Porta de conexão do banco de dados (POSTGRES PADRÃO : 5432).</li>
  <li><b>DB_NAME</b> - Array com o nome dos seus Schemas, ['banco1', 'banco2'].</li>
</ul>
<br>

# Path
Agora para que se configure o diretório onde as pastas, arquivos serão gerados, coloque o script 'backuppostgres.py'<br> dentro de um novo diretório e crie uma pasta chamada <b>BackupPost</b> , que será onde os backups serão salvos.


# Raiz

Quando o seu ambiente estiver totalmente configurado, a raiz do seu projeto deverá se parecer com isso:

![RAIZ](https://github.com/iiiiiuri/Dump-Postgres/blob/main/Raiz.png?raw=true)

Todos os arquivos que o Script gerar, serão adicionados dentro da pasta <b>'Backup-ano-mes-dia'</b>, <br> que corresponde a data atual da execução.
# 


### Thanks for reading!!

![LogoIuri](https://raw.githubusercontent.com/iiiiiuri/DB-BLUE/a1c0c051c891ecd5f9a3f3c36a060bed6a85d912/static/img/logoIuri.svg)





