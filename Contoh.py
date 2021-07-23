import gi
import subprocess

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello World")
        self.set_default_size(300, 450)
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_border_width(5)
        
        buffer1 = Gtk.TextBuffer()
        buffer1.set_text("This is")
        textview = Gtk.TextView(buffer=buffer1.set_text("This is"))
        textview.set_wrap_mode(Gtk.WrapMode.WORD)
        scrolled_window.add(textview)
        
        p = subprocess.Popen(
                    "free -h", shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT
                    )
        for line in p.stdout.readlines():
            print(line),
        retval = p.wait()


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
