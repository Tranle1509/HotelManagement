from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtWidgets import QColorDialog, QFileDialog

from RoomBookingReport.MainWindow import Ui_MainWindow
import numpy as np
import pyqtgraph as pg
import pandas as pd
import random as nd

from PyQt6.QtWidgets import QMainWindow

class MainWindowEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Thiết lập giao diện


    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow

        self.setupBarGraph()
        self.setupSignal()
    def setupBarGraph(self):
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setTitle(
            "Room Booking Report for 6 months",
            color="#FAA7B8",
            size="15pt",
            bold=True,
            italic=True,
            font="Times New Roman"
        )

        self.graphWidget.setBackground('black')

        labelStyle = {"color": "#FAA7B8", "font-size": "18px", "font-family": "Times New Roman", "font-weight": "bold"}
        labelBrandStyle = {"color": "yellow", "font-size": "18px", "font-family": "Times New Roman",
                           "font-weight": "bold"}
        self.graphWidget.setLabel("left", "Type of room", **labelBrandStyle)
        self.graphWidget.setLabel("bottom", "Months", **labelStyle)
        self.graphWidget.setLabel("right", "Danteria Exxclusive Hotel", **labelBrandStyle)

        self.graphWidget.showGrid(x=True, y=True)

        self.width = 0.2
        self.bargraphItems = []

        self.legend = self.graphWidget.addLegend()

        self.layoutGraph.addWidget(self.graphWidget)

    def setupSignal(self):
        self.pushButtonPickDataset.clicked.connect(self.processPickDataset)
        self.chkBackgroundGrid.stateChanged.connect(self.processChangeGrid)
        self.chkLegend.stateChanged.connect(self.processChangeLegend)
        self.pushButtonChangBackground.clicked.connect(self.processChangeChartBackground)
        self.pushButtonChangeBarColor.clicked.connect(self.processChangeBarColor)

    def processPickDataset(self):
        filters = "Dataset (*.xlsx);;All files(*)"
        filename, selected_filter = QFileDialog.getOpenFileName(
            self.MainWindow,
            filter=filters,
        )
        self.lineEditDataset.setText(filename)

        self.drawChart(filename)

    def drawChart(self,datasetPath):
        #read Excel file into DataFrame by Pandas
        dataframe = pd.read_excel(datasetPath, engine="openpyxl")
        #Read columns, we omit first column (corner)
        #Hà Nội,Huế,TP.HCM,Cần Thơ,An Giang:
        self.xlab = dataframe.columns.values[1:]
        #create an array from 1 to number of column
        self.positions = np.arange(1, len(self.xlab) + 1)
        #remove existing BarGraph Item
        #(user can choose file many times)
        for barItem in self.bargraphItems:
            self.graphWidget.removeItem(barItem)
        self.bargraphItems = []
        self.cboBarItem.clear()
        i = 0
        #loop to read row data
        for row in range(len(dataframe.values)):
            #Get value in the first column for each row(quarter X)
            name = dataframe.values[row][0]
            #Get an Array data for each row
            revenues = dataframe.values[row][1:].tolist()
            #setup the position for each graph bar item
            x = self.positions + i * self.width
            #random color for each bar item
            brush = (nd.randint(0, 255), nd.randint(0, 255), nd.randint(0, 255))
            #create BarGraphItem:
            bargraphItem = pg.BarGraphItem(x=x, height=revenues, width=self.width, brush=brush, name=name)
            i = i + 1
            #store bargraphItem into bargraphItems
            self.bargraphItems.append(bargraphItem)
            #add the Bar Graph Item into the Chart
            self.graphWidget.addItem(bargraphItem)
            #Draw the name of BarItem into QComBoBox
            self.cboBarItem.addItem(bargraphItem.name(), bargraphItem)
        #setup tick
        self.autoTick(self.graphWidget, self.xlab)
        #setup label
        self.autolabel(self.bargraphItems)
    def processChangeGrid(self,value):
        state=Qt.CheckState(value)
        if state==Qt.CheckState.Checked:
            self.graphWidget.showGrid(x=True, y=True)
        else:
            self.graphWidget.showGrid(x=False, y=False)
    def processChangeLegend(self,value):
        state=Qt.CheckState(value)
        if state==Qt.CheckState.Checked:
            self.legend.show()
        else:
            self.legend.hide()
    def processChangeChartBackground(self):
        dialog = QColorDialog()
        if dialog.exec():
            color = dialog.currentColor()
            self.graphWidget.setBackground(color.name())
            del dialog
    def processChangeBarColor(self):
        dialog = QColorDialog()
        if dialog.exec():
            color = dialog.currentColor()
            bargraphItem=self.bargraphItems[self.cboBarItem.currentIndex()]
            bargraphItem.opts["brush"]=color.name()
            bargraphItem._updateColors(bargraphItem.opts)
            del dialog
    def autoTick(self,graphWidget, xlab):
        ticks = []
        for i, item in enumerate(xlab):
            ticks.append((i +1+ 2*self.width, item))
        ticks = [ticks]
        ax = graphWidget.getAxis('bottom')
        ax.setTicks(ticks)

    def autolabel(self,barItems):
        # attach some text labels
        for barItem in barItems:
            xs, heights = barItem.getData()
            for i in range(len(heights)):
                height = heights[i]
                x = xs[i]
                clr = barItem.opts["brush"]
                text = pg.TextItem(str(height), color=clr)
                text.setParentItem(barItem)
                text.setX(x)
                text.setY(height)
                text.setAnchor((QPointF(0.5, 0.75)))

    def show(self):
        print("📊 Đang mở Barchart...")
        super().show()