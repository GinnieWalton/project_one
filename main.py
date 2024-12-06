from gui import *

def main():
    window = Tk()
    window.title('VOTE MENU')

    window.geometry('300x400')
    window.resizable(False, False)
    window.config(bg='lightblue')
    Gui(window)
    window.mainloop()


if __name__ == "__main__":
    main() 