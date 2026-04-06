class peixe:
    def __init__(self, nome, valor, dificuldade, peso):
        self.nome = nome
        self.valor = valor
        self.dificuldade = dificuldade
        self.peso = peso
        self.proximo = None

class Mochila:
    def __init__(self, capacidade):
        self.primeiro = None
        self.capacidade = capacidade
        self.quantidade_atual = 0
        self.tamanho_hash = 15 
        self.hash_peixes = [None] * self.tamanho_hash

    def func_hash(self, nome):
        soma = 0
        for letra in nome:
            soma += ord(letra)
        return soma % self.tamanho_hash

    def inserir_peixe(self, nome, valor, dificuldade, peso):
        if self.quantidade_atual >= self.capacidade:
            print("mochila cheia!\nVenda os seus peixes ou atualize a sua mochila no Willy")
            return

        novo = peixe(nome, valor, dificuldade, peso)

        indice = self.func_hash(nome)
        if self.hash_peixes[indice] is None:
            self.hash_peixes[indice] = novo
        else:
            atual_h = self.hash_peixes[indice]
            while atual_h.proximo is not None:
                atual_h = atual_h.proximo
            atual_h.proximo = novo

        if self.primeiro is None:
            self.primeiro = novo
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo

        self.quantidade_atual += 1
        print("Você pegou o peixe!!")

class loja:
    def __init__(self, tamanho):
        

def minigame():
    # A fazer

def main():
    # A fazer


MUNDOS = {
    "Rio": {"nomes": ["Lambari", "Truta", "Piau", "Piranha", "Dourado"], "valor_min": 10, "peso_max": 15},
    "Mar": {"nomes": ["Robalo", "Sardinha", "Atum", "Garoupa", "Marlin"], "valor_min": 50, "peso_max": 200},
    "Abismo": {"nomes": ["Peixe-Lanterna", "Lula-Gigante", "Peixe-Gota", "Dragão-Negro"], "valor_min": 200, "peso_max": 500},
    "Lagoa Gelada": {"nomes": ["Salmão-do-Ártico", "Peixe-Gelo", "Truta-Prateada"], "valor_min": 80, "peso_max": 30},
    "Pântano": {"nomes": ["Bagre", "Jacundá", "Peixe-Cobra", "Traíra"], "valor_min": 30, "peso_max": 60}
}
