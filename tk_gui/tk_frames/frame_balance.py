import tkinter as tk


class FrmBalance(tk.Frame):
    def __init__(self, master, background='#16c784'):
        super().__init__(master, background=background)

        self.grid_columnconfigure(0, weight=1)

        self.lbl_balance_title = tk.Label(self,
                                          background=background,
                                          text='Balance'.upper(),
                                          font=('Verdana', 18))
        self.lbl_balance_title.grid(row=0, column=0,
                                    padx=10, pady=10, sticky='ew')

        self.lbl_balance_amount = tk.Label(self,
                                          background=background,
                                          text='20.916,92 EUR',
                                          font=('Verdana', 24))
        self.lbl_balance_amount.grid(row=1, column=0,
                                    padx=10, pady=10, sticky='ew')

        self.lbl_balance_trend = tk.Label(self,
                                          background=background,
                                          text='+25,93 %',
                                          font=('Verdana', 14))
        self.lbl_balance_trend.grid(row=2, column=0,
                                    padx=10, pady=10, sticky='ew')