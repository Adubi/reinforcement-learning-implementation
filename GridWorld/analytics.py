import os
import matplotlib.pyplot as plt
from collections import Counter


def plot_aggregate_rewards_q_learning(filename: str):
    """
    reads in the file of rewards and plots them
    """

    names = []
    r = 0
    if filename in os.listdir():
        pass
    else:
        raise FileNotFoundError(f"No such file: {filename}")

    f = open(filename, "r")
    for v in f.readlines():
        names.extend(v.replace("\n", "").split(","))
        r += 1

    
    c = Counter(names)
    plt.bar(x=list(c.keys()), height=list(c.values()))
    plt.title(f"Aggregrate of rewards from {r} games")
    plt.savefig("aggregate_rewards_q.png")
    plt.show()
    


def plot_aggregate_rewards_v_learning(filename: str):
    """
    reads in the file of rewards and plots them
    """

    names = []
    r = 0

    f = open(filename, "r")
    for v in f.readlines():
        names.extend(v.replace("\n", "").split(","))
        r += 1
    
    c = Counter(names)
    plt.bar(x=list(c.keys()), height=list(c.values()))
    plt.title(f"Aggregrate of rewards from {r} games")
    plt.savefig("aggregate_rewards_v.png")
    plt.show()


if __name__ == "__main__":
    plot_aggregate_rewards_v_learning("rewards_v.txt")
    plot_aggregate_rewards_q_learning("rewards_q.txt")