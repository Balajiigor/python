import requests
from bs4 import BeautifulSoup
from tkinter import Tk
from tkinter import Label
from PIL import ImageTk, Image

Tamil_nadu = "https://weather.com/en-IN/weather/today/l/4a5f6abb61cf684f3b18578ada1c5647346a0c273b8d5cd86c1eb48842d572e5"
Seattle = "https://weather.com/en-IN/weather/today/l/ced0de18c1d771856e6012f3abf0a952cfe22952e72e516e6e098d54ca737114"
Dubai = "https://weather.com/en-IN/weather/today/l/af60f113ba123ce93774fed531be2e1e51a1666be5d6012f129cfa27bae1ee6c"
Paris = "https://weather.com/en-IN/weather/today/l/501361e097b79e8221d5c0b1447e80a0bf1c48b8fee1e4d98d4dad397ba2f204"
Norway = "https://weather.com/en-IN/weather/today/l/cb003c6f366a3ae14b6a78ac5f2cfd18285fa02d15f892112dd00961afcb043b"
Los_Angeles = "https://weather.com/en-IN/weather/today/l/0f4e045fdd139c3280846cf4eaae5b3f1c6ca58d13169016e6209f7b86872fc1"
Arab = "https://weather.com/en-IN/weather/today/l/9eb72583100b2852c7d0da1a9f6d6d523dc38cfeb848d2ba82517e7f8bb44626"
Moscow = "https://weather.com/en-IN/weather/today/l/34f2aafc84cff75ae0b014754856ea5e7f8ddf618cf9735549dfb5e016c28e10"


master = Tk()
master.title("Weather app")
master.config(background = "black")

img = Image.open("/home/balaji/Pictures/weather.png")
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

def getWeather():
    page = requests.get(Tamil_nadu)
    soup = BeautifulSoup(page.content, "html.parser")
    location =soup.find("h1", class_="CurrentConditions--location--2_osB").text
    time = soup.find("div",class_="CurrentConditions--timestamp--3_-CV" ).text
    temperature = soup.find("span",class_="CurrentConditions--tempValue--1RYJJ" ).text
    weatherPrediction = soup.find("div",class_="CurrentConditions--phraseValue--17s79" ).text
    alert = soup.find("div", class_="CurrentConditions--precipValue--1RgXi").text
    print(location)
    print(time)
    print(temperature)
    print(weatherPrediction)
    print(alert)

    locationLabel.config(text = location)
    timeLabel.config(text = time)
    temperaturLabel.config(text = temperature)
    weatherPredictionLabel.config(text = weatherPrediction)
    alertLabel.config(text = alert)

    timeLabel.after(60000, getWeather)
    temperaturLabel.after(60000, getWeather)
    weatherPredictionLabel.after(60000, getWeather)
    alertLabel.after(60000, getWeather)

    


locationLabel = Label(master, font = ("calibri bold", 30), background = "black", foreground = "white")
locationLabel.grid(row = 0, sticky="W", padx=40)
timeLabel = Label(master, font =("calibri bold", 20), background = "black", foreground = "white")
timeLabel.grid(row = 1, sticky = "W", padx = 40)
temperaturLabel = Label(master, font=("calibri bold", 70), background="black", foreground = "white")
temperaturLabel.grid(row =2, sticky = "W", padx = 40)
Label(master, image = img, background = "black").grid(row = 2, sticky = "E")
weatherPredictionLabel = Label(master, font= ("calibri bold", 40), background = "black", foreground ="white")
weatherPredictionLabel.grid(row = 3, sticky = "W", padx=40)
alertLabel = Label(master, font = ("calibri bold", 15), background = "black", foreground = "white")
alertLabel.grid(row= 4, sticky ="W", padx = 40)

getWeather()
master.mainloop()