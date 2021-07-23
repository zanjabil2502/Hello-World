import gi
import subprocess
import glib


gi.require_version("Gtk", "3.0")
from gi.repository import GObject,Gtk
  
class CommandTextView(Gtk.TextView):
    ''' Nice TextView that reads the output of a command syncronously '''
    def __init__(self, command):
        '''command : the shell command to spawn'''
        super(CommandTextView, self).__init__()
        self.command = command
    def run(self):
        ''' Runs the process '''
        proc = subprocess.Popen(self.command, stdout = subprocess.PIPE) # Spawning
        glib.io_add_watch(proc.stdout, # file descriptor
                          glib.IO_IN,  # condition
                          self.write_to_buffer ) # callback
    def write_to_buffer(self, fd, condition):
        char = fd.read(1) # we read one byte per time, to avoid blocking
        buf = self.get_buffer()
        buf.insert_at_cursor(char) # When running don't touch the TextView!!


def test():
    # This command will download one project of mine deheh
    ctv = CommandTextView("ls")
    win=Gtk.Window()
    win.connect("delete-event", lambda wid,event: Gtk.main_quit()) # Defining callbacks with lambdas
    win.set_size_request(200,300)
    win.add(ctv)
    win.show_all()
    ctv.run()
    Gtk.main()
if __name__=='__main__' : test()
