# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 17:51:01 2022

@author: MARIA
"""

from tkinter import *
import time
import requests
from PIL import Image, ImageTk

def new_bg_color():
    ask1=Toplevel()
    ask1.geometry("500x50")
    write1 = Label(ask1, text="Pick a color{pink, purple, light green, light blue}: ").grid(row=0, column=0)
    color_bg = Entry(ask1)
    color_bg.grid(row=0, column=1)    
    color=str(color_bg.get())

    def pickcolor():
        color=str(color_bg.get())
        
        time_label.config(bg=color)
        day_label.config(bg=color)
        date_label.config(bg=color)
        
    button = Button(ask1,text="ok",command=pickcolor).grid(row=1,column=0)
    
#-----------------------------------------------------------------------------------------------------------------------------------
    
def new_color_letter():
    ask2=Toplevel()
    ask2.geometry("500x50")
    write2 = Label(ask2, text="Pick a color{white,black,pink, purple, light green, light blue}: ").grid(row=0, column=0)
    color_letter = Entry(ask2)
    color_letter.grid(row=0, column=1)    
    color_fg=str(color_letter.get())
    
    def pick_color_letters():
    
        color_fg=str(color_letter.get())
        time_label.config(fg=color_fg)
        day_label.config(fg=color_fg)
        date_label.config(fg=color_fg)
        
    button2 = Button(ask2,text="ok",command=pick_color_letters).grid(row=1,column=0)
    
#-----------------------------------------------------------------------------------------------------------------------------------
    
def clock():
    
    tm = time.strftime("%I:%M:%S %p")
    
    time_label.config(text=tm)
    
    day = time.strftime("%A")
    day_label.config(text=day)
    
    date = time.strftime("%d %B %Y")
    date_label.config(text=date)
    
    window.after(1000,clock)

#-----------------------------------------------------------------------------------------------------------------------------------
    
def new_wind():
    global city_name
    
    ask=Toplevel()
    ask.geometry("200x50")
    write = Label(ask, text="City: ").grid(row=0, column=0)
    city = Entry(ask)
    city.grid(row=0, column=1)    
    city_name=str(city.get())
    
    
    def weath():
    
    
    
        api_key = "9e27ff86db8e4ce681b45a7e3dac91ad"
        lat = 45.46427
        lon = 9.18951
    #city = "Milan"

        url = "https://api.weatherbit.io/v2.0/current?key=9e27ff86db8e4ce681b45a7e3dac91ad&include=minutely"




        city_name = city.get()

    #url = "https://api.weatherbit.io/v2.0/current" 

        payload = {
        
            'city': city_name,
            }   

        response = requests.get(url, params=payload)

        data = response.json()

        if 'error' in data:
            print('Error:', data['error'])
        else:
            temperature = data["data"][0]["temp"]
            pressure    = data["data"][0]["pres"]
            humidity    = data["data"][0]["rh"]
            weather     = data["data"][0]["weather"]["description"]
        #description = data["data"][0]

            #print(f"Temperature (in Celsius unit) = {temperature}")
            #print(f"atmospheric pressure (in hPa unit) = {pressure}")
            #print(f"humidity (in percentage) = {humidity}")
            #print(f"description = {weather}")
            ask.destroy()
            weather_results=Toplevel()
            results = Text(weather_results,relief='raised')
            results.pack()
            
            results.insert('1.0',f"Temperature (in Celsius unit) = {temperature}\n")
            results.insert('2.0',f"atmospheric pressure (in hPa unit) = {pressure}\n")
            results.insert('3.0',f"humidity (in percentage) = {humidity}\n")
            results.insert('4.0',f"description = {weather}")
            
    ok = Button(ask,text="ok",command=weath).grid(row=1,column=0)
    
    
#--------------------------------------------------------------------------------------------------------------------------

window = Tk()
window.title("Clock and weather")
image_l = PhotoImage(file="C:\\Users\\MARIA\\Desktop\\python_exercises\\l.png")


image_2 = PhotoImage(file="C:\\Users\\MARIA\\Desktop\\python_exercises\\gamer.png")
window.iconphoto(False, image_2)



window.geometry("600x600")
time_label = Label(window,bg="pink",font=("Georgia",50),fg="white", width="600")
time_label.pack()

day_label = Label(window, bg="pink", font=("Georgia",40),fg="white",width="600")
day_label.pack()

date_label = Label(window,bg="pink", font=("Georgia",40),fg="white",width="600")
date_label.pack()
clock()

color_changer = Button(window, text="Change backgound color", command=new_bg_color)
color_changer.pack()

color_changer2 = Button(window, text="Change color of the words", command=new_color_letter)
color_changer2.pack()

weather = Button(window, text="Ask for the weather in a city",image=image_l, compound=BOTTOM, command = new_wind, width="220", height="220")
weather.pack()


window.mainloop()