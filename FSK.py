import matplotlib.pylab as plt
import numpy as np


class FSK:
    def __init__(self, message):
        self.signal = message

    def graph(self):
        plt.figure('FSK')

        x = np.linspace(0, 2 * np.pi, 201)
        if self.signal[0] == 1:
            plt.plot(x, (np.sin(2 * x)), 'b')
        else:
            plt.plot(x, np.sin(x), 'b')

        for num in range(1, len(self.signal)):
            y = np.linspace((num * 2) * np.pi, (num * 2 + 2) * np.pi, 201)
            if self.signal[0] == 0:
                if self.signal[num] == 0:
                    plt.plot(y, np.sin(y), 'b')
                else:
                    plt.plot(y, np.sin(2 * y), 'b')
            else:
                if self.signal[num] == 1:
                    plt.plot(y, np.sin(y * 2), 'b')
                else:
                    plt.plot(y, np.sin(y), 'b')


