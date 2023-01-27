import statistics
import numpy as np

class StatData:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def getMean(self, data):
        return round(statistics.mean(data), 4)

    def getMode(self, data):
        return round(statistics.mode(data), 4)

    def getMedian(self, data):
        return round(statistics.median(data), 4)

    def getLowMedian(self, data):
        return round(statistics.median_low(data), 4)

    def getHighMedian(self, data):
        return round(statistics.median_high(data), 4)

    def getVariance(self, data):
        return round(statistics.variance(data, self.getMean(data)), 4)

    def getCorrelation(self, dataX, dataY):
        return round(np.corrcoef(dataX, dataY)[0, 1], 4)

    def calculateB1(self, x, z):
        r = round(self.getCorrelation(self.x, self.z), 4)
        sx = statistics.stdev(x, self.getMean(x))
        sz = statistics.stdev(z, self.getMean(z))
        b1 = r * (sz / sx)
        return round(b1, 4)

    def calculateB0(self, x, z):
        return round(self.getMean(z) - (self.calculateB1(x, z) * self.getMean(x)), 4)

    def calculateRegression(self, x, z):
        bo = self.calculateB0(x, z)
        b1 = self.calculateB1(x, z)
        x = self.getMean(x)
        return bo + b1 * x

    def getPopulationMean(self, x):
        pass