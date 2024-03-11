frutas=["Piña", "Uva","Cereza", "Guanaba","Pera"]
pop=[4,2,3,1,0]
lista=[]
for i in range(len(frutas)):
    for j in frutas:
        if frutas.index(j)==pop[i]:
            lista.append(j)
print (lista)