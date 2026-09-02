class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1="".join(sorted(s1)) #Sort s1
        
        window_size=len(s1) #store s1 in a variable
        for left in range(len(s2) - window_size + 1):
            window = s2[left:left + window_size]
            sorted_window="".join(sorted(window))
            if sorted_window == sorted_s1:
                return True
        return False