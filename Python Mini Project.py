from tkinter import *
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import csv
import numpy as np
import scipy.interpolate
from matplotlib_scalebar.scalebar import ScaleBar
x=[]
y=[]
z=[]
x1=[]
y1=[]
root =Tk()

with open('csvfile1.txt', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
            x.append(float(row[0]))
            y.append(float(row[1]))
            z.append(float(row[2]))
plt.title('Topographic Map Sample')

plt.xlabel('Easting')
plt.ylabel('Northing')
scalebar = ScaleBar(0.8,location='lower center') # 1 pixel = 100 meter
plt.gca().add_artist(scalebar)
def NewFile():
         window = tk.Toplevel(root)
         print("New File")
def OpenFile():
    name=askopenfilename()
    print(name)
def About():
    print("This is a simple example of a menu")
def CreateContour():
        p=[]
        q=[]
        r=[]
        xmin=424235.258
        xmax=424635.258
        ymin=3055188.245
        ymax=3055696.969
        n=20
        with open('csvfile1.txt', 'r') as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                    p.append(float(row[0]))
                    q.append(float(row[1]))
                    r.append(float(row[2]))

        xi=np.linspace(xmin,xmax,n)
        yi=np.linspace(ymin,ymax,n)
        zi=scipy.interpolate.griddata((p,q),r,(xi[None,:],yi[:,None]),method='cubic')
        cs=plt.contour(xi,yi,zi,colors=['#A0A0A0'])
        plt.clabel(cs, fmt = '%.0f', inline = True , colors=['#ff0000'])
        
        plt.axis('off')
    
        
        print("contour Created")
        plt.show()


def InsertPoint():
    cpX=[]
    cpY=[]
    EPx=[]
    EPy=[]
    with open('csvfile1.txt', 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=',')
        for row in plots:
            if row[3]=="CP":
                cpX.append(float(row[0]))
                cpY.append(float(row[1]))
                control_points=plt.scatter(cpX,cpY,marker="^",s=200,color="black",)
        
            elif row[3]=="EP":
                EPx.append(float(row[0]))
                EPy.append(float(row[1]))
                Electpole=plt.scatter(EPx,EPy,marker="o",s=150,color="black")
            else:
                
                plt.axis('off')
                plt.scatter(x,y)
                
                     
                     
                
                   

            

    
    
    

    plt.legend([Electpole,control_points],["Electrictic Pole","Control Point"],loc='best')
    plt.show()
    
    print("point Inserted")

            
def JoinFeature():
    def feature():
        s=v.get()
        if s=="road right":
            def roadRight():
                x2=[]
                y2=[]
                s1=v1.get()
                s2=v2.get()
                s3=v3.get()
                s4=v4.get()
                remarks=[s1,s2,s3,s4]
                with open('csvfile1.txt', 'r') as csvfile:
                    plots= csv.reader(csvfile, delimiter=',')
                
                    for row in plots:
                        for i in range(0,4):
                            if row[3]==remarks[i]:
                                x2.append(float(row[0]))
                                y2.append(float(row[1]))
                print(x2,y2)
                    
                plt.plot(x2,y2)
               
                scalebar = ScaleBar(0.02) # 1 pixel = 100 meter
                plt.gca().add_artist(scalebar)
                plt.legend(plt.plot(x2,y2),["Road Right"],loc='lower right')
                plt.axis('off')
                plt.show()              

                    
            v1 = StringVar()
            v2 = StringVar()
            v3 = StringVar()
            v4 = StringVar()
            e2=Entry(root, textvariable=v1)
            e2.grid(row=3,column=1)
      
            e3=Entry(root, textvariable=v2)
            e3.grid(row=4,column=1)
          
            e4=Entry(root, textvariable=v3)
            e4.grid(row=5,column=1)

            Label(root,text="Input the remarks of road Right").grid(row=3)
            e5=Entry(root, textvariable=v4)
            e5.grid(row=6,column=1)
            
            Button(root,text="submit",command=roadRight).grid(row=4)
            
        
        if s=="road left":
            def roadLeft():
                x2=[]
                y2=[]
                
                s1=v1.get()
                s2=v2.get()
                s3=v3.get()
                s4=v4.get()
                remarks=[s1,s2,s3,s4]
                with open('csvfile1.txt', 'r') as csvfile:
                    plots= csv.reader(csvfile, delimiter=',')
                
                    for row in plots:
                        for i in range(0,4):
                            if row[3]==remarks[i]:
                                x2.append(float(row[0]))
                                y2.append(float(row[1]))
                print(x2,y2)
                    
                plt.plot(x2,y2)
                plt.legend(plt.plot(x2,y2),["Road Left"],loc='upper right')
                plt.axis('off')
                plt.show()              
            
            v1 = StringVar()
            v2 = StringVar()
            v3 = StringVar()
            v4 = StringVar()
            e2=Entry(root, textvariable=v1)
            e2.grid(row=3,column=1)
      
            e3=Entry(root, textvariable=v2)
            e3.grid(row=4,column=1)
          
            e4=Entry(root, textvariable=v3)
            e4.grid(row=5,column=1)

            Label(root,text="Input the remarks of road left").grid(row=3)
            e5=Entry(root, textvariable=v4)
            e5.grid(row=6,column=1)
            
            Button(root,text="submit",command=roadLeft).grid(row=4)
            
        if s=="house":
            def house():
                x2=[]
                y2=[]
               
                s1=v1.get()
                s2=v2.get()
                s3=v3.get()
                s4=v4.get()
                remarks=[s1,s2,s3,s4]
                with open('csvfile1.txt', 'r') as csvfile:
                    plots= csv.reader(csvfile, delimiter=',')
                
                    for row in plots:
                        for i in range(0,4):
                            if row[3]==remarks[i]:
                                x2.append(float(row[0]))
                                y2.append(float(row[1]))
                    
                with open('csvfile1.txt', 'r') as csvfile:
                    plots= csv.reader(csvfile, delimiter=',')
                    for row in plots:
                        if row[3]==s1:
                            x2.append(float(row[0]))
                            y2.append(float(row[1]))
                print(x2,y2)
                    
                plt.plot(x2,y2,)
                plt.fill(x2,y2,color='black',alpha=0.3,hatch='|')
                plt.legend(plt.plot(x2,y2),["house"],loc='lower right')
                
                plt.axis('off')
                plt.show()
                    
               
                
                
                
            
            v1 = StringVar()
            v2 = StringVar()
            v3 = StringVar()
            v4 = StringVar()
            
            e2=Entry(root, textvariable=v1)
            e2.grid(row=3,column=1)
      
            e3=Entry(root, textvariable=v2)
            e3.grid(row=4,column=1)
          
            e4=Entry(root, textvariable=v3)
            e4.grid(row=5,column=1)

            Label(root,text="Input the remarks of houses").grid(row=3)
            e5=Entry(root, textvariable=v4)
            e5.grid(row=6,column=1)
            
            Button(root,text="submit",command=house).grid(row=4)
           
        e1.delete(0,END)
        e1.insert(0,"")
    v = StringVar()
    Label(root,text="Input the feature to join").grid(row=1)
    e1=Entry(root, textvariable=v)
    e1.grid(row=1,column=1)
    Button(root,text="submit",command=feature).grid(row=2)        
    print("House Joined")
def AddLegend():
    print("Legend Added")


    


menu =Menu(root)
root.config(menu=menu)
filemenu =Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

Mapmenu = Menu(menu)
menu.add_cascade(label="Plot", menu=Mapmenu)
Mapmenu.add_command(label="Insert Points", command=InsertPoint)
Mapmenu.add_command(label="Create Contour", command=CreateContour)
Mapmenu.add_command(label="Join Feature", command=JoinFeature)
mainloop()

