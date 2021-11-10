from numpy.core.numeric import correlate
import plotly
import plotly.express as px
import csv
import numpy as np

def plotFigure():
    with open("StudentMarksvsDaysPresent.csv")as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x="Marks-In-Percentage",y="Days-Present")
        fig.show()

def getDataSource():
    Student_marks=[]
    Day_present= []
    with open ("StudentMarksvsDaysPresent.csv")as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            Day_present.append(float(row["Marks-In-Percentage"]))
            Student_marks.append(float(row["Days-Present"]))
    
    return{"x":Day_present,"y":Student_marks}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Marks and Days Present  is ",correlation)

def main():
    dataSource = getDataSource()
    findCorrelation(dataSource)
    plotFigure()

main()


        
