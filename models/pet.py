import json
import os
import random

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Pet:
    def __init__(self, nome: str):
        self.nome = nome
        self.fome = 10        # 0-10
        self.felicidade = 10  # 0-10
        self.energia = 10     # 0-10
        self.qi = 1     # 0-10
        self.vida = 100     # 0-vidamax
        self.vidamax = 100     # 0-1000
        self.sujeira = 10 # 0-10
        self.vivo = True
        # morre se:
        # vida == 0
        # fome == 0
        # energia == 0
        # sujeira == 0
        # felicidade == 0

    def comer(self):
        r1 = random.randint(0,1)
        r2 = random.randint(0,1)
        self.fome = min(10, self.fome + 1 + r1)
        self.sujeira = max(0, self.sujeira - r2)

    def brincar(self):
        r1 = random.randint(0,1)
        r2 = random.randint(0,1)
        self.felicidade = min(10, self.felicidade + 1 + r1)
        self.sujeira = max(0, self.sujeira - r2)
        self.energia = max(0, self.energia - 1)

    def dormir(self):
        r1 = random.randint(0,1)
        r2 = random.randint(0,1)
        self.energia = min(10, self.energia + 1 + r1)
        self.fome = max(0, self.fome - 1)
        self.sujeira = max(0, self.sujeira - r2)

    def treinar(self):
        self.qi = min(1000, self.qi + 1)
        self.felicidade = max(0, self.felicidade - 1)
        self.sujeira = max(0, self.sujeira - 1)
        self.fome = max(0, self.fome - 1)
        self.vida = max(0, self.vida - 10)
        self.energia = max(0, self.energia - 1)

    def banhar(self):
        r1 = random.randint(0,1)
        r2 = random.randint(0,1)
        self.sujeira = min(10, self.sujeira + 1)
        self.energia = max(0, self.energia - r1)
        self.fome = max(0, self.fome - r2)

    def curar(self):
        r1 = random.randint(0,1)
        self.vida = min(self.vidamax, self.vida + 10)
        self.felicidade = max(0, self.felicidade - 1 - r1)

    def status(self):
        return {
            "nome": self.nome,
            "fome": self.fome,
            "felicidade": self.felicidade,
            "energia": self.energia,
            "sujeira": self.sujeira,
            "qi": self.qi,
            "vida": self.vida,
            "vidamax": self.vidamax,
            "vivo": self.vivo
        }

class PetModel:
    pass