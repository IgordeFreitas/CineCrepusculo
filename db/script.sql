CREATE TABLE cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE filme (
    id_filme INT AUTO_INCREMENT PRIMARY KEY,
    nome TEXT NOT NULL,
    genero TEXT NOT NULL,
    sinopse TEXT NOT NULL,
    duracao TEXT NOT NULL
);

CREATE TABLE sala (
    id_sala INT AUTO_INCREMENT PRIMARY KEY,
    qtd_assento INT NOT NULL
);

CREATE TABLE sessao (
    id_sessao INT AUTO_INCREMENT PRIMARY KEY,
    id_filme INT NOT NULL,
    data_hora TIMESTAMP DEFAULT NOW(),
    id_sala INT NOT NULL,
    FOREIGN KEY (id_filme) REFERENCES filme (id_filme),
    FOREIGN KEY (id_sala) REFERENCES sala (id_sala)
);

CREATE TABLE pedido (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_sessao INT NOT NULL,
    assento TEXT NOT NULL,
    status ENUM ('disponivel', 'selecionado', 'ocupado'),
    data_pedido TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente),
    FOREIGN KEY (id_sessao) REFERENCES sessao (id_sessao)
);

CREATE TABLE produto (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome TEXT NOT NULL,
    preco NUMERIC(10,2) NOT NULL
);

CREATE TABLE pedido_produto (
    id_pedido INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL CHECK (quantidade > 0),
    PRIMARY KEY (id_pedido, id_produto),
    FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido),
    FOREIGN KEY (id_produto) REFERENCES produto (id_produto)9
);

-- INSERT

-- Clientes
INSERT INTO cliente (nome, endereco, email) VALUES
('Lara Ribeiro', 'Rua das Flores, 123', 'lara@email.com'),
('Carlos Souza', 'Av. Central, 456', 'carlos@email.com'),
('Marina Lima', 'Rua das Palmeiras, 789', 'marina@email.com');

-- Filmes
INSERT INTO filme (nome, genero, sinopse, duracao) VALUES
('O Segredo das Estrelas', 'Ficção Científica', 'Exploradores descobrem vida em outro planeta.', '2h10min'),
('Amor em Paris', 'Romance', 'Um casal se reencontra após anos separados.', '1h45min'),
('Missão Submarina', 'Ação', 'Uma equipe tenta salvar o mundo debaixo do mar.', '2h05min');

-- Salas
INSERT INTO sala (qtd_assento) VALUES (100), (80), (60);

-- Sessões
INSERT INTO sessao (id_filme, data_hora, id_sala) VALUES
(1, '2025-10-27 19:30:00', 1),
(2, '2025-10-27 20:00:00', 2),
(3, '2025-10-28 18:00:00', 3);

-- Pedidos
INSERT INTO pedido (id_cliente, id_sessao, assento, status) VALUES
(1, 1, 'A10', 'ocupado'),
(2, 2, 'B05', 'ocupado'),
(3, 3, 'C03', 'selecionado');

-- Produtos
INSERT INTO produto (nome, preco) VALUES
('Pipoca Média', 15.00),
('Refrigerante 500ml', 8.00),
('Chocolate', 6.50);

-- Pedido + Produtos
INSERT INTO pedido_produto (id_pedido, id_produto, quantidade) VALUES
(1, 1, 1),
(1, 2, 2),
(2, 3, 1);

-- (SELECT)

--  Listar todos os clientes
SELECT * FROM cliente;

-- Listar todos os filmes
SELECT * FROM filme;

-- Ver sessões com nome do filme e sala
SELECT 
    s.id_sessao,
    f.nome AS filme,
    s.data_hora,
    sa.qtd_assento AS capacidade_sala
FROM sessao s
JOIN filme f ON s.id_filme = f.id_filme
JOIN sala sa ON s.id_sala = sa.id_sala;

-- Ver pedidos com nome do cliente, filme e status
SELECT 
    p.id_pedido,
    c.nome AS cliente,
    f.nome AS filme,
    p.assento,
    p.status,
    p.data_pedido
FROM pedido p
JOIN cliente c ON p.id_cliente = c.id_cliente
JOIN sessao s ON p.id_sessao = s.id_sessao
JOIN filme f ON s.id_filme = f.id_filme;

-- Ver produtos comprados em cada pedido
SELECT 
    p.id_pedido,
    pr.nome AS produto,
    pr.preco,
    pp.quantidade,
    (pr.preco * pp.quantidade) AS total_item
FROM pedido_produto pp
JOIN produto pr ON pp.id_produto = pr.id_produto
JOIN pedido p ON pp.id_pedido = p.id_pedido;

--  Calcular valor total de cada pedido
SELECT 
    p.id_pedido,
    c.nome AS cliente,
    SUM(pr.preco * pp.quantidade) AS total_pedido
FROM pedido_produto pp
JOIN produto pr ON pp.id_produto = pr.id_produto
JOIN pedido p ON pp.id_pedido = p.id_pedido
JOIN cliente c ON p.id_cliente = c.id_cliente
GROUP BY p.id_pedido, c.nome;

-- (UPDATE)

--Atualizar o endereço de um cliente
UPDATE cliente
SET endereco = 'Rua Nova Esperança, 500'
WHERE id_cliente = 1;

-- Mudar o status de um pedido
UPDATE pedido
SET status = 'ocupado'
WHERE id_pedido = 3;

-- Alterar o preço de um produto
UPDATE produto
SET preco = 9.50
WHERE nome = 'Refrigerante 500ml';

--  Atualizar o horário de uma sessão
UPDATE sessao
SET data_hora = '2025-10-28 21:00:00'
WHERE id_sessao = 1;

-- (DELETE)

--  Excluir um produto específico
DELETE FROM produto
WHERE nome = 'Chocolate';

-- Excluir um pedido e seus produtos associados
DELETE FROM pedido_produto
WHERE id_pedido = 2;

DELETE FROM pedido
WHERE id_pedido = 2;

--  Excluir um cliente (apenas se não tiver pedidos)
DELETE FROM cliente
WHERE id_cliente = 3;

-- Excluir uma sessão (se não tiver pedidos associados)
DELETE FROM sessao
WHERE id_sessao = 3;