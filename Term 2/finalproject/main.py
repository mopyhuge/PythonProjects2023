from applications import *



def main():
    root = Tk()
    get_file = Get_File_Name(root)
    if create_app:
        app = Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()