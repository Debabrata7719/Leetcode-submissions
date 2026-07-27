class StockSpanner:

    def __init__(self):
        self.values=[]

    def next(self, price: int) -> int:
        self.values.append(price)
        i = len(self.values) - 1
        j = i
        count = 0
        while j >= 0:
            if self.values[j] <= self.values[i]:
                count += 1
                j -= 1
            else:
                break

        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)