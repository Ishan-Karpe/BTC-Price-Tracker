
# the code will make a request to the URL which will trigger an action

import tkinter as tk
from tkinter import messagebox # to show a message box
import requests #send a request to the URL

root = tk.Tk() # create a root window
root.title("Crypto Price Checker")

crypto_var = tk.StringVar(root) # to store the crypto name
threshold_var = tk.StringVar() # to store the threshold value
current_price_label = tk.Label(text="") # to display the current price of the crypto
current_price_label.pack() # pack the label

#get the current price of Bitcoin
def get_price(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    
    
    # if it is not found handle it

    if crypto not in data: #  # if the crypto is not found
        return None

    return data[crypto]['usd'] # return the price in USD

# create a function to check the price
def check_price():
    crypto = crypto_var.get().lower()
    try:
        threshold = float(threshold_var.get())
    except ValueError: # if the threshold is not a number
        messagebox.showerror("Error", "Threshold must be a number")
        return
    price = get_price(crypto) # get the price of the crypto

    if price is None: # if the crypto is not found
        messagebox.showerror("Error", f"{crypto} not found")
        return

    current_price_label.config(text=f"Current {crypto.upper()} price: ${price}")

    if price > threshold:
        messagebox.showinfo("Price Alert", f"{crypto.upper()} price is above ${threshold}")

tk.Label(root, text="Crypto:").pack() #  # label for the crypto
tk.Entry(root, textvariable=crypto_var).pack() # entry for the crypto
tk.Label(root, text="Threshold:").pack() # label for the threshold
tk.Entry(root, textvariable=threshold_var).pack() # entry for the threshold
tk.Button(root, text="Check Price", command=check_price).pack() # button to check the price
#pack() the current price label and is used to display the current price of the crypto

root.mainloop() # run the GUI
# the line above always comes last

'''In Summary:
1. Import necessary libraries: tkinter for GUI, messagebox for alerts, and requests for API calls.
2. Create the main application window using tkinter.
3. Define a StringVar to store the cryptocurrency name and another for the threshold value.
4. Create a label to display the current price of the cryptocurrency.
5. Define a function to fetch the current price of a given cryptocurrency using the CoinGecko API.
6. Get the price of the cryptocurrency in USD.'''