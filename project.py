class Project:
    def __init__(self, items=0, samples=[]):
        self.samples = samples
        self.items = items

    def iterations(self):
        if len(self.samples) == 0:
            return 0
        done = 0
        count = 0
        while done < self.items:
            done += self.samples[-1]
            count += 1
        return count
