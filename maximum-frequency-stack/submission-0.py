class FreqStack(object):

    def __init__(self):
        self.freq = {}       # value -> frequency
        self.group = {}      # frequency -> stack of values
        self.maxfreq = 0

    def push(self, val):
        # Increase frequency
        self.freq[val] = self.freq.get(val, 0) + 1

        f = self.freq[val]

        # Create stack for this frequency if needed
        if f not in self.group:
            self.group[f] = []

        # Put val into the frequency stack
        self.group[f].append(val)

        # Update maximum frequency
        self.maxfreq = max(self.maxfreq, f)

    def pop(self):
        # Get most recently pushed value
        val = self.group[self.maxfreq].pop()

        # Decrease its frequency
        self.freq[val] -= 1

        # If this frequency stack becomes empty,
        # decrease max frequency
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return val