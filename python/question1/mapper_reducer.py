from mrjob.job import MRJob, MRStep


class Mapper(MRJob):
    def mapper(self, key, ligne):
        el_ligne = ligne.split(',')#recuperation des differentes mesures d'une ligne
        keys = ['O3','NO2','SO2','CO'] #cles valeurs des colonnes
        for i, element in enumerate(el_ligne):
            try:
                if float(element) > 0.5:# test de si la mersure est valide
                    yield (keys[i], 1)
            except ValueError:
                pass
    def reducer(self, key, values):#traitement du cas ou une ligne n'est pas lisible (header/footer/erreur d'ecriture)
        yield(key, sum(values)) #On calcule la somme des mesures valide



    def steps(self):
        return [MRStep(mapper=self.mapper), MRStep(reducer=self.reducer)]


if __name__ == "__main__":
    Mapper.run()