import json
import os
from models.pet import PetModel, Pet

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "pets.json")
DATA_PATH = os.path.abspath(DATA_PATH)



class PetService:
    def __init__(self):
        self.pets = self.load_pets()

    # ---------------------------
    #  Carregar e salvar JSON
    # ---------------------------
    def load_pets(self):
        if not os.path.exists(DATA_PATH):
            return []

        try:
            with open(DATA_PATH, "r", encoding="utf8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def save_pets(self):
        with open(DATA_PATH, "w", encoding="utf8") as f:
            json.dump(self.pets, f, indent=4)

    # ---------------------------
    #  Buscar pet por usuário
    # ---------------------------
    def get_pet_by_user(self, user_id):
        self.pets = self.load_pets()
        for pet in self.pets:
            if pet["user_id"] == user_id:
                return pet
        return None

    # ---------------------------
    #  Criar pet ligado ao usuário
    # ---------------------------
    def create_pet_for_user(self, user_id, nome):
        existing = self.get_pet_by_user(user_id)
        if existing:
            return existing

        pet_model = Pet(nome)

        pet_data = {
            "id": len(self.pets) + 1,
            "user_id": user_id,
            "nome": pet_model.nome,
            "fome": pet_model.fome,
            "felicidade": pet_model.felicidade,
            "energia": pet_model.energia,
            "sujeira": pet_model.sujeira,
            "qi": pet_model.qi,
            "vida": pet_model.vida,
            "vidamax": pet_model.vidamax
        }

        self.pets.append(pet_data)
        self.save_pets()

        return pet_data

    # ---------------------------
    #  Atualizar pet no JSON
    # ---------------------------
    def update_pet(self, pet_dict):
        for i, p in enumerate(self.pets):
            if p["id"] == pet_dict["id"]:
                self.pets[i] = pet_dict
                self.save_pets()
                return

    # ---------------------------
    #  Ações usando o MODEL
    # ---------------------------
    def load_pet_model(self, pet_dict):
        """Converte o dicionário salvo no JSON em um objeto Pet."""
        pet = Pet(pet_dict["nome"])

        print("A)", pet)
        print("B)", pet_dict)

        pet.fome = pet_dict["fome"]
        pet.felicidade = pet_dict["felicidade"]
        pet.energia = pet_dict["energia"]
        pet.sujeira = pet_dict["sujeira"]
        pet.qi = pet_dict["qi"]
        pet.vida = pet_dict["vida"]
        pet.vidamax = pet_dict["vidamax"]
        return pet

    def apply_and_save(self, user_id, action):
        pet_dict = self.get_pet_by_user(user_id)
        if not pet_dict:
            return None

        pet = self.load_pet_model(pet_dict)

        # Executa ação
        action(pet)

        # Atualiza dicionário com novos valores
        pet_dict["nome"] = pet.nome
        pet_dict["fome"] = pet.fome
        pet_dict["felicidade"] = pet.felicidade
        pet_dict["energia"] = pet.energia
        pet_dict["sujeira"] = pet.sujeira
        pet_dict["qi"] = pet.qi
        pet_dict["vida"] = pet.vida
        pet_dict["vidamax"] = pet.vidamax

        self.update_pet(pet_dict)
        return pet_dict

    def comer(self, user_id):
        return self.apply_and_save(user_id, lambda p: p.comer())

    def brincar(self, user_id):
        return self.apply_and_save(user_id, lambda p: p.brincar())

    def dormir(self, user_id):
        return self.apply_and_save(user_id, lambda p: p.dormir())
    
    def banhar(self, user_id):
        return self.apply_and_save(user_id, lambda p: p.banhar())

    def treinar(self, user_id):
        return self.apply_and_save(user_id, lambda p: p.treinar())
    
    def curar(self, user_id):
        return self.apply_and_save(user_id, lambda p: p.curar())
