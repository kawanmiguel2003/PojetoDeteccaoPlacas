import string
from typing import List
import services.database as db
import models.Pessoa as pessoa
import numpy as np


def Incluir(pessoa):
    count = db.cursor.execute("""
    INSERT INTO Pessoa (nome, RA, CPF, idVeiculo)
    VALUES (?,?,?,?)""",
    pessoa.nome, pessoa.ra, pessoa.cpf, pessoa.idVeiculo).rowcount
    db.cnxn.commit()

def SelecionarById(id):
    db.cursor.execute("SELECT * FROM Pessoa WHERE idPessoa = ?", id)
    pessoaList = []

    for row in db.cursor.fetchall():
        pessoaList.append(pessoa.Pessoa(row[0],row[1],row[2],row[3],row[4]))
    return pessoaList[0]

def Alterar(pessoa):
    print("alterando...")
    count = db.cursor.execute("""
    UPDATE Pessoa 
    SET Nome = ?, RA = ?, CPF =?, idVeiculo = ?
    WHERE idPessoa = ?
    """,
    pessoa.nome, pessoa.ra, pessoa.cpf, pessoa.idVeiculo, pessoa.id).rowcount
    db.cnxn.commit()
def SelecionarTodos():
    db.cursor.execute("SELECT * FROM PESSOA")
    pessoaList = []

    for row in db.cursor.fetchall():
        pessoaList.append(pessoa.Pessoa(row[0],row[1],row[2],row[3],row[4]))
    return pessoaList

def Excluir(id):
    count = db.cursor.execute("""
    DELETE FROM PESSOA WHERE idPessoa = ?""",
    id).rowcount
    db.cnxn.commit()