# This function counts the number of pairs in a list whose sum equals 10
def count_pairs(list):
    # Finding the length of the list
    lent = len(list)
    count = 0

    # Iterate through each element in the list
    for i in range(0, lent - 1):
        # For each element, check with the remaining elements in the list
        for j in range(i + 1, lent):
            # If the sum of the pair equals 10, increment the count
            if list[i] + list[j] == 10:
                count += 1

    # Return the total count of pairs whose sum is 10
    return count


# Call the function with a sample list and print the result
count = count_pairs([2, 7, 4, 1, 3, 6])
print("No of pairs with sum 10 are ", count)
