import tkinter as tk


class FrmDashboard(tk.Frame):
    def __init__(self, master, background='#333333', items_number=4):
        super().__init__(master, background=background)

        self.grid_columnconfigure((0, 1), weight=1)

        self.lbl_pie_chart = tk.Label(self,
                                      foreground='#FFFFFF',
                                      background=background,
                                      text='PIE CHART',
                                      font=('Verdana', 18))
        self.lbl_pie_chart.grid(row=0, column=0,
                                padx=10, pady=10, sticky='ew')

        self.frm_trend = tk.Frame(self,
                                  background=background)
        self.frm_trend.grid(row=0, column=1,
                            padx=10, pady=10, sticky='ew')
        self.frm_trend.grid_columnconfigure(0, weight=1)
        self.frm_trend.grid_columnconfigure((1, 2), weight=2)

        for i in range(items_number):
            self.lbl_crypto_color_code = tk.Label(self.frm_trend,
                                                  foreground='#FFFFFF',
                                                  background=background,
                                             text=f'CC {i}')
            self.lbl_crypto_color_code.grid(row=i, column=0,
                                       padx=10, pady=10, sticky='ew')

            self.lbl_crypto_name = tk.Label(self.frm_trend,
                                            foreground='#FFFFFF',
                                            background=background,
                                             text=f'NAME {i}')
            self.lbl_crypto_name.grid(row=i, column=1,
                                       padx=10, pady=10, sticky='ew')

            self.lbl_crypto_trend = tk.Label(self.frm_trend,
                                             foreground='#FFFFFF',
                                             background=background,
                                             text=f'TREND {i}%')
            self.lbl_crypto_trend.grid(row=i, column=2,
                                       padx=10, pady=10, sticky='ew')
