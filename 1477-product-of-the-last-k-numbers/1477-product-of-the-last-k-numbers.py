class ProductOfNumbers:

    def __init__(self):
        self.prefix_prod = [1]

    def add(self, num):
        if num == 0:
            self.prefix_prod = [1]
        else:
            self.prefix_prod.append(self.prefix_prod[-1] * num)

    def getProduct(self, k):
        if k >= len(self.prefix_prod):
            return 0
        return self.prefix_prod[-1] // self.prefix_prod[-k-1]