import tkinter as tk

from tk_gui.tk_frames.frame_scrollable import FrmScrollable



# def canvas_configure(event):
#      canvas.configure(scrollregion=canvas.bbox("all"))


main_window = tk.Tk()
#frm_container = tk.Frame(main_window)
frm_container = FrmScrollable(main_window)
frm_container.pack()




for i in range(35):
     lbl_test = tk.Label(frm_container.frm_scrollable, text=f'Labela index {i + 1}.',
                         font=('Verdana', 16))
     lbl_test.pack()



main_window.mainloop()

