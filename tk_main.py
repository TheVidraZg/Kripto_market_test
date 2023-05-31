import tkinter as tk

from tk_gui.tk_frames.frame_balance import FrmBalance
from tk_gui.tk_frames.frm_dashboard import FrmDashboard


class MainWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title('Crypto Market App')
        self.geometry('500x700')

        self.frm_balance = FrmBalance(self)
        self.frm_balance.pack(padx=0, pady=(0, 10), fill='x')

        self.frm_dashboard = FrmDashboard(self, items_number=45)
        self.frm_dashboard.pack(padx=10, pady=(0, 10), fill='x')




if __name__ == '__main__':
    tk_app = MainWindow()
    tk_app.mainloop()