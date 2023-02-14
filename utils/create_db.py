#adicionar no futuro uma verificação para alugar um livro
import sqlite3

try:
    con = sqlite3.connect("data/library.db")
    print('DB created successfully')
except:
    print('DB already exists')

cur = con.cursor()

def create_tables():
    cur.execute("CREATE TABLE IF NOT EXISTS category(name VARCHAR(45) NOT NULL, category_id INTEGER PRIMARY KEY AUTOINCREMENT)")

    cur.execute("CREATE TABLE IF NOT EXISTS book(title VARCHAR(45) NOT NULL, author VARCHAR(45) NOT NULL, year INTEGER NOT NULL,\
                publisher VARCHAR(45) NOT NULL, quantity INTEGER NOT NULL, price FLOAT NOT NULL, id INTEGER PRIMARY KEY AUTOINCREMENT,\
                category_id INTEGER NOT NULL, FOREIGN KEY (category_id) REFERENCES category(category_id))")

    cur.execute("CREATE TABLE IF NOT EXISTS employe(name VARCHAR(45) NOT NULL, date_birth DATE NOT NULL, password VARCHAR(45) NOT NULL,\
                cpf CHAR(11) PRIMARY KEY)")

    cur.execute("CREATE TABLE IF NOT EXISTS rent(book_id INTEGER NOT NULL, student_cpf CHAR(11) NOT NULL, start_time DATE NOT NULL,\
                end_time DATE NOT NULL, FOREIGN KEY (book_id) REFERENCES book(id), FOREIGN KEY (student_cpf) REFERENCES student(cpf),\
                PRIMARY KEY (book_id, student_cpf))")

    cur.execute("CREATE TABLE IF NOT EXISTS student(name VARCHAR(45) NOT NULL, date_birth DATE NOT NULL, address VARCHAR(45) NOT NULL,\
                cpf CHAR(11) PRIMARY KEY)")


def insert_into():
    #insert into category
    cur.execute("INSERT INTO category(name) VALUES('Literatura')")
    cur.execute("INSERT INTO category(name) VALUES('Matemática')")
    cur.execute("INSERT INTO category(name) VALUES('Computação')")
    cur.execute("INSERT INTO category(name) VALUES('Historia')")
    cur.execute("INSERT INTO category(name) VALUES('Química')")

    #insert into book
    cur.execute("INSERT INTO book(title, author, year, publisher, quantity, price, category_id)\
                VALUES ('Sistemas de Informação', 'Markus', 2019, 'Pearson', 10, 100.00, 3)")
    cur.execute("INSERT INTO book(title, author, year, publisher, quantity, price, category_id)\
                VALUES ('Teoria da Computação', 'Markus', 2002, 'Pearson', 3, 199.00, 3)")
    cur.execute("INSERT INTO book(title, author, year, publisher, quantity, price, category_id)\
                VALUES ('Ciência de Dados', 'dos Santos', 2023, 'Harbor', 5, 50.00, 3)")
    cur.execute("INSERT INTO book(title, author, year, publisher, quantity, price, category_id)\
                VALUES ('O mágico de Oz', 'L. Frank Baum', 1900, 'Harper', 10, 50.00, 1)")
    cur.execute("INSERT INTO book(title, author, year, publisher, quantity, price, category_id)\
                VALUES ('Algebra Linear', 'dos Santos', 2019, 'Pearson', 10, 100.00, 2)")
    cur.execute("INSERT INTO book(title, author, year, publisher, quantity, price, category_id)\
                VALUES ('A historia do mundo para quem tem pressa', 'Niall Ferguson', 2019, 'Harper', 10, 150.00, 4)")
    cur.execute("INSERT INTO book(title, author, year, publisher, quantity, price, category_id)\
                VALUES ('Os botões de Napoleão', 'Luiz Ruffato', 2019, 'Harper', 10, 150.00, 5)")

    #insert into employe
    cur.execute("INSERT INTO employe(name, date_birth, password, cpf) VALUES('Yuri', '2002-01-01', '123', '12345678901')")

    #insert into student
    cur.execute("INSERT INTO student(name, date_birth, address, cpf) VALUES('Maria', '1999-01-01', 'Rua 1', '12345678901')")
    cur.execute("INSERT INTO student(name, date_birth, address, cpf) VALUES('João', '1999-01-01', 'Rua 2', '12345678902')")
    cur.execute("INSERT INTO student(name, date_birth, address, cpf) VALUES('Pedro', '1999-01-01', 'Rua 3', '12345678903')")

    #insert into rent
    cur.execute("INSERT INTO rent(book_id, student_cpf, start_time, end_time) VALUES(1, '12345678901', '2020-01-01', '2020-01-10')")
    cur.execute("INSERT INTO rent(book_id, student_cpf, start_time, end_time) VALUES(2, '12345678901', '2020-01-01', '2020-01-10')")
    
    con.commit()
    print('Data commited successfully')

if __name__ == '__main__':
    create_tables()
    insert_into()
    cur.close()
    con.close()