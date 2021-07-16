import requests
from bs4 import BeautifulSoup
from tkinter import Tk
from tkinter import Label
from PIL import ImageTk, Image

url = "https://weather.com/en-BB/weather/today/l/36845bf50838019712986a2e2b564dd5026cda2064f47d39b26aa8bb1fcb1f9d"
master = Tk()
master.title("Weather app")
master.config(background = "black")

img = Image.open("/home/balaji/Pictures/weather.png")
img = img.resize((150, 150))
img=ImageTk.PhotoImage(img)

def getweather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find("h1", class_="CurrentConditions--location--2_osB").text
    temperature = soup.find("span", class_="CurrentConditions--tempValue--1RYJJ").text
    weatherpredicion = soup.find("div", class_="CurrentConditions--phraseValue--17s79").text
    ist = soup.find("div", class_="CurrentConditions--timestamp--3_-CV").text

    locationLabel.config(text=location)
    temperatureLabel.config(text = temperature)
    weatherpredicionLabel.config(text = weatherpredicion)
    ISTLabel.config(text = ist)
    temperatureLabel.after(60000, getweather)
    weatherpredicionLabel.after(60000, getweather)
    ISTLabel.after(60000, getweather)


  
    

locationLabel = Label(master, font=("calibri bold", 20), background = 'black', foreground = 'white')
locationLabel.grid(row = 0, sticky="W", padx=40)
ISTLabel  = Label(master, font = ("calibri bold", 15), background = "black", foreground = "white")
ISTLabel.grid(row = 1,sticky = "W",padx = 40)
temperatureLabel = Label(master, font=("calibri bold", 80), background = 'black', foreground = "white")
temperatureLabel.grid(row =2, sticky = "W", padx= 40)

Label(master, image = img , background = "black").grid(row = 2, sticky="E")
weatherpredicionLabel = Label(master, font=("calibri bold", 40), background = "black", foreground="white")
weatherpredicionLabel.grid(row = 3, sticky="W", padx = 40)

getweather()
master.mainloop()