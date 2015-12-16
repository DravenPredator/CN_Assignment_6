import matplotlib.pyplot as plt
import numpy as np
from ASK import ASK
from FSK import FSK
from PSK import PSK

'''
    Change signal to whatever you want as along as it contains 1's and 0's
'''
signal = [0, 1, 1, 0, 1, 1, 1, 0]

def Carrier():
    plt.figure('Carrier Signal')

    x = np.linspace(0, 18 * np.pi, 201)
    plt.plot(x, np.sin(x))


def OrginSignal():
    plt.figure('Original Digital Signal')
    y = np.repeat(signal, 2, axis=None)
    t = np.arange(len(y))

    plt.step(t, y + 2, 'r', linewidth=2)


def main():
    psk = PSK(signal)
    fsk = FSK(signal)
    ask = ASK(signal)

    psk.graph()
    fsk.graph()
    ask.graph()

    Carrier()

    OrginSignal()

    plt.show()


if __name__ == '__main__':
    main()
