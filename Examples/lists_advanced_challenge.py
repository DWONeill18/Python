# List Advanced Challenges

# Every Three N umbers

def every_three_nums(start):
    if start > 100:
        return []
    else:
        return list(range(start, 101, 3))
    
#Uncomment the line below when your function is done
print(every_three_nums(91))

# Remove middle

def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# More Frequent Item

def more_frequent_item(lst, item1, item2):
  if lst.count(item1) > lst.count(item2):
    return item1
  elif lst.count(item2) > lst.count(item1):
    return item2
  else:
    return item1
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# Double Index

def double_index(lst, index):
  lst[index] = lst[index] * 2
  return lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))


# Middle Item

def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))