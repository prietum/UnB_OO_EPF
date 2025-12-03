import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class User:
    def __init__(self, user_id, nome, senha):
        self.id = user_id
        self.nome = nome
        self.senha = senha

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'senha': self.senha,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            user_id=data.get('id'),
            nome=data.get('nome'),
            senha=data.get('senha'),
        )

class UserModel:
    FILE_PATH = os.path.join(DATA_DIR, 'users.json')

    def __init__(self):
        self.users = self._load()
        self._update_next_id()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # ensure every item has an 'id' — if missing, assign sequential ids
            # find current max id among items that already have one
            existing_ids = [item.get('id') for item in data if isinstance(item.get('id'), int)]
            current_max = max(existing_ids) if existing_ids else 0
            next_id = current_max + 1
            for item in data:
                if 'id' not in item or not isinstance(item.get('id'), int):
                    item['id'] = next_id
                    next_id += 1
            return [User.from_dict(item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4, ensure_ascii=False)

    def _update_next_id(self):
        if not self.users:
            self.next_id = 1
        else:
            self.next_id = max(u.id for u in self.users) + 1

    def get_all(self):
        return self.users

    def get_by_nome(self, nome):
        return next((u for u in self.users if u.nome == nome), None)

    def get_by_id(self, user_id):
        return next((u for u in self.users if u.id == user_id), None)

    def add_user(self, user: User):
        self.users.append(user)
        self._save()
        self.next_id += 1

    def create_user(self, nome, senha):
        user = User(self.next_id, nome, senha)
        self.add_user(user)
        return user

    def update_senha(self, user_id, nova_senha):
        user = self.get_by_id(user_id)
        if user:
            user.senha = nova_senha
            self._save()

    def delete_user(self, user_id):
        self.users = [u for u in self.users if u.id != user_id]
        self._save()
