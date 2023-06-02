from tk_gui.main_window import MainWindow
from repositories.db_repo import db_init, db_seed


if __name__ == '__main__':
    
    db_init()
    db_seed()

    tk_app = MainWindow()
    tk_app.mainloop()