from mrjob.job import MRJob, MRStep
import time

class Mapper(MRJob):

    def mapper(self, key, ligne):
        el_ligne = ligne.split(',') #recuperation des differentes mesures d'une ligne
        keys = ['O3', 'NO2', 'SO2', 'CO'] #cles valeurs des colonnes 

        for i, element in enumerate(el_ligne):
            try:
                temp = float(element)
                if temp > 0.5 :  # test de si la mersure est valide
                    yield (keys[i], (temp, 1))

            except ValueError: #traitement du cas ou une ligne n'est pas lisible (header/footer/erreur d'ecriture)
                pass


    def reducer(self, key, values):
        min_val = next(values) #valeurs initiale
        max_val = min_val      #valeur initiale
        count = 0              #valeur initiale
        avg = 0                #valeur initiale
        for element in values:
            avg += element[0]
            min_val = min(element, min_val) #compare la valeur actuelle avec la valeur iteree  
            max_val = max(element, max_val) #compare la valeur actuelle avec la valeur iteree 
            count += 1
        yield key, (min_val[0], max_val[0], count, avg/count) #retourne pour chaque cle : min, max, nombre de mesure valide, moyenne des mesures valide


    def steps(self):
        return [MRStep(mapper=self.mapper, reducer=self.reducer)]


if __name__ == "__main__":
    Mapper.run()
