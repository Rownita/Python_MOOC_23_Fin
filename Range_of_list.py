"""
Please write a function named range_of_list, which takes a list of integers as an argument.
The function returns the difference between the smallest and the largest value in the list.
"""
# Write your solution here

def range_of_list(my_list):
    max_1= max(my_list)
    min_1 = min(my_list)
    range = max_1 - min_1
    return range
  
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)
