class Bottiglia: #class x creare la classe bottiglia
    def __init__(self, capacita): #init istanzazione di un oggetto
        self.capacita = capacita
        self.quantita = 0
    def __str__(self):
        #return str(self.quantita)+"/"+str(self.capacita)
        #return"{}/{}".format(self.quantita,self.capacita)
        return f"{self.quantita}/{self.capacita}"
    
    def riempi(self, q):
        self.quantita += q
        if self.quantita > self.capacita:
            self.quantita = self.capacita
        
    def svuota(self, q):
        self.quantita -= q
        if self.quantita < 0:
            self.quantita = 0

class BottigliaconTappo(Bottiglia): #eredita sottoclasse bottiglia
    def __init__(self, capacita):
        super().__init__(capacita) #super chiama la funzione costruttore di bottiglia
        self.aperta = True
    def apri(self):
        self.aperta = True
    def chiudi(self):
        self.chiudi = False
    def __str__(self):
        return super().__str__() + f" aperta: {self.aperta}"
    
    def riempi(self, q):
        if self.aperta:
        super().riempi(q)