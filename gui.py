import tkinter as tk

w = tk.Tk()
w.title("Scraper")
w.geometry("800x600")
# entry = tk.Entry(parent, options)

def scrape():
    product = product_var.get()
    price_min = price_min_var.get()
    price_max = price_max_var.get()

    print(product, price_min, price_max)

    product_var.set("")
    price_min_var.set("")
    price_max_var.set("")

frm = tk.Frame(Tk(), padding=10)
frm.grid()
product_var = tk.StringVar()
price_min_var = tk.StringVar()
price_max_var = tk.StringVar()

product_label = tk.Label(w, text = "Product name", font = ("calibre", 10, "bold"))
product_entry = tk.Entry(w, textvariable = product_var, font = ("calibre", 10, "normal"))

price_min_label = tk.Label(w, text = "Minimum price", font = ("calibre", 10, "bold"))
price_min_entry = tk.Entry(w, textvariable = price_min_var, font = ("calibre", 10, "normal"))

price_max_label = tk.Label(w, text = "Maximum price", font = ("calibre", 10, "bold"))
price_max_entry = tk.Entry(w, textvariable = price_max_var, font = ("calibre", 10, "normal"))

scrape_btn = tk.Button(w, text = "SCRAPE", command = scrape)

product_label.grid(row=0, column=0)
product_entry.grid(row=0, column=1)

price_min_label.grid(row=1, column=0)
price_min_entry.grid(row=1, column=1)

price_max_label.grid(row=2, column=0)
price_max_entry.grid(row=2, column=1)

w_input = scrape_btn.grid(row=3, column=0)

w.mainloop()

print(w_input)