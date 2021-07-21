import requests
from tkinter import *

def GetWeather(master):
    city = search_bar.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=34dfd385ecef669c48fed8e8cfb90fa3"
    json_data = requests.get(api).json()
    weather = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] -273.15)
    temp_min = int(json_data['main']['temp_min'] -273.15)
    temp_max = int(json_data['main']['temp_max'] -273.15)
    humidity = json_data['main']['humidity']

    main_info = city + "\n"+ weather + "\n" + str(temp)
    sub_info = "\n" + "Min temp: " + str(temp_min) + "\n" +"Max temp: " + str(temp_min) + "\n" + "Humidity: " + str(humidity)

    Label1.config(text = main_info)
    Label2.config(text=sub_info)
    print(main_info)
    print(sub_info)
    

master = Tk()
master.title("Weather app")

master.geometry("500x400")

t = ("poppins", 35 ,"bold")
f = ("poppins", 15, "bold")

search_bar = Entry(master, font = f)
search_bar.pack(anchor = "center")
search_bar.focus()
search_bar.bind('<Return>', GetWeather)

Label1 = Label(master, font=t)
Label1.pack()
Label2 = Label(master, font=f )
Label2.pack()

master.mainloop()