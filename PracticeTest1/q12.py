<<<<<<< HEAD
# input 1 2 3 4 5
# output 3.0
=======
# 33.12 LAB: Calculate average
>>>>>>> 1fb6fe752aba8c7b7b0b917c2bea505ca0ade96b

def calc_average(nums):
    numsum = sum(nums) # this finds the sum
    numslength = len(nums) # this gibes us the length of the list
    
    average = numsum / numslength # sum / length -> gives us our value
    return float(average)
    
    
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
<<<<<<< HEAD
    print(calc_average(nums))   # calc_average() should return 3.0
=======
    print(calc_average(nums))   # calc_average() should return 3.0
    
>>>>>>> 1fb6fe752aba8c7b7b0b917c2bea505ca0ade96b
