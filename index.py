from bottiglia import Bottiglia;from bottiglia import BottigliaconTappo

b = Bottiglia(500)
print(b.capacita)
print(b)
b.riempi(200)
print(b)
b.riempi(1500) 
print(b)
b.svuota(50) 
print(b)
b.svuota(600) 
print(b)

b2 = BottigliaconTappo
print(b2)
b2.chiudi()
print(b2)
b2.riempi(1500)
print(b2)