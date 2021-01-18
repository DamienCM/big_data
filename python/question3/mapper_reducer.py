from mrjob.job import MRJob, MRStep
import time

maximum = 0
minimum = 0

#keys_val = ['O3_val', 'NO2_val', 'SO2_val', 'CO_val']

class Mapper(MRJob):
    def filter(self, key, ligne):
        el_ligne = ligne.split(',')
        keys = ['O3', 'NO2', 'SO2', 'CO']
        for i, element in enumerate(el_ligne):
            try:
                temp = float(element)
                if temp > 0.5:
                    yield (keys[i], (temp, 1))
                    #yield (keys_val[i], temp)
            except ValueError:
                pass
    def reducer(self, key, values):
        min_val = next(values)
        max_val = min_val
        count = 0
        avg = 0
        for element in values:
            avg += element[0]
            min_val = min(element, min_val)
            max_val = max(element, max_val)
            count += 1
        yield key, (min_val[0], max_val[0], count, avg/count)



    def steps(self):
        return [MRStep(mapper=self.filter,reducer=self.reducer)]


if __name__ == "__main__":
    t0 = time.time()
    Mapper.run()
    print(f'Program executed in {time.time() - t0} seconds')