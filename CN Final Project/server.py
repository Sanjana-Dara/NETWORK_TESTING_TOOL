# import socket programming library 
import socket 
from Tkinter import *
import Tkinter as tk
import tkMessageBox
import subprocess, platform
from subprocess import Popen, PIPE  
from thread import *
import threading 
clientlist = []
print_lock = threading.Lock() 
  
# thread function 
def threaded(c,addr,i): 
    while True: 
        # data received from client 
        data = c.recv(1024) 
        if not data: 
            print('Disconnected from {} and port {}'. format(addr[0], str(addr[1])) ) 
            del clientlist[i]              
            #print_lock.release() 
            break    
    # connection closed 
    c.close() 
  
def Main(): 
    serverip="127.0.0.1"
    host = serverip 
    port = 9009
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
  
    # put the socket into listening mode 
    s.listen(10) 
    print("socket is listening") 
  
    for i in range(6s): 
  
        # establish connection with client 
        c, addr = s.accept() 
        l = {} 
        #print_lock.acquire() 
        print('Connected to :'+addr[0]+'  '+str(addr[1])) 
        l["ip"] = addr[0]
        l["port"] = addr[1]
        clientlist.append(l)
        start_new_thread(threaded, (c,addr,i)) 
        
        
    top = tk.Tk()
    top.title("Server Network Testing Tool")
    canvas = tk.Canvas(top, bg = "#99d6ff", height=550, width=750)
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
            
    def pingbox(host, count):
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
           #tkMessageBox.showinfo("IFCONFIG",output)

    def digbox(host=serverip):
        clearFrame()
        #result=ping(serverip)
        command = "python3 dig.py "+host
        stdout = Popen(command, shell=True, stdout=PIPE).stdout
        output = stdout.read()
        for i in output.split("\n"):
            pinglabel = Label(main_frame, text=i, bg="black", fg="white")
            pinglabel.pack()
    
    def routebox(host=serverip):
       clearFrame()
       command = "python3 route.py "+host
       stdout = Popen(command, shell=True, stdout=PIPE).stdout
       output = stdout.read()  
       routelabel = Label(main_frame, text=output, bg="black", fg="white")
       routelabel.pack()
       
    def nmapbox(host=serverip):
       clearFrame()
       command = "python3 nmap.py "+host
       stdout = Popen(command, shell=True, stdout=PIPE).stdout
       output = stdout.read()  
       nmaplabel = Label(main_frame, text=output, bg="black", fg="white")
       nmaplabel.pack()
       
    def getdata(text_input,top1,funcname):
            data = text_input.get();
            top1.destroy()
            funcname(clientlist[int(data)-1]['ip'])  
             
    def pingcustom():
        top1 = tk.Tk()
        top1.title("Custom ping")
        canvas1 = tk.Canvas(top1, height=260, width=300)
        canvas1.pack() 
        data=[]
        f = open("clientdata.txt","w")
        f.write("Client\t  ip\tport\n")
        for i in range(len(clientlist)):
               #print(clientlist[i])
            f.write(str(i+1)+"          "+clientlist[i]['ip']+"     "+str(clientlist[i]['port'])+"\n")
            data.append(clientlist[i]['ip']+"   "+str(clientlist[i]['port'])+"\n")
        f.close()
      
        def getdataping(text_input,top1,funcname):
            data = text_input.get();
            num,count = data.split(",")
            top1.destroy()
            funcname(clientlist[int(num)-1]['ip'],count)

        f = open("clientdata.txt","r")
        cdata = f.read()
        P = Label(top1, text = cdata, font = ('times', 12,'bold'))
        f.close()
        P.place(x=2, y=10, width= 280, height=150)
        L = Label(top1, text = "Enter Client Number, number of pings", font = ('times', 12,'bold'))
        L.place(x=5, y=140, width= 280, height=40)
        text_input = Entry(top1, width=30)
        text_input.bind("<Return>", lambda i : getdataping(text_input,top1,pingbox))
        text_input.place(x=10, y=180,width=180, height=30)
        S = Label(top1, text = "Press enter to proceed", font = ('times', 11,'italic'))
        S.place(x=5, y=220, width= 180, height=20)
        top1.mainloop()
        
    def traceroutecustom():
        top1 = tk.Tk()
        top1.title("Custom traceroute")
        canvas1 = tk.Canvas(top1, height=260, width=300)
        canvas1.pack() 
        data=[]
        f = open("clientdata.txt","w")
        f.write("Client\t  ip\tport\n")
        for i in range(len(clientlist)):
            f.write(str(i+1)+"          "+clientlist[i]['ip']+"     "+str(clientlist[i]['port'])+"\n")
        f.close()
        f = open("clientdata.txt","r")
        cdata = f.read()
        P = Label(top1, text = cdata, font = ('times', 12,'bold'))
        f.close()
        P.place(x=2, y=10, width= 280, height=150)
        L = Label(top1, text = "Enter Client Number:", font = ('times', 12,'bold'))
        L.place(x=5, y=140, width= 280, height=40)
        text_input = Entry(top1, width=30)
        text_input.bind("<Return>", lambda i : getdata(text_input,top1,traceroutebox))
        text_input.place(x=10, y=180,width=180, height=30)
        S = Label(top1, text = "Press enter to proceed", font = ('times', 11,'italic'))
        S.place(x=5, y=220, width= 180, height=20)
        top1.mainloop()
        
    def nslookupcustom():
        top1 = tk.Tk()
        top1.title("Custom nslookup")
        canvas1 = tk.Canvas(top1, height=260, width=300)
        canvas1.pack() 
        data=[]
        f = open("clientdata.txt","w")
        f.write("Client\t  ip\tport\n")
        for i in range(len(clientlist)):
            f.write(str(i+1)+"          "+clientlist[i]['ip']+"     "+str(clientlist[i]['port'])+"\n")
        f.close()
        f = open("clientdata.txt","r")
        cdata = f.read()
        P = Label(top1, text = cdata, font = ('times', 12,'bold'))
        f.close()
        P.place(x=2, y=10, width= 280, height=150)
        L = Label(top1, text = "Enter Client Number:", font = ('times', 12,'bold'))
        L.place(x=5, y=140, width= 280, height=40)
        text_input = Entry(top1, width=30)
        text_input.bind("<Return>", lambda i : getdata(text_input,top1,nslookupbox))
        text_input.place(x=10, y=180,width=180, height=30)
        S = Label(top1, text = "Press enter to proceed", font = ('times', 11,'italic'))
        S.place(x=5, y=220, width= 180, height=20)
        top1.mainloop()
        
    def digcustom():
        top1 = tk.Tk()
        top1.title("Custom dig")
        canvas1 = tk.Canvas(top1, height=260, width=300)
        canvas1.pack() 
        data=[]
        f = open("clientdata.txt","w")
        f.write("Client\t  ip\tport\n")
        for i in range(len(clientlist)):
            f.write(str(i+1)+"          "+clientlist[i]['ip']+"     "+str(clientlist[i]['port'])+"\n")
        f.close()
        f = open("clientdata.txt","r")
        cdata = f.read()
        P = Label(top1, text = cdata, font = ('times', 12,'bold'))
        f.close()
        P.place(x=2, y=10, width= 280, height=150)
        L = Label(top1, text = "Enter Client Number :", font = ('times', 12,'bold'))
        L.place(x=5, y=140, width= 280, height=40)
        text_input = Entry(top1, width=30)
        text_input.bind("<Return>", lambda i : getdata(text_input,top1,digbox))
        text_input.place(x=10, y=180,width=180, height=30)
        S = Label(top1, text = "Press enter to proceed", font = ('times', 11,'italic'))
        S.place(x=5, y=220, width= 180, height=20)
        
    def nmapcustom():
        top1 = tk.Tk()
        top1.title("Custom nmap")
        canvas1 = tk.Canvas(top1, height=260, width=300)
        canvas1.pack() 
        data=[]
        f = open("clientdata.txt","w")
        f.write("Client\t  ip\tport\n")
        for i in range(len(clientlist)):
            f.write(str(i+1)+"          "+clientlist[i]['ip']+"     "+str(clientlist[i]['port'])+"\n")
        f.close()
        f = open("clientdata.txt","r")
        cdata = f.read()
        P = Label(top1, text = cdata, font = ('times', 12,'bold'))
        f.close()
        P.place(x=2, y=10, width= 280, height=150)
        L = Label(top1, text = "Enter Client Number :", font = ('times', 12,'bold'))
        L.place(x=5, y=140, width= 280, height=40)
        text_input = Entry(top1, width=30)
        text_input.bind("<Return>", lambda i : getdata(text_input,top1,nmapbox))
        text_input.place(x=10, y=180,width=180, height=30)
        S = Label(top1, text = "Press enter to proceed", font = ('times', 11,'italic'))
        S.place(x=5, y=220, width= 180, height=20)
        top1.mainloop()
        
    B=  tk.Button( top, text="ping",fg = "white", bg="black", font=('times', 16, 'bold'), cursor="hand2", command=pingcustom)
    B.place(relx=0, rely=0.04, relwidth=0.143, relheight=0.075)

           
    C=  tk.Button ( top, text="traceroute",  fg = "white", bg="black", font=('times', 16, 'bold'), cursor="hand2", command=traceroutecustom)
    C.place(relx=0.143, rely=0.04, relwidth=0.143, relheight=0.075)
          
    D=  tk.Button ( top, text="nslookup" , fg = "white", bg="black", font=('times', 16, 'bold'), cursor="hand2", command=nslookupcustom)
    D.place(relx=0.286, rely=0.04, relwidth=0.143, relheight=0.075)

    E = tk.Button(top, text ="ifconfig", fg = "white", bg="black",font=('times', 16, 'bold'),cursor = "hand2", command = ifconfigbox)
    E.place(relx=0.429, rely=0.04, relwidth=0.143, relheight=0.075)

           
    F=  tk.Button ( top, text="dig", relief=RAISED , fg = "white", bg="black", font=('times', 16, 'bold'), cursor="hand2", command=digcustom)
    F.place(relx=0.572, rely=0.04, relwidth=0.143, relheight=0.075,)
    
    G = tk.Button(top, text ="route", fg = "white", bg="black",font=('times', 16, 'bold'),command = routebox, cursor="hand2")
    G.place(relx=0.715, rely=0.04, relwidth=0.143, relheight=0.075,)
    
    H=  tk.Button(top, text ="nmap", fg = "white", bg="black",font=('times', 16, 'bold'),command = nmapcustom, cursor="hand2")
    H.place(relx=0.858, rely=0.04, relwidth=0.143, relheight=0.075,)

    top.mainloop()
    s.close() 
if __name__ == '__main__': 
    Main() 
