import pandas as pd
import matplotlib.pyplot as plt
import StatData
import Graph
import numpy as np
import statistics
import openpyxl
from tkinter import *
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class Main:

    # Main Data

    # Constructor
    def __init__(self, window, topFrame, botFrame, botRightFrame, botLeftFrame):
        self.window = window
        self.topFrame = topFrame
        self.botFrame = botFrame
        self.botRightFrame = botRightFrame
        self.botLeftFrame = botLeftFrame
        var = pd.read_excel(r'D:\Ahmed\Own Projects\python\condatest\analysis.xlsx')
        self.x = list(var['reported cases'])
        self.y = list(var['country'])
        self.z = list(var['deaths'])
        self.st = StatData.StatData(self.x, self.y, self.z)
        self.gr = Graph.Graph(self.x, self.y, self.z, botRightFrame)
        self.main(self.x, self.y, self.z, self.gr, self.st)

    # Functions
    def reduceData(self, x):
        pass

    def displayData(self):
        plt.figure(figsize=(10, 10))
        plt.style.use('ggplot')

    def addButtonsToTopFrame(self, topFrame):
        graphBtn = Button(topFrame, text="Graph Reported", command=lambda :self.gr.viewGraph(self.y, self.x), width=14, height=10, activebackground="#000", borderwidth=3, relief="ridge", activeforeground="#ffffff")
        graphBtn.pack(side=LEFT, pady=10)

        histBtn = Button(topFrame, text="Histogram Reported", command=lambda :self.gr.viewHist(self.x), width=14, height=10, activebackground="#000", borderwidth=3, relief="ridge", activeforeground="#ffffff")
        histBtn.pack(side=LEFT, pady=10)

        pieBtn = Button(topFrame, text="Pie Chart Reported", command=lambda :self.gr.viewPie(self.x, self.y), width=14, height=10, activebackground="#000", borderwidth=3, relief="ridge", activeforeground="#ffffff")
        pieBtn.pack(side=LEFT, pady=10)

        barBtn = Button(topFrame, text="Bar Chart Reported", command=lambda :self.gr.viewBar(self.y, self.x), width=14, height=10, activebackground="#000", borderwidth=3, relief="ridge", activeforeground="#ffffff")
        barBtn.pack(side=LEFT, pady=10)

        boxPlotBtn = Button(topFrame, text="Box Plot Reported", command=lambda: self.gr.viewBoxPlot(self.x), width=14, height=10, activebackground="#000", borderwidth=3, relief="ridge", activeforeground="#ffffff")
        boxPlotBtn.pack(side=LEFT, pady=10)

        graphBtn = Button(topFrame, text="Graph Deaths", command=lambda :self.gr.viewGraph(self.y, self.z), width=14, height=10, activebackground="#000", borderwidth=3, relief="ridge", activeforeground="#ffffff")
        graphBtn.pack(side=LEFT, pady=10)

        histBtn = Button(topFrame, text="Histogram Deaths", command=lambda :self.gr.viewHist(self.z), width=14, height=10, activebackground="#000", borderwidth=3, relief="ridge", activeforeground="#ffffff")
        histBtn.pack(side=LEFT, pady=10)

        pieBtn = Button(topFrame, text="Pie Chart Deaths", command=lambda :self.gr.viewPie(self.z, self.y), width=14, height=10, activebackground="#000", borderwidth=3, relief="ridge", activeforeground="#ffffff")
        pieBtn.pack(side=LEFT, pady=10)

        barBtn = Button(topFrame, text="Bar Chart Deaths", command=lambda :self.gr.viewBar(self.y, self.z), width=14, height=10, activebackground="#000", borderwidth=3, relief="ridge", activeforeground="#ffffff")
        barBtn.pack(side=LEFT, pady=10)

        dotPlotBtn = Button(topFrame, text="Dot Plot", command=lambda: self.gr.viewDotPlot(self.z, self.x), width=14, height=10, activebackground="#000", borderwidth=3, relief="ridge", activeforeground="#ffffff")
        dotPlotBtn.pack(side=LEFT, pady=10)

        boxPlotBtn = Button(topFrame, text="Box Plot Deaths", command=lambda: self.gr.viewBoxPlot(self.z), width=14, height=10, activebackground="#000", borderwidth=3, relief="ridge", activeforeground="#ffffff")
        boxPlotBtn.pack(side=LEFT, pady=10)

        clearBtn = Button(topFrame, text="Clear", command=lambda: self.gr.clearScreen(self.botRightFrame), width=14, height=10, activebackground="#000", borderwidth=3, relief="ridge", activeforeground="#ffffff", fg="red")
        clearBtn.pack(side=LEFT, pady=10)

    def addLabelsToBottomLeftFrame(self, botLeftFrame):

        # Reported Cases
        reportedLabelFrame = LabelFrame(botLeftFrame, text="Reported Cases Stats", height= f"{botLeftFrame.winfo_screenheight() * (1 / 4)}", width= f"{botLeftFrame.winfo_screenwidth()}")
        reportedLabelFrame.pack_propagate(False)
        reportedLabelFrame.pack()

        meanLabel = Label(reportedLabelFrame, text=f"Mean: {self.st.getMean(self.x)}")
        meanLabel.pack(side= TOP)

        medianLabel = Label(reportedLabelFrame, text=f"Median : {self.st.getMedian(self.x)}")
        medianLabel.pack(side= TOP)

        modeLabel = Label(reportedLabelFrame, text=f"Mode: {self.st.getMode(self.x)}")
        modeLabel.pack(side= TOP)

        varianceLabel = Label(reportedLabelFrame, text=f"Variance: {self.st.getVariance(self.x)}")
        varianceLabel.pack(side= TOP)


        # Death Cases
        deathLabelFrame = LabelFrame(botLeftFrame, text="Reported Cases Stats", height= f"{botLeftFrame.winfo_vrootheight() * (1 / 4)}", width= f"{botLeftFrame.winfo_screenheight()}")
        deathLabelFrame.pack_propagate(False)
        deathLabelFrame.pack()

        meanLabel = Label(deathLabelFrame, text=f"Mean: {self.st.getMean(self.z)}")
        meanLabel.pack(side=TOP)

        medianLabel = Label(deathLabelFrame, text=f"Median : {self.st.getMedian(self.z)}")
        medianLabel.pack(side=TOP)

        modeLabel = Label(deathLabelFrame, text=f"Mode: {self.st.getMode(self.z)}")
        modeLabel.pack(side=TOP)

        varianceLabel = Label(deathLabelFrame, text=f"Variance: {self.st.getVariance(self.z)}")
        varianceLabel.pack(side=TOP)


        # Both Cases
        commonLabelFrame = LabelFrame(botLeftFrame, text="Reported Cases Stats", height= f"{botLeftFrame.winfo_vrootheight() * (1 / 4)}", width= f"{botLeftFrame.winfo_vrootwidth()}")
        commonLabelFrame.pack_propagate(False)
        commonLabelFrame.pack()

        correlationLabel = Label(commonLabelFrame, text=f"Correlation: {self.st.getCorrelation(self.x, self.z)}")
        correlationLabel.pack(side=TOP)

        regressionB0Label = Label(commonLabelFrame, text=f"B0: {self.st.calculateB0(self.x, self.z)}")
        regressionB0Label.pack(side=TOP)

        regressionB1Label = Label(commonLabelFrame, text=f"B1: {self.st.calculateB1(self.x, self.z)}")
        regressionB1Label.pack(side=TOP)

        regressionLabel = Label(commonLabelFrame, text=f"Regression: Y = {self.st.calculateB0(self.x, self.z)} + {self.st.calculateB1(self.x, self.z)}X")
        regressionLabel.pack(side=TOP)

    def main(self, x, y, z, gr, st):

        # Adjusting Frames
        topFrame.pack_propagate(False)
        topFrame.pack(side= TOP)

        botFrame.pack_propagate(False)
        botFrame.pack(side= BOTTOM)

        botRightFrame.pack_propagate(False)
        botRightFrame.pack(side= RIGHT)

        botLeftFrame.pack_propagate(False)
        botLeftFrame.pack(side= LEFT)

        # counter = 0
        # for i in x:
        #     x[counter] = i / 1000
        #     counter = counter + 1
        #
        # counter = 0
        # for i in z:
        #     z[counter] = i / 1000
        #     counter = counter + 1

        # Calling Frame Functions
        self.addButtonsToTopFrame(topFrame)
        self.addLabelsToBottomLeftFrame(botLeftFrame)

        # Reducing Data Size
        self.reduceData(x)


# Creating Window
window = Tk()

# Window Characteristics
X_AXIS = window.winfo_screenwidth()
Y_AXIS = window.winfo_screenheight()
window.state("zoomed")
window.title("Corona Virus Across The World!")

# Frames
topFrame = Frame(window, height=f"{Y_AXIS / 8}", width=f"{X_AXIS}")
botFrame = Frame(window, height=f"{Y_AXIS * (7 / 8)}", width=f"{X_AXIS}")
botRightFrame = Frame(botFrame, height=f"{botFrame.winfo_screenheight()}", width=f"{botFrame.winfo_screenwidth() * (6 / 8)}")
botLeftFrame = Frame(botFrame, height=f"{botFrame.winfo_screenheight()}", width=f"{botFrame.winfo_screenwidth() * (2 / 8)}")

start = Main(window, topFrame, botFrame, botRightFrame, botLeftFrame)
window.mainloop()
