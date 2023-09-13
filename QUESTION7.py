#QUESTION 7: GIVEN AN ARRAY OF 1S AND 0S WHICH HASALL 1S FIRST FOLLOWED BY 0S. WRIET A FUNCTION CALLED COUNTZEROS
#WHICH RETURNS NUMBER OF ZERO IN ARRAY.

import math
def countzero(customList):
    left=0
    right=len(customList)-1
    while left<=right:
        middle=math.floor((left+right)/2)
        if customList[middle]==1:
            left=middle+1
        else:
            rigght=middle-1
    return len(customList)-left         #minus 1s           
