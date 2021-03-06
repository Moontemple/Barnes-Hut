from Tkinter import Tk
import Barnes_Hut.Graphics as grph
from time import time
import warnings
warnings.filterwarnings("ignore")

def run(frame):
    """
    Run Function
    Logs title text and times
    Creates instance of Graphics
        calls add_stars of Graphics
        calls add_tree of Graphics

    :param frame:
    Tkinter frame to draw simulation on

    :return:
    Instance of Graphics from Barnes_Hut.Graphics
    """
    with open("title.txt", 'r') as file:
        print file.read()

    t = time()
    window = grph.Graphics(frame)
    t = time() - t
    print "Class creation took {}s".format(t)
    print "Rendering window..."

    t = time()
    window.add_stars()
    window.add_tree()
    t = time() - t
    print "Rendering took {}s".format(t)
    print "Starting Tkinter... this may take a while"
    return window


if __name__ == '__main__':
    def on_close():
        window.close()      #close window properly
        root.destroy()

    root = Tk()
    root.resizable(width=False, height=False)
    root.protocol("WM_DELETE_WINDOW", on_close)
    window = run(root)
    root.mainloop()