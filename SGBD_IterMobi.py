from random import randint
import mysql.connector
from mysql.connector import Error
import smtplib

global meucursor

conexao = mysql.connector.connect(user = "root", host = "127.0.0.1")
meucursor = conexao.cursor(buffered=True)

def conecta():
    try:
        conexao = mysql.connector.connect(user = "root", host = "127.0.0.1")
        print('conectado')
        return conexao
    except:
        print("Não foi possível conectar ao SGBD. \nVerifique o XAMPP/WAMP ou os dados de conexão.")
        return 1

def useBanco():
    try:
        meucursor.execute('USE bd_itermobi;')
        print('Conexao estabelecida \nbd_itermobi ok')
    except:
        print('Conexao estabelecida \nbd_itermobi ok')

def registrar(nome, email, senha):
    try:
        meucursor.execute("INSERT INTO Usuarios (nome, email, senha) VALUES(%s, %s, %s);", (nome, email, senha))
        print('cadastrado')
        conexao.commit()
    except:
        print('Não foi possível cadastrar. Usuário já existe.')
        return 0
    
def verificarConta(email):
    try:
        email = str(email)
        meucursor.execute("SELECT email FROM Usuarios WHERE email = '{}';".format(email))
        print(email)
        for i in meucursor:
            l = []
            for x in i:
                l.append(x)
        e = l[0]
        return e
    except UnboundLocalError:
        return ''
        

def verificarSenha(email, senha):
    meucursor.execute("SELECT senha FROM Usuarios WHERE email = '{}';".format(email))
    
    for i in meucursor:
        l = []
        for x in i:
            l.append(x)
    s = l[0]
    print(s)
    s = str(s)
    c = ''
    for p in senha:
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
    if c == s:
        return 0
    else:
        return 1

def procurar(onibus):
    try:
        tipo = int(onibus)
        print(type(tipo))
        try:
            meucursor.execute("SELECT trajeto FROM trajetos WHERE id_onibus = '{}';".format(onibus))
            l = []
            for i in meucursor:
                for x in i:
                    l.append(x)
            return l
        except UnboundLocalError:
            return 1
    except:
        tipo = str(onibus)
        try:
            meucursor.execute("SELECT trajeto FROM trajetos WHERE trajeto LIKE '%{}%';".format(onibus))
            for i in meucursor:
                l = []
                for x in i:
                    l.append(x)
            return l
        except UnboundLocalError:
            return 1        

def locNome(email):
    try:
        meucursor.execute("SELECT nome FROM usuarios WHERE email = '{}';".format(email))
        for i in meucursor:
            l = []
            for x in i:
                l.append(x)
        return l[0]
    except:
        return 1        

if __name__ == '__main__':
    conexao = conecta()
    if conexao != 1:
        meucursor = conexao.cursor(buffered=True)
        conecta()
        useBanco()

        conexao.close()