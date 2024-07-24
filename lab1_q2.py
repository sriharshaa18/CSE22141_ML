def inp():
    list = []
    r = int(input("enter the size:"))
    j = 1
    while j <= r:
        i = input("Enter the number:")
        list.append(i)
        j = j + 1

    return list

def min(list):
    s = list[0]
    for i in list:
        if i < s:
            s = i
    return s

def max(list):
    lar = list[0]
    for i in list:
        if i > lar:
            lar = i
    return lar

def Range(list):
    s = int(min(list))
    l = int(max(list))
    r = l - s
    if len(list) == 3:
        print("Range determination not possible")
    print(f"range is {r}:({l}-{s} )")

list = inp()
Range(list)