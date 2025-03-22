class Bottiglia:
    def __init__(self, capacità):                               #il costruttore (__init__) è il metodo che serve per creare un oggetto #"self" è un parametro obbligatorio per i metodi dell'oggetto
        self.quantità = 0                                       #valore fisso
        self.capacità = capacità                                #valore passato
    
    def __str__(self):                                          #definisce come far diventare l'oggetto una stringa
        return str(self.quantità)+"/"+str(self.capacità) 
        return "{}/{}",format(self.quantità,self.capacità)
        return f"{self.quantità}/{self.capacità}"
    
    def riempi(self,q):
        self.quantità += q
        if self.quantità > self.capacità:                       #fa in modo che anche riempendo di più, ti dia un massimo di 500
            self.quantità = self.capacità

    def svuota(self,q):
        self.quantità -= q
        if self.quantità < 0:                                   #fa in modo che anche svuotando di meno, non ti dia meno di 0
            self.quantità = 0

class BottigliaConTappo(Bottiglia):                             #Abbiamo creato una sottoclasse che sia una copia della classe madre
    def __init__(self, capacità):
        super().__init__(capacità)                              #"super" serve a chiamare la classe madre
        self.aperta = True
    def apri(self):
        self.aperta = True
        print("La bottiglia è aperta")
    def chiudi(self):
        self.aperta = False
        print("La bottiglia è chiusa")
    def __str__(self):
        return super().__str__() + f" aperta: {self.aperta}"
    def riempi(self, q):                                        #la funziona doveva essere riscritta per non andare in overide
        if self.aperta: 
            super().riempi(q)
    