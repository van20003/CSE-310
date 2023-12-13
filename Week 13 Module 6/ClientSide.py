"""
This will is my code for the Client side of the project. The CLients will have a simple GUI to
input the information needed. Then through the ServerSide program, it will have a established
connection with the API host and obtain their information and output it for the user to see.

"""

import tkinter as tk
from tkinter import scrolledtext
import socket
import json


# This first function is to get a response from the API to get the values we want
# when we search/input a location and then output or show us the information

def show_weather_data(response):
    output_text.delete(1.0, tk.END)  
    if response:
        try:
            formatted_response = json.dumps(response, indent=4) 
            output_text.insert(tk.END, formatted_response) 
        except Exception as e:
            print(f"Error displaying data: {e}")
    else:
        output_text.insert(tk.END, "No valid weather data received")

# This funtion is how we input our desired location for the program to work

def send_location_request():
    location = entry.get()
    host = '127.0.0.1'
    port = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((host, port))
            client_socket.sendall(location.encode('utf-8'))
            
            response = client_socket.recv(8192).decode('utf-8')
            show_weather_data(response)
        except ConnectionRefusedError:
            show_weather_data("Connection error.")

# This is a simple GUI, not needed. If this was not in place the user would simple type in
# their input/location in the terminal instead of the GUI. It has a simple text entry box
# and a simple button to submit the input

root = tk.Tk()
root.title("Weather - James Vang | BYUI 2023")
root.geometry("500x500")

label = tk.Label(root, text="Enter location:")
label.pack()

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Get Weather", command=send_location_request)
submit_button.pack()

output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
output_text.pack()

root.mainloop()

# My struggles here is that the information that is supposed to be displayed here is instead put into the
# terminal of the Serverside. I spend hours trying to fix it but would instead ruin it and not get a
# response back from my API I was using. So instead I ended up at least keeping getting result from my
# API than just full on errors. Also I could not figure out how to output the Temps in F instead of C.