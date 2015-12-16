import matplotlib.pylab as plt
import numpy as np


class ASK:
    def __init__(self, message):
        self.signal = message

    def graph(self):
        plt.figure('ASK')

        x = np.linspace(0, 2 * np.pi, 201)
        if self.signal[0] == 1:
            plt.plot(x, (2 * np.sin(x)), 'g')
        else:
            plt.plot(x, np.sin(x), 'g')

        for num in range(1, len(self.signal)):
            y = np.linspace((num * 2) * np.pi, (num * 2 + 2) * np.pi, 201)
            if self.signal[0] == 0:
                if self.signal[num] == 0:
                    plt.plot(y, np.sin(y), 'g')
                else:
                    plt.plot(y, (2 * np.sin(y)), 'g')
            else:
                if self.signal[num] == 1:
                    plt.plot(y, (2 * np.sin(y)), 'g')
                else:
                    plt.plot(y, np.sin(y), 'g')

