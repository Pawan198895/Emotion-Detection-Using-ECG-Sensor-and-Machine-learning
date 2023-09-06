from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd
    from tkinter import ttk
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    root.geometry("800x850+250+5")
    root.title(" Prediction")
    root.configure(background="LightSkyBlue")
    
    Pulse_value = tk.IntVar()
   
    
    
    
    
    
    #===================================================================================================================



    def Detect():
        e1=Pulse_value.get()
        print(e1)
        
        
        
      
        
        
        
    
        
        #########################################################################################
        
        import joblib
        from joblib import dump , load
        a1=load('/home/pi/22E9547-ECG_emotion_detection/ECG_New/svm.joblib')
        v= a1.predict([[e1]])
        print(v)
    
        if v[0]=='happy':
           print("happy")
           yes = tk.Label(root,text="happy",background="Green",foreground="white",font=('times', 20, ' bold '),width=20)
           yes.place(x=600,y=600)
           
        
           
        else :
            print("sad")
            yes = tk.Label(root,text="sad",background="Green",foreground="white",font=('times', 20, ' bold '),width=20)
            yes.place(x=600,y=600)
           
      
    l1=tk.Label(root,text="Pulse value",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l1.place(x=5,y=30)
    Pulse_value=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Pulse_value)
    Pulse_value.place(x=500,y=30)      
      

    

   

   
    
    
   
    
   
    
    button1 = tk.Button(root, foreground="white", background="red",text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=600,y=400)


    root.mainloop()

Train()
