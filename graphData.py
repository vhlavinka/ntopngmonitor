import matplotlib.pylab as plt
import pickle

def main():
    #unpickle the list
    with open("CSC495data.json", "rb") as fp:
        list = pickle.load(fp)

    #swaplist = {val: key for (key, val) in list.items()}

    #change x-axis
    start = 0
    for num in list:
        start = start + 10
        list[num] = start
    print (list)

    swaplist = {val:key for (key, val) in list.items()}
    plt.plot(*zip(*sorted(swaplist.items())))
    plt.ylabel('throughput')
    plt.xlabel('time (in seconds)')
    plt.ylim(100000, 400000)
    plt.show()


main()