def Max_area(height):
#Finds the maximum area of a container formed by two vertical lines.
    left,right=0,len(height)-1
    max_area=0
    while left<right:
        area=(right-left)*min(height[left],height[right])
        max_area=max(max_area,area)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return max_area

height=[1, 8, 6, 2, 5, 4, 8, 3, 7]
result=Max_area(height)
print(result)