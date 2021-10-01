import mysql.connector
from mysql.connector import Error

conexao = mysql.connector.connect(user = "root", host = "127.0.0.1")
meucursor = conexao.cursor()

def conecta():
    try:
        conexao = mysql.connector.connect(user = "root", host = "127.0.0.1")
        meucursor.execute('USE bd_itermobi;')
        print('conectado')
        return conexao
    except:
        print("Não foi possível conectar ao SGBD. \nVerifique o XAMPP/WAMP ou os dados de conexão.")
        return 1

def cripto(palavra):
    c = ''
    for p in palavra:
        e = ord(p)

        if e % 2 == 0:
            d = f'{chr(e)}{chr(e-1)}'
            e = e//2
        else:
            if e == 33:
                d = f'{chr(e)}{chr(e+1)}'
                e *= 2
            else:
                d = f'{chr(e)}{chr(e+1)}'
                e *= 2

        c = (c+f'{e}{d}')
        return c

def registrar(nome, email, senha, deficiencia):
    try:
        meucursor.execute("INSERT INTO Usuarios(palavra) VALUES(%s, %s, %s, %s);", (nome, email, senha, deficiencia))
        conexao.commit()
        print('palavra adicionada')
    except Error as err:
        return 1

if __name__ == '__main__':
    conexao = conecta()
    if conexao != 1:
        conexao.close()