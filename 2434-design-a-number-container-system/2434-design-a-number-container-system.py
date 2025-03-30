class NumberContainers:
    def __init__(self):
        self.index_to_number = {}
        self.number_to_indices = defaultdict(SortedSet)

    def change(self, index, number):
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            self.number_to_indices[old_number].discard(index)
            if not self.number_to_indices[old_number]:
                del self.number_to_indices[old_number]

        self.index_to_number[index] = number
        self.number_to_indices[number].add(index)

    def find(self, number):
        return next(iter(self.number_to_indices[number]), -1)

# Example usage:
# obj = NumberContainers()
# obj.change(index, number)
# param_2 = obj.find(number)