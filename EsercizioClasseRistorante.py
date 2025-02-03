class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome 
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.lista_piatti = []
        self.lista_prezzi = []
        
        
    def descrivi_ristorante(self):
        print(f"Il ristorante {nome} è una {tipo_cucina}")    
        
    def aggiungi_piatto(self, piatto, prezzo):
        scelta_piatto = input("Aggiungi piatto:")
        scelta_prezzo = input("Aggiungi prezzo")
        
        self.lista_piatti.append(scelta_piatto)
        self.lista_prezzi.append(scelta_prezzo)
        print(f"Il Piatto {scelta_piatto} è stato aggiunto con prezzo {scelta_prezzo}€")
        
    def crea_menu(self):
        menu = list(zip(lista_piatti, lista_prezzi))    
    
        
        
    def apri(self):
        self.aperto = True  
        print(f"{self.nome} è ora aperto!")

    def chiudi(self):
        self.aperto = False  
        print(f"{self.nome} è ora chiuso!")    