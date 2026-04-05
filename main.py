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
    
    def inserir_peixe(self,nome, valor, dificuldade, peso):
        novo = peixe(nome, valor, dificuldade, peso)

        if self.quantidade_atual >= self.capacidade:
                print("mochila cheia!\nVenda os seus peixes ou atualize a sua mochila no Willy")
        elif self.primeiro is None:
            self.primeiro = novo
            self.quantidade_atual += 1
        else:
            atual = self. primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            
            atual.proximo = novo
            self.quantidade_atual += 1
                        
            print("Você pegou o peixe!!")


        def esvaziar_e_vender(self):
                ganho_total = 0
                atual = self.primeiro

                while atual is not None:
                    ganho_total += atual.valor
                    atual = atual.proximo

                
                self.primeiro = None
                self.quantidade_atual = 0
                return ganho_total
    
    def listar_peixes(self):
        atual = self.primeiro
        while atual is not None:
            print(f"{atual.nome}, {atual.valor}, {atual.dificuldade}, {atual.peso} KG")

            atual = atual.proximo
    
class loja:
     def __init__(self,tamanho):
          self.tamanho = None
          
          

def mingame():
    

def main():




MUNDOS = {
"Rio": {
    "nomes": ["Lambari", "Truta", "Piau", "Piranha", "Dourado"], 
    "valor_min": 10, "peso_max": 15
},
"Mar": {
    "nomes": ["Robalo", "Sardinha", "Atum", "Garoupa", "Marlin"], 
    "valor_min": 50, "peso_max": 200
},
"Abismo": {
    "nomes": ["Peixe-Lanterna", "Lula-Gigante", "Peixe-Gota", "Dragão-Negro"], 
    "valor_min": 200, "peso_max": 500
},
"Lagoa Gelada": {
    "nomes": ["Salmão-do-Ártico", "Peixe-Gelo", "Truta-Prateada"], 
    "valor_min": 80, "peso_max": 30
},
"Pântano": {
    "nomes": ["Bagre", "Jacundá", "Peixe-Cobra", "Traíra"], 
    "valor_min": 30, "peso_max": 60
}
}