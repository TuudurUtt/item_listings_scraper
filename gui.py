import tkinter as tk

def retrieve_user_input():
    product_name = product_name_input.get()
    min_price = min_price_input.get()
    max_price = max_price_input.get()

    print(product_name, min_price, max_price)

    product_name_input.delete(0, tk.END)
    min_price_input.delete(0, tk.END)
    max_price_input.delete(0, tk.END)

    return [product_name, min_price, max_price]

def gui_input():

    window = tk.Tk()

    #replace window icon with icon.png
    window.iconbitmap("icon.ico")

    window.title("Scrape Prices")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width/2) - (300/2)
    y = (screen_height/2) - (200/2)
    window.geometry('%dx%d+%d+%d' % (300, 200, x, y))

    #lock window size
    window.resizable(0, 0)

    def retrieve_user_input():
        product_name = product_name_input.get()
        min_price = min_price_input.get()
        max_price = max_price_input.get()

        print(product_name, min_price, max_price)

        product_name_input.delete(0, tk.END)
        min_price_input.delete(0, tk.END)
        max_price_input.delete(0, tk.END)

        return [product_name, min_price, max_price]


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

    buffer = tk.Label(window, text=" ")
    buffer.pack(side=tk.BOTTOM)

    scrape_button = tk.Button(window, text="Scrape", command=retrieve_user_input)
    scrape_button.pack(side=tk.BOTTOM)

    window.mainloop()

gui_input()