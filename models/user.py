import json
import os
from dataclasses import dataclass, asdict
from typing import List

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class User:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha


    def __repr__(self):
        return (f"Usuário(nome={self.nome}, senha={self.senha})")


    def to_dict(self):
        return {
            'nome': self.nome,
            'senha': self.senha,
        }


    @classmethod
    def from_dict(cls, data):
        return cls(
            nome=data['nome'],
            senha=data['senha']
        )


class UserModel:
    FILE_PATH = os.path.join(DATA_DIR, 'users.json')

    def __init__(self):
        self.users = self._load()


    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [User(**item) for item in data]


    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4, ensure_ascii=False)


    def get_all(self):
        return self.users


    def get_by_nome(self, user_nome: int):
        return next((u for u in self.users if u.nome == user_nome), None)


    def add_user(self, user: User):
        self.users.append(user)
        self._save()


    def update_senha(self, user_nome, new_senha):
        self.get_by_nome(user_nome).senha = new_senha
        self._save()


    def delete_user(self, user_nome):
        self.users = [u for u in self.users if u.nome != user_nome]
        self._save()
