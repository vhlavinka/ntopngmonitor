import pickle
from pprint import pprint


# finding max value
def max(list):
    max = 0
    for num in list:
        if num >= max:
            max = num
    return max


# min value
def min(list):
    min = 9999999
    for num in list:
        if num <= min:
            min = num
    return min


# average value
def avg(list):
    sum = 0
    count = 0
    for num in list:
        sum = sum + num
        count = count + 1
    avg = sum / count
    return avg


def main():
    with open("CSC495data.json", "rb") as fp:
        list = pickle.load(fp)

    minimum = min(list)
    maximum = max(list)
    average = avg(list)

    print("Data Dump: ")
    pprint(list)

    print("\nMin:" + str(minimum))
    print("Max: " + str(maximum))
    print("Average: " + str(average))


main()
