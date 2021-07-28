import requests
from tkinter import *
from bs4 import BeautifulSoup


url= "https://www.google.co.in/maps"
master = Tk()
master.title("Google map")
master.geometry("500x500")

def googlemap():
    page = requests.get(url)
    soup = BeautifulSoup(page.content,("html.parser"))
    Map = soup.find("div",class_="vasquette id-app-container pane-empty-mode app-imagery-mode app-globe-mode app-planetary-earth-mode")
    search_bar = soup.find("div", class_="vasquette-margin-enabled noprint id-omnibox")
    
    mapLabel.config(text = Map)
    search_barLabel.config(text = search_bar)



api = "AIzaSyCjlu1-z7jYwBz5Ug93yXEkFwTwYcDpo5o"
mapLabel = Label(master)
mapLabel.grid(row = 0)
search_barLabel = Label(master)
mapLabel.grid(row = 0, sticky = "W", padx = 20)

master.mainloop()