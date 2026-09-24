class MyHashSet(object):

    def __init__(self):
        self.myset = [False] * 1000001

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.myset[key]=True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.myset[key]=False

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.myset[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna