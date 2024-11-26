-- Criando uma base de dados
create database vendas 
default character set utf8 -- Padrão de character latino 
default collate utf8_general_ci;

-- Selecionado nossa base
use vendas;

-- Criando tabela clientes
create table clientes (
cpf varchar(11) not null,
nome varchar(20) not null,
dt_nasc date,
tel varchar(11),
primary key(cpf)
) default charset = utf8;

-- Inserindo dados fictícios na tabela
insert into clientes values
    ('12345678901', 'João Silva', '1990-05-15', '11987654321'),
    ('98765432109', 'Maria Santos', '1985-08-20', '11955551234'),
    ('45678901234', 'Pedro Oliveira', '2000-02-10', '11933334444'),
    ('78901234567', 'Ana Pereira', '1998-11-30', '11922223333'),
    ('23456789012', 'Carlos Souza', '1988-04-05', '11944445555'),
    ('34567890123', 'Lúcia Almeida', '1995-09-25', '11966667777'),
    ('56789012345', 'Rafael Mendes', '1993-07-12', '11977778888'),
    ('67890123456', 'Fernanda Costa', '1992-03-18', '11988889999'),
    ('78901234568', 'Lucas Rodrigues', '1987-12-05', '11911112222'),
    ('89012345678', 'Isabela Ferreira', '1997-10-22', '11944446666'),
    ('90123456789', 'Gustavo Lima', '1989-06-08', '11955557777'),
    ('23456789013', 'Camila Santos', '1994-04-02', '11966668888'),
    ('34567890124', 'Eduardo Oliveira', '1991-01-10', '11977779999'),
    ('56789012346', 'Amanda Pereira', '1996-08-28', '11988881111'),
    ('67890123457', 'Ricardo Souza', '1986-11-15', '11999992222'),
    ('78901234569', 'Patrícia Almeida', '1999-09-20', '11911113333'),
    ('89012345679', 'Henrique Mendes', '1993-02-14', '11944445555'),
    ('90123456790', 'Carolina Costa', '1988-07-01', '11955556666'),
    ('23456789014', 'Thiago Rodrigues', '1997-05-17', '11966667777'),
    ('34567890125', 'Larissa Ferreira', '1995-12-10', '11977778888'),
    ('56789012347', 'Bruno Lima', '1990-03-22', '11988889999'),
    ('67890123458', 'Mariana Santos', '1984-09-08', '11911112222'),
    ('78901234570', 'Alexandre Oliveira', '1998-06-25', '11944443333'),
    ('89012345680', 'Juliana Pereira', '1992-11-12', '11955554444'),
    ('90123456791', 'Leonardo Souza', '1987-04-30', '11966665555'),
    ('23456789015', 'Vanessa Almeida', '1994-01-05', '11977776666'),
    ('34567890126', 'Rodrigo Mendes', '1996-07-23', '11988887777'),
    ('56789012348', 'Fernanda Costa', '1989-12-18', '11911118888');

-- Criando a coluna idade
alter table clientes
add column idade tinyint;

-- Configurando a coluna idade para receber o valor da data atual menos a data de nascimento
-- O cálcul retorna o número de dias, então fiz a divisão por 365 para receber os anos de idade
UPDATE clientes
SET idade = DATEDIFF(CURRENT_DATE, dt_nasc) / 365;

select * from clientes
limit 5;
