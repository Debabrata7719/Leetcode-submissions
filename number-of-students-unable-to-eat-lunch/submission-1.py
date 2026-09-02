from typing import List
from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        students = deque(students)
        sandwiches = deque(sandwiches)
        count=0
        while len(students) > 0:
        
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                count = 0  #If student choose sandwich count reset
            else:
                students.append(students.popleft())
                count +=1 #If student go to the back of the queue count for break the loop until it was a infinite loop
        
            if count == len(students):
                break

        return len(students)

