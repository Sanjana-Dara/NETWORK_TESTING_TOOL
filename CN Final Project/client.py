import socket 
from Tkinter import *
import Tkinter as tk
import tkMessageBox
import subprocess, platform
from subprocess import Popen, PIPE
#35.246.29.33
def Main():  
    host = '127.0.0.1'
    serverip = host 
    port = 9009
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.connect((host,port)) 
        
    top = tk.Tk()
    top.title("Network Testing Tool")
    canvas = tk.Canvas(top, height=550, width=750)
    canvas.pack(fill=BOTH, expand = YES)
    
    main_frame = tk.Frame(top, bg="black")
    main_frame.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.8)

    scroll_bar = Scrollbar(main_frame)   
    scroll_bar.pack( side = RIGHT, fill = Y ) 
    mylist = Listbox(main_frame,  yscrollcommand = scroll_bar.set )   
    scroll_bar.config( command = mylist.yview )

    def clearFrame():
       for widget in main_frame.winfo_children():
          widget.destroy()
        
    def pingbox(host=serverip, count=5):
       clearFrame()
       command = "python3 ping.py "+host+" "+str(count)
       stdout = Popen(command, shell=True, stdout=PIPE).stdout
       output = stdout.read()     
       pinglabel = Label(main_frame, text=output, bg="black", fg="white")
       pinglabel.pack()

    def traceroutebox(host=serverip):
       clearFrame()
       command = "sudo python3 tracefinal.py "+host
       stdout = Popen(command, shell=True, stdout=PIPE).stdout
       output = stdout.read()
       for i in output.split("\n"):
           pinglabel = Label(main_frame, text=i, bg="black", fg="white")
           pinglabel.pack()
       
    def nslookupbox(host=serverip):
       clearFrame()
       command = "python3 nslookup.py "+host
       stdout = Popen(command, shell=True, stdout=PIPE).stdout
       output = stdout.read()
       pinglabel = Label(main_frame, text=output, bg="black", fg="white")
       pinglabel.pack()
       
    def ifconfigbox():
       clearFrame()
       stdout = Popen('python3 ifconfig.py', shell=True, stdout=PIPE).stdout
       output = stdout.read()
       pinglabel = Label(main_frame, text=output, bg="black", fg="white")
       pinglabel.pack()

    def digbox(host=serverip):
       clearFrame()
       command = "python3 dig.py "+host
       stdout = Popen(command, shell=True, stdout=PIPE).stdout
       output = stdout.read()
       for i in output.split("\n"):
           pinglabel = Label(main_frame, text=i, bg="black", fg="white")
           pinglabel.pack()
   
    def nmapbox(host=serverip):
       clearFrame()
       command = "python3 nmap.py "+host
       stdout = Popen(command, shell=True, stdout=PIPE).stdout
       output = stdout.read()  
       nmaplabel = Label(main_frame, text=output, bg="black", fg="white")
       nmaplabel.pack()
       
    def routebox(host=serverip):
       clearFrame()
       command = "python3 route.py "+host
       stdout = Popen(command, shell=True, stdout=PIPE).stdout
       output = stdout.read()  
       routelabel = Label(main_frame, text=output, bg="black", fg="white")
       routelabel.pack()


    def getdataping(text_input,top1,funcname):
       data = text_input.get();
       host,count = data.split(",")
       top1.destroy()
       funcname(host,count)
      
    def getdata(text_input,top1,funcname):
       data = text_input.get();
       top1.destroy()
       funcname(data)
       
    def pingcustom():
       top1 = tk.Tk()
       top1.title("Custom ping")
       canvas1 = tk.Canvas(top1, height=100, width=200)
       canvas1.pack() 
       L = Label(top1, text = "Enter IP address,count", font = ('times', 12,'bold'))
       L.place(x=5, y=0.2, width= 180, height=40)
       text_input = Entry(top1, width=30)
       text_input.bind("<Return>", lambda i : getdataping(text_input,top1,pingbox))
       text_input.place(x=10, y=30,width=180, height=30)
       S = Label(top1, text = "Press enter to proceed", font = ('times', 11,'italic'))
       S.place(x=5, y=60, width= 180, height=40)
       top1.mainloop()

    B=  Menubutton ( top, text="ping", relief=RAISED , fg = "white", bg="black", font=('times', 16, 'bold'), cursor="hand2", direction=RIGHT)
    B.menu =  Menu ( B, tearoff = 0 )
    B["menu"] =  B.menu
    B.menu.add_checkbutton ( label="ping server" ,command=pingbox)
    B.menu.add_checkbutton ( label="custom" ,command=pingcustom)
    B.place(relx=0, rely=0.04, relwidth=0.143, relheight=0.075)

    def traceroutecustom():
       top1 = tk.Tk()
       top1.title("Custom Traceroute")
       canvas1 = tk.Canvas(top1, height=100, width=250)
       canvas1.pack() 
       L = Label(top1, text = "Enter IP address", font = ('times', 12,'bold'))
       L.place(x=5, y=0.2, width= 180, height=40)
       text_input = Entry(top1, width=30)
       text_input.bind("<Return>", lambda i : getdata(text_input,top1,traceroutebox))
       text_input.place(x=10, y=30,width=180, height=30)
       S = Label(top1, text = "Press enter to proceed", font = ('times', 11,'italic'))
       S.place(x=5, y=60, width= 180, height=40)
       top1.mainloop()
       
    C=  Menubutton ( top, text="traceroute", relief=RAISED , fg = "white", bg="black", font=('times', 16, 'bold'), cursor="hand2")
    C.menu =  Menu ( C, tearoff = 0 )
    C["menu"] =  C.menu
    C.menu.add_checkbutton ( label="server",command = traceroutebox)
    C.menu.add_checkbutton ( label="custom",command = traceroutecustom)
    C.place(relx=0.143, rely=0.04, relwidth=0.143, relheight=0.075)

    def nslookupcustom():
       top1 = tk.Tk()
       top1.title("Custom nslookup")
       canvas1 = tk.Canvas(top1, height=100, width=250)
       canvas1.pack() 
       L = Label(top1, text = "Enter IP address", font = ('times', 12,'bold'))
       L.place(x=5, y=0.2, width= 180, height=40)
       text_input = Entry(top1, width=30)
       text_input.bind("<Return>", lambda i : getdata(text_input,top1,nslookupbox))
       text_input.place(x=10, y=30,width=180, height=30)
       S = Label(top1, text = "Press enter to proceed", font = ('times', 11,'italic'))
       S.place(x=5, y=60, width= 180, height=40)
       top1.mainloop()
       
    D=  Menubutton ( top, text="nslookup", relief=RAISED , fg = "white", bg="black", font=('times', 16, 'bold'), cursor="hand2")
    D.menu =  Menu ( D, tearoff = 0 )
    D["menu"] =  D.menu
    D.menu.add_checkbutton ( label="server",command = nslookupbox)
    D.menu.add_checkbutton ( label="custom",command = nslookupcustom)
    D.place(relx=0.286, rely=0.04, relwidth=0.143, relheight=0.075)

    E = tk.Button(top, text ="ifconfig", fg = "white", bg="black",font=('times', 16, 'bold'),cursor = "hand2", command = ifconfigbox)
    E.place(relx=0.429, rely=0.04, relwidth=0.143, relheight=0.075)

    def digcustom():
       top1 = tk.Tk()
       top1.title("Custom dig")
       canvas1 = tk.Canvas(top1, height=100, width=200)
       canvas1.pack() 
       L = Label(top1, text = "Enter IP address", font = ('times', 12,'bold'))
       L.place(x=5, y=0.2, width= 180, height=40)
       text_input = Entry(top1, width=30)
       text_input.bind("<Return>", lambda i : getdata(text_input,top1,digbox))
       text_input.place(x=10, y=30,width=180, height=30)
       S = Label(top1, text = "Press enter to proceed", font = ('times', 11,'italic'))
       S.place(x=5, y=60, width= 180, height=40)
       top1.mainloop()
       
    F=  Menubutton ( top, text="dig", relief=RAISED , fg = "white", bg="black",font=('times', 16, 'bold'), cursor="hand2")
    F.menu =  Menu ( F, tearoff = 0 )
    F["menu"] =  F.menu
    F.menu.add_checkbutton ( label="server" ,command = digbox)
    F.menu.add_checkbutton ( label="custom",command = digcustom)
    F.place(relx=0.572, rely=0.04, relwidth=0.143, relheight=0.075,)
    
    G = tk.Button(top, text ="route", fg = "white", bg="black",font=('times', 16, 'bold'),command = routebox, cursor="hand2")
    G.place(relx=0.715, rely=0.04, relwidth=0.143, relheight=0.075,)
    
    def nmapcustom():
       top1 = tk.Tk()
       top1.title("Custom nmap")
       canvas1 = tk.Canvas(top1, height=100, width=200)
       canvas1.pack() 
       L = Label(top1, text = "Enter IP address", font = ('times', 12,'bold'))
       L.place(x=5, y=0.2, width= 180, height=40)
       text_input = Entry(top1, width=30)
       text_input.bind("<Return>", lambda i : getdata(text_input,top1,nmapbox))
       text_input.place(x=10, y=30,width=180, height=30)
       S = Label(top1, text = "Press enter to proceed", font = ('times', 11,'italic'))
       S.place(x=5, y=60, width= 180, height=40)
       top1.mainloop()
       
    H=  Menubutton ( top, text="nmap", relief=RAISED , fg = "white", bg="black",font=('times', 16, 'bold'), cursor="hand2")
    H.menu =  Menu ( H, tearoff = 0 )
    H["menu"] =  H.menu
    H.menu.add_checkbutton ( label="server" ,command = nmapbox)
    H.menu.add_checkbutton ( label="custom",command = nmapcustom)
    H.place(relx=0.858, rely=0.04, relwidth=0.143, relheight=0.075,)
    
    top.mainloop() 
    s.close() 
 
if __name__ == '__main__': 
    Main() 
