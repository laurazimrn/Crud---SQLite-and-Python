import sqlite3 as con

sql_clientes = '''
    CREATE TABLE IF NOT EXISTS Cliente (
        ID_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        RG VARCHAR(12) NOT NULL,
        Nome_Cliente VARCHAR(30) NOT NULL,
        Sobrenome_Cliente VARCHAR(40),
        Telefone VARCHAR(15),
        Rua VARCHAR(40),
        Numero VARCHAR(5),
        Bairro VARCHAR(25)
    );
'''

sql_produtos = '''
    CREATE TABLE IF NOT EXISTS Produto (
        ID_Produto INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome_Produto VARCHAR(30) NOT NULL,
        Descricao_Produto VARCHAR(100),
        Preco DECIMAL(10, 2) NOT NULL,
        Estoque SMALLINT NOT NULL
    );
'''

sql_vendas = '''
    CREATE TABLE IF NOT EXISTS Venda (
        ID_Transacao INTEGER PRIMARY KEY AUTOINCREMENT,
        Nota_Fiscal SMALLINT NOT NULL,
        ID_Cliente INTEGER NOT NULL,
        Data_Compra DATETIME,
        ID_Produto INT NOT NULL,
        Quantidade SMALLINT NOT NULL,
        FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente),
        FOREIGN KEY (ID_Produto) REFERENCES Produto(ID_Produto)
    );
'''

try:
    conexao = con.connect('loja.db')
    cursor = conexao.cursor()
    
    cursor.execute(sql_clientes)
    cursor.execute(sql_produtos)
    cursor.execute(sql_vendas)
    conexao.commit()

except con.DatabaseError as erro:
    print("Erro no banco de dados:", erro)
    
finally:
    if conexao:
        conexao.close()


insere_cliente = '''
    INSERT INTO Cliente (RG, Nome_Cliente, Sobrenome_Cliente, Telefone, Rua, Numero, Bairro)
    VALUES
    ('312654987', 'Mariana', 'Silva', '11984563214', 'Rua das Flores', '120', 'Ipiranga'),
    ('365214987', 'Carlos', 'Pereira', '11896321457', 'Avenida Paulista', '1578', 'Bela Vista'),
    ('398745621', 'Renata', 'Almeida', '11975463218', 'Rua Vergueiro', '3050', 'Vila Mariana'),
    ('412369875', 'Lucas', 'Ferreira', '11963254789', 'Rua Domingos de Morais', '850', 'Saúde'),
    ('456987321', 'Patricia', 'Oliveira', '11784563219', 'Rua Haddock Lobo', '980', 'Jardins'),
    ('498763215', 'André', 'Moura', '11987456321', 'Rua Conselheiro Furtado', '430', 'Liberdade'),
    ('523698741', 'Beatriz', 'Ramos', '11963258741', 'Rua da Mooca', '2150', 'Mooca'),
    ('587412963', 'Eduardo', 'Nogueira', '11874563210', 'Rua Apeninos', '410', 'Aclimação');
'''

try:
    conexao = con.connect('loja.db')
    cursor = conexao.cursor()

    cursor.execute(insere_cliente)

    conexao.commit()    
except con.DatabaseError as erro:
    print("Erro no banco de dados", erro)
else:    
    # Verificar se dados foram cadastrados
    res = cursor.execute("SELECT * FROM Cliente;")
    print(res.fetchall())
finally:
    if conexao:
        conexao.close()
        
insere_produto = '''
    INSERT INTO Produto (Nome_Produto, Descricao_Produto, Preco, Estoque)
    VALUES
    ('Notebook Dell', 'Notebook Dell Inspiron 15 3000, Intel Core i5, 8GB RAM, 256GB SSD', 3500.00, 15),
    ('Smartphone Samsung', 'Smartphone Samsung Galaxy S21, 128GB, Tela 6.2", Câmera Tripla', 2800.00, 30),
    ('Fone de Ouvido JBL', 'Fone de Ouvido JBL Tune 500BT, Bluetooth, Preto', 250.00, 50),
    ('Monitor LG', 'Monitor LG 24", Full HD, HDMI, VGA', 900.00, 20),
    ('Teclado Mecânico', 'Teclado Mecânico Redragon Kumara K552, RGB, Switch Outemu Blue', 300.00, 40),
    ('Mouse Gamer Logitech', 'Mouse Gamer Logitech G502 HERO, RGB, 16000 DPI', 350.00, 25),
    ('Impressora HP', 'Impressora HP DeskJet 2755 All-in-One, Wi-Fi', 450.00, 10),
    ('Tablet Apple iPad', 'Tablet Apple iPad 10.2", Wi-Fi, 64GB, Cinza Espacial', 3200.00, 18);
'''

try:
    conexao = con.connect('loja.db')
    cursor = conexao.cursor()

    cursor.execute(insere_produto)
    conexao.commit()
except con.DatabaseError as erro:
    print("Erro no banco de dados", erro)
else:
    res = cursor.execute("SELECT * FROM Produto;")
    print(res.fetchall())
finally:
    if conexao:
        conexao.close()

insere_venda = '''
    INSERT INTO Venda (Nota_Fiscal, ID_Cliente, Data_Compra, ID_Produto, Quantidade)
    VALUES
    (1001, 1, '2024-01-15 10:30:00', 2, 1),
    (1002, 3, '2024-01-16 14:45:00', 1, 1),
    (1003, 2, '2024-01-17 09:20:00', 5, 2),
    (1004, 5, '2024-01-18 16:10:00', 3, 1),
    (1005, 4, '2024-01-19 11:05:00', 4, 1),
    (1006, 6, '2024-01-20 13:30:00', 6, 1),
    (1007, 7, '2024-01-21 15:50:00', 8, 1),
    (1008, 8, '2024-01-22 12:15:00', 7, 1);
'''

try:
    conexao = con.connect('loja.db')
    cursor = conexao.cursor()

    cursor.execute(insere_venda)
    conexao.commit()
except con.DatabaseError as erro:
    print("Erro no banco de dados", erro)
else:
    # Verificar se dados foram cadastrados
    res = cursor.execute("SELECT * FROM Venda;")
    print(res.fetchall())
finally:
    if conexao:
        conexao.close()