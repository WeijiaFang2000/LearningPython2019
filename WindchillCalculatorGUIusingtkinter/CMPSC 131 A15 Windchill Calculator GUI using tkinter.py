# Author: Weijia Fang
# Title: Windchill Calculator GUI using tkinter
# Completion Date: Apr 2019

from tkinter import *

#A function to calculate windchill
def calculate_windchill(temperature,windspeed):
    windchill = 35.74 + 0.6215 * temperature - 35.75 * windspeed**0.16 + 0.4275 * temperature * windspeed**0.16
    return round(windchill,1)

#A function to calculate the result when click the button    
def calculate():
    Fahrenheit = int(FahrenheitInput.get())
    WindSpeed = int(SpeedMPHInput.get())

    windchill = calculate_windchill(Fahrenheit, WindSpeed)
        
    CalculatingResultLabel['text']='the windchill temperature is:' + str(windchill) + ' degrees fahrenheit.'

#Initiate tk and add title to the window
app = Tk()
app.title = "Windchill Calculator"

#Create the top level of frame
frameRoot = Frame(app)
frameRoot.pack()

#Create 4 frames to contain labels and input entry
#Display the yellow headline
f1 = Frame(frameRoot)
f1.pack()
WindchillCalculatorLabel = Label(f1, text='Windchill Calculator', fg='red', bg='yellow')
WindchillCalculatorLabel.pack()

#Input temperature
f2 = Frame(frameRoot)
f2.pack()
FahrenheitLabel = Label(f2, text='Enter the temperature in degrees Fahrenheit:')
FahrenheitLabel.pack(side=LEFT)
FahrenheitInput = Entry(f2, width=4)
FahrenheitInput.pack(side=LEFT)

#Input windchill
f3 = Frame(frameRoot)
f3.pack()
SpeedMPHLabel = Label(f3, text='Enter the wind speed in mph:')
SpeedMPHLabel.pack(side=LEFT)
SpeedMPHInput = Entry(f3, width=4)
SpeedMPHInput.pack(side=LEFT)

#Display the button
f4 = Frame(frameRoot)
f4.pack()

CalculatingButton = Button(f4, text='Calculate Windchill', command=calculate)
CalculatingButton.pack()
CalculatingResultLabel = Label(f4, text='the windchill temperature is:')
CalculatingResultLabel.pack()

app.mainloop()
