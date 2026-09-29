class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        count=0
        
        while students and count <len(students):
            if students[0]==sandwiches[0]:

                #count+=1
                students.pop(0)
                sandwiches.pop(0)
                count=0
                
            else:
                #students[i]!=sandwiches[i]:
                students.append(students.pop(0))
                count+=1
        return len(students)        

                  