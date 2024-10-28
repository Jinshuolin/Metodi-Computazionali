semain = [ "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica", "Lunedì"]
ottobre = semain*4
ottobre.append ("Martedì")
ottobre.append ("Mercoledì")
ottobre.append ("Giovedì")
rel = {1 : "Martedì"}
for k in range(1,31):
    rel[k+1] = ottobre[k]

#for k in rel:
 #   print ( "Giorno", k, " ", rel[k])
print (rel)
    
    
