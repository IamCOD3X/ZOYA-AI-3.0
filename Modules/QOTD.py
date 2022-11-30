import requests

import tkinter as tk
import tkinter.scrolledtext as sb_text
from tkinter import *



def CreateWidgets():

    root.quoteText = sb_text.ScrolledText(root, width=30, height=5, bg='azure3')
    root.quoteText.grid(row=3, column=0, rowspan=5, columnspan=3, padx=10, pady=5)
    # Making Text Widget uneditable by setting state parameter of config() to DISABLED
    root.quoteText.config(state=DISABLED, font = "Calibri 15", wrap="word")

    getQuote()



## function that gets the random quote
def getQuote():
    
    # Concatenating category with the API and sending request to concatenated endpoint
    quote_output = requests.get('https://quote-garden.herokuapp.com/api/v3/quotes/random')
    # Converting the response to the json and fetching the first item from quotes key
    quote_output_json = quote_output.json()
    # Fetching the quote from the above json output
    quote_of_the_day = quote_output_json['data']
    quote_of_the_day_ = quote_of_the_day
    quote=quote_of_the_day_[0]['quoteText'] 
    # Enabling the Text Widget by setting state parameter of config() to NORMAL
    root.quoteText.config(state=NORMAL)
    # Clearing the entries from the Text Widget using the delete() method
    root.quoteText.delete('1.0', END)
    # Displaying quote of the day and it's author in the quoteText Widget
    root.quoteText.insert("end", quote)
    # Making Widget uneditable again after the displaying quote of the day
    root.quoteText.config(state=DISABLED)

# Creating object of tk class
root = tk.Tk()
# Setting the title, background color, windowsize
# & disabling the resizing property
root.title("PythonQuoteOfTheDay")
root.geometry("345x170")
root.config(background="lightgreen")
root.resizable(False, False)
# Creating the tkinter variables

# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()