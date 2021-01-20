from mrjob.job import MRJob, MRStep


class Mapper(MRJob):
    def mapper(self, key, ligne):
        el_ligne = ligne.split(',')
        keys = ['O3','NO2','SO2','CO']
        for i, element in enumerate(el_ligne):
            try:
                if float(element) > 0.5:
                    yield (keys[i], 1)
            except ValueError:
                pass

    def reducer(self, key, values):
        yield(key, sum(values))



    def steps(self):
        return [MRStep(mapper=self.mapper, reducer=self.reducer)]


if __name__ == "__main__":
    Mapper.run()