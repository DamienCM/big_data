from mrjob.job import MRJob, MRStep
import time

# On cherche ici a calculer le nombre d'occurence ou sur une ligne il y a des combinaisons
# telles que la somme de 2 facteurs est superieure a 0.5
# on renverra le nombre de combinaison qui donne un resultat > 0.5 pour chaque element
#  ex : 
# C02 : 40 (sur les lignes il y a 40 combinaisons avec les autres colonne de CO2 qui donne un resultat superieur a 0.5)
# SO : 200
# etc

# image de ce que l'on cherche a faire :
# https://puu.sh/H8Gyg/fccf9b3f1b.png

class Mapper(MRJob):

    def filter(self, key, ligne):
        els_ligne = ligne.split(',') #recuperation des differentes mesures d'une ligne
        keys = ['O3', 'NO2', 'SO2', 'CO'] #cles valeurs des colonnes 

        try : 
            valeurs = [float(v) for v in els_ligne] # convertit [floats] <-- [strings]
            counts = []
            for i1,v1 in enumerate(valeurs): #calcule le nombre de combinaison presente sur la ligne pour la i eme valeur
                count = 0 #nombre de combinaison init= 0
                for i2,v2 in enumerate(valeurs): #compare avec les autres valeurs de la ligne
                    if (v1 + v2) > 0.5 and i1 != i2 :
                        count+=1
                counts.append(count)
            yield "Combinaisons", counts #renvoie le nombre de combinaison 

        except ValueError:
            pass

    def reducer(self, key, values):
        sums = next(values) #initialisation de la somme
        for line in values: 
            for i in range(len(sums)): #parcoure les lignes
                sums[i]+=line[i]
        yield key, sums #retourne pour chaque cle le nombre de combianison


    def steps(self):
        return [MRStep(mapper=self.filter),MRStep(reducer=self.reducer)]


if __name__ == "__main__":
    t0 = time.time()
    Mapper.run()
    print(f'Program executed in {time.time() - t0} seconds')