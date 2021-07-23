#Program GUI
import gi 
import subprocess

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

#Membuat kumpulan fungsi yang diberi nama CommandTextView yang didasari pada GTK.TextView  
class CommandTextView(Gtk.TextView):

    #keadaan initial
    def __init__(self):
        super(CommandTextView, self).__init__()
        self.textbuffer = self.get_buffer()

    #keadaan saat run, dimana membuat fungsi run  
    def run(self):
        #menjalankan perintah terminal yaitu free -h
        proc = subprocess.Popen(
                    "free -h", shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT
                    )
        #membuat fungsi dengan nama listToString, yaitu mengubah data list ke String
        def listToString(s):
            str1= " "
            return (str1.join(s))
        #pembacaan hasil perintah terminal
        s = proc.stdout.readlines()
        encoding ='utf-8'
        text =[]
        for line in s:
            #mengubah pembacaan dengan format byte ke string
            lines = str(line, encoding)
            text.append(lines)
        
        #mengubah list ke string
        text = listToString(text)
        #pembacaan string untuk ditampilkan ke textview
        self.textbuffer.set_text(text)

#membuat window GUI
ctv = CommandTextView()
win=Gtk.Window()

#memberikan fungsi pada tombol close pada window
win.connect("delete-event", lambda wid,event: Gtk.main_quit()) 

#mengatur ukuran window
win.set_size_request(500,200)

#menambahkan CTV pada window
win.add(ctv)
win.show_all()
ctv.run()
Gtk.main()

