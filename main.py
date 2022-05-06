import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font
import requests


def format_response(weather):
   try:
       name = weather['name']
       desc = weather['weather'][0]['description']
       temp = weather['main']['temp']
       final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
   except:
       final_str = 'There was a problem retrieving that information'
   return final_str



def get_weather(city):

    weather_key = 'dea490e8e25a1a023eef92860ae8611e'
    url='https://api.openweathermap.org/data/2.5/weather'
    params = {'appid': weather_key, 'q': city, 'units': 'metric'}
    response=requests.get(url,params=params)
    weather=response.json()
    label2['text'] = format_response(weather)





root = tk.Tk()
canvas=tk.Canvas(root, height=300, width=500)
canvas.pack()



def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('background.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.place(x=0,y=0,relwidth=1, relheight=1)

frame = tk.Frame(root,highlightbackground="black", highlightthickness=2)
frame.place(relx=0.38, rely=0.1, relwidth=0.5, relheight=0.12, anchor='n')

entry = tk.Entry(frame, font=('Gabriola',20))
entry.place(relwidth=1, relheight=1)

frame2 = tk.Frame(root,highlightbackground="black", highlightthickness=2)
frame2.place(relx=0.75, rely=0.1, relwidth=0.3, relheight=0.12, anchor='n')
button = tk.Button(frame2, text="Get Weather",bg= '#FFFFFF',font=('Gabriola',20),command=lambda: get_weather(entry.get()))
button.place( relheight=1, relwidth=1)


lower_frame = tk.Frame(root, bd=8,highlightbackground="black", highlightthickness=2)
lower_frame.place(relx=0.515, rely=0.25, relwidth=0.77, relheight=0.6, anchor='n')

label2 = tk.Label(lower_frame,font=('Gabriola',20))
label2.place(relwidth=1, relheight=1)



root.mainloop()
