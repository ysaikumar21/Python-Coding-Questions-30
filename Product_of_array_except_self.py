def product_except_self(nums):
    n=len(nums)
    res=[1]*n
    #calculation on preffix 
    for i in range(1,n):
        res[i]=res[i-1]*nums[i-1]
    suffix_product=1
    for i in range(n-1,-1,-1):
        res[i]*=suffix_product
        suffix_product*=nums[i]
    return res
nums=[1,2,3,4]
result=product_except_self(nums)
print(result)
