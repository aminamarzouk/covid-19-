import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Graph:
    def __init__(self, x, y, z, botRightFrame):
        self.x = x
        self.y = y
        self.z = z
        self.botRightFrame = botRightFrame
        self.FIG_SIZE_X = 10
        self.FIG_SIZE_Y = 6

    def clearScreen(self, botRightFrame):
        for widget in botRightFrame.winfo_children():
            widget.destroy()

    def drawCanvas(self, fig):
        self.clearScreen(self.botRightFrame)
        canvas = FigureCanvasTkAgg(fig, master=self.botRightFrame)
        canvas.get_tk_widget().pack()
        canvas.draw()

    def viewGraph(self, y, x):
        fig = Figure(figsize=(self.FIG_SIZE_X, self.FIG_SIZE_Y))
        a = fig.add_subplot(111)
        a.set_title("Graph of Reported Cases")
        a.plot(y, x, color='red')
        self.drawCanvas(fig)

    def viewHist(self, x):
        fig = Figure(figsize=(self.FIG_SIZE_X, self.FIG_SIZE_Y))
        a = fig.add_subplot(111)
        a.set_title("Histogram of Reported Cases")
        a.hist(x, color='red')
        self.drawCanvas(fig)

    def viewPie(self, x, y):
        myExplode = [0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        fig = Figure(figsize=(self.FIG_SIZE_X, self.FIG_SIZE_Y))
        a = fig.add_subplot(111)
        a.set_title("Pie Chart of Reported Cases")
        a.pie(x, labels=y, explode=myExplode)
        self.drawCanvas(fig)

    def viewBar(self, y, x):
        fig = Figure(figsize=(self.FIG_SIZE_X, self.FIG_SIZE_Y))
        a = fig.add_subplot(111)
        a.set_title("Bar Chart of Reported Cases")
        a.bar(y, x, color="red")
        self.drawCanvas(fig)

    def viewDotPlot(self, y, x):
        fig = Figure(figsize=(self.FIG_SIZE_X, self.FIG_SIZE_Y))
        a = fig.add_subplot(111)
        a.set_title("Dot Plot of Reported Cases and Deaths")
        a.scatter(y, x, color="red")
        self.drawCanvas(fig)

    def viewBoxPlot(self, x):
        fig = Figure(figsize=(self.FIG_SIZE_X, self.FIG_SIZE_Y))
        a = fig.add_subplot(111)
        a.set_title("Box Plot of Reported Cases")
        a.boxplot(x)
        self.drawCanvas(fig)
