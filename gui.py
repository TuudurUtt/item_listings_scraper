import tkinter as tk

window = tk.Tk()

window.title("Scrape Prices")

window.geometry("300x200")

def scrape():
    product_name = product_name_input.get()
    min_price = min_price_input.get()
    max_price = max_price_input.get()

    print(product_name, min_price, max_price)

    product_name_input.delete(0, tk.END)
    min_price_input.delete(0, tk.END)
    max_price_input.delete(0, tk.END)


max_price_label = tk.Label(window, text="Maximum Price:",font = ("calibre", 10, "bold"))
max_price_label.pack()

max_price_input = tk.Entry(window)
max_price_input.pack()

min_price_label = tk.Label(window, text="Minimum Price:",font = ("calibre", 10, "bold"))
min_price_label.pack()

min_price_input = tk.Entry(window)
min_price_input.pack()

product_name_label = tk.Label(window, text="Product Name:",font = ("calibre", 10, "bold"))
product_name_label.pack()

product_name_input = tk.Entry(window)
product_name_input.pack()

scrape_button = tk.Button(window, text="Scrape", command=scrape)
scrape_button.pack()

window.mainloop()