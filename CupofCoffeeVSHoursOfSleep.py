from numpy.core.numeric import correlate
import plotly
import plotly.express as px
import csv
import numpy as np

def plotFigure():
    with open("CupOfCoffeeVSHoursOfSleep.csv")as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x="Coffee-in-ml",y="sleep-in-hours")
        fig.show()

def getDataSource():
    Cup_Of_Coffee=[]
    Hours_Of_Sleep= []
    with open ("CupOfCoffeeVSHoursOfSleep.csv")as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
           Hours_Of_Sleep.append(float(row["sleep-in-hours"]))
            Cup_Of_Coffee.append(float(row["Coffee-in-ml"]))
    
    return{"x":Hours_Of_Sleep,"y":Cup_Of_Coffee}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Cups of coffee and Hours of sleep  is ",correlation)

def main():
    dataSource = getDataSource()
    findCorrelation(dataSource)
    plotFigure()

main()
