import tkinter as tk


class Gui:
    def __init__(self):
        self.returns = None
        self.window = tk.Tk()
        self.product_name_input = tk.Entry(self.window)
        self.max_price_input = tk.Entry(self.window)
        self.min_price_input = tk.Entry(self.window)
        self.scrape_button = tk.Button(self.window, text="Scrape", command=self.scrape_button_command)

        self.window.iconbitmap("icon.ico")
        self.window.title("Scrape Prices")
        self.window.geometry('%dx%d+%d+%d' % (300, 200,
                                              (self.window.winfo_screenwidth() / 2) - (300 / 2),
                                              (self.window.winfo_screenheight() / 2) - (200 / 2)))
        self.window.resizable(0, 0)

        tk.Label(self.window, text="Product Name:", font=("calibre", 10, "bold")).pack()
        self.product_name_input.pack()
        tk.Label(self.window, text="Maximum Price:", font=("calibre", 10, "bold")).pack()
        self.max_price_input.pack()
        tk.Label(self.window, text="Minimum Price:", font=("calibre", 10, "bold")).pack()
        self.min_price_input.pack()
        self.scrape_button.pack(side=tk.BOTTOM, pady=16)

        self.window.mainloop()

    def scrape_button_command(self):
        if self.product_name_input.get() != "":
            self.returns = self.product_name_input.get(), self.max_price_input.get(), self.min_price_input.get()
            self.window.destroy()
