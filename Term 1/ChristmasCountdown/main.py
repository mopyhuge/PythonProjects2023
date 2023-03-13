from clock import *

def main():
    root = Tk()
    app = Application(root)
    root.after(1,app.update())
    root.mainloop()




main()