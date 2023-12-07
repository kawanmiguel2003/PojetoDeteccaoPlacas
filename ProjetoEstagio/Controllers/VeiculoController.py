import services.database as db
from typing import List
import models.Veiculo as veiculo

def IncluirVeiculos(veiculo):
    count = db.cursor.execute("""
    INSERT INTO Veiculos (modelo, cor, placa)
    VALUES (?,?,?)""",
    veiculo.modelo, veiculo.cor, veiculo.placa).rowcount
    db.cnxn.commit()

def SelecionarVeiculoById(id):
    db.cursor.execute("SELECT * FROM Veiculos WHERE idVeiculo =?", id)
    veiculoList = []

    for row in db.cursor.fetchall():
        veiculoList.append(veiculo.Veiculo(row[0],row[1],row[2],row[3]))
    return veiculoList[0]

def AlterarVeiculos(veiculo):
    count = db.cursor.execute("""
    UPDATE Veiculos
    SET modelo = ?, cor = ?, placa =?, )
    WHERE idVeiculo = ?""",
    veiculo.modelo, veiculo.cor, veiculo.placa, veiculo.idVeiculo).rowcount
    db.cnxn.commit()

def SelecionarTodosVeiculos():
    db.cursor.execute("SELECT * FROM Veiculos")
    veiculoList = []

    for row in db.cursor.fetchall():
        veiculoList.append(veiculo.Veiculo(row[0],row[1],row[2],row[3]))
    return veiculoList

def ExcluirVeiculo(id):
    count = db.cursor.execute("""
    DELETE FROM Veiculos WHERE idVeiculo =?""",
    id).rowcount

    db.cnxn.commit()