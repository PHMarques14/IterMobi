from tkinter import *
import mysql.connector
from mysql.connector import Error
from threading import Timer

#BANCO DE DADOS#

conexao = mysql.connector.connect(user = "root", host = "127.0.0.1")
meucursor = conexao.cursor()

def conecta():
    try:
        conexao = mysql.connector.connect(user = "root", host = "127.0.0.1")
        meucursor.execute('CREATE DATABASE bd_itermobi;')
        meucursor.execute('USE bd_itermobi;')
        print('conectado')
        return conexao
    except:
        print("Não foi possível conectar ao SGBD. \nVerifique o XAMPP/WAMP ou os dados de conexão.")
        return 1

def criaTabela():
    try:
        meucursor.execute('CREATE TABLE Usuarios(palavra);')
    except:
        print('A tabela já foi criada.')

def registrar(nome, email, senha):
            try:
                meucursor.execute("INSERT INTO Usuarios(palavra) VALUES(%s, %s, %s);", (nome, email, senha))
                conexao.commit()
                print('palavra adicionada')
            except Error as err:
                return 1

def cadastrar(self):
        self.__senha = cripto(self.__senha)

        r= registrar(self.nome, self.email, self.__senha, self.deficienciaVisual)

        if r == 1:
            pass
        else:
            pass