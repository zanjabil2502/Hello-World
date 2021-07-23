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
        textview = Gtk.TextView()
        buffer1.set_text("test")
        textview.set_buffer(buffer1)
        scrolled_window.add(textview)
        p = subprocess.Popen(
                    "free -h", shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT
                    )
        encoding ='utf-8'
        for line in p.stdout.readlines():
            lines = str(line, encoding) 
        
        
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
