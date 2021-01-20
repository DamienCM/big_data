from mrjob.job import MRJob, MRStep


class Mapper(MRJob):
    def filter(self, key, ligne):
        el_ligne = ligne.split(',') #recuperation des elements sur une ligne
        keys = ['O3','NO2','SO2','CO'] # liste des cles
        for i, element in enumerate(el_ligne):
            try:
                if float(element) > 0.5: # on map seulement pour les elements consideres valide 
                    yield (keys[i], 1)
            except ValueError:
                pass
    def reducer(self, key, values): 
        yield(key, sum(values)) #on somme tous les 1



    def steps(self): #definition de l'ordre des etapes du job
        return [MRStep(mapper=self.filter), MRStep(reducer=self.reducer)]


if __name__ == "__main__":
    Mapper.run()