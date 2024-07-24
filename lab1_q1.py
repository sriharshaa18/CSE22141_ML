def count_pairs(list):
    lent = len(list)
    count = 0
    for i in range(0, lent-1):
        for j in range(i+1, lent):
            if list[i]+list[j] == 10:
                count += 1
    return count
count = count_pairs([2, 7, 4, 1, 3, 6])
print("No of pairs with sum 10 are ", count)