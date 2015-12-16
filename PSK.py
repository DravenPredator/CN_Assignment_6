import matplotlib.pylab as plt
import numpy as np


class PSK:
    def __init__(self, message):
        self.signal = message

    def graph(self):
        plt.figure('PSK')

        x = np.linspace(0, 2 * np.pi, 201)
        if self.signal[0] == 1:
            plt.plot(x, np.cos(x + 1.57), 'r')
        else:
            plt.plot(x, np.sin(x), 'r')

        for num in range(1, len(self.signal)):
            y = np.linspace((num * 2) * np.pi, (num * 2 + 2) * np.pi, 201)
            if self.signal[0] == 0:
                if self.signal[num] == 0:
                    plt.plot(y, (np.sin(y)), 'r')
                else:
                    plt.plot(y, (np.cos(y + 1.57)), 'r')
            else:
                if self.signal[num] == 0:
                    plt.plot(y, (np.sin(y)))
                else:
                    plt.plot(y, (np.cos(y + 1.57)), 'r')

