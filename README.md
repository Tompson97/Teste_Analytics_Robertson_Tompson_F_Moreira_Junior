
# DASHBOARD VAREJO
## INTRODUÇÃO
Este projeto foi desenvolvido para criar um dashboard de vendas utilizando as ferramentas MySQL, Power e Github.
Os dados são fictícios.
Inciaremos com a criação da base de dados no MySQl, tratamento dos dados e quando a estrutura está normalizada vamos conectar no Power BI para desenvolver os relatórios.





## CRIAÇÃO DA BASE DE DADOS 
Utilizaremos a linguagem MySQL para criar toda a estrutra dos dados, então vamos começar.

Estou criando um database chamados "vendas" utilizando os padrões de caracteres brasileiros "utf8" para ele aceitar palavras com acentos.
```
create database vendas 
default character set utf8
default collate utf8_general_ci;
```
Após criar o database vamos selecioná-lo.
```
use vendas; 
```
Com a base selecionada podemos seguir com a criação da primeira tabela chamada "clientes".
Usaremos o CPF como chave primária, pois é um dado único dentro de todos os registros.
```
create table clientes (
cpf varchar(11) not null,
nome varchar(20) not null,
dt_nasc date,
tel varchar(11),
primary key(cpf)
) default charset = utf8;
```
Agora vamos inserir alguns dados fictícios na tabela usando esse padrã e depois vamos executar um Select para conferir.
```
insert into clientes values
('12345678901', 'João Silva', '1990-05-15', '11987654321'),

('98765432109', 'Maria Santos', '1985-08-20', '11955551234'),

select * from clientes;

```
Vamos criar uma coluna para calcular a idade com base na data de nascimento. Como a idade é um número pequeno que não ultrapassará 256 vamos atribuir o tipo tinyint que é semelhante ao int, mas para número menores.
Você pode utilziar o int, mas o tinyint irá reduzir o espaço ocupado na memória.
A função DATEDIFF irá retornar a diferença entre duas datas que na instrução foram CURRENT_DATA data atual para dt_nasc que é a data de nascimento, o resultado gerado é em número de dias e façoa divisão por 365 para chegar no número de anos e portanto a idade.

```
alter table clientes
add column idade tinyint;

UPDATE clientes
SET idade = 
DATEDIFF(CURRENT_DATE, dt_nasc) / 365;
```