from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #calculate distance
        distances=[]
        for num in arr:
            distance=abs(num - x)
            distances.append((distance,num))

        distances.sort()
        #choosing k element from distances
        answer=[]
        for i in range(k):
            answer.append(distances[i][1])

        answer.sort()
        return answer
        