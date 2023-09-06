from subprocess import call
import tkinter as tk
import tkinter as tK
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

root = tk.Tk()
root.title("Prediction")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++


 # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Prediction", font=('times', 35,' bold '), height=1, width=65,bg="violet Red",fg="Black")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++
data = pd.read_csv(r"/home/pi/22E9547-ECG_emotion_detection/ECG_New/training.csv")



data = data.dropna()

le = LabelEncoder()



def Data_Preprocessing():
    data = pd.read_csv(r"/home/pi/22E9547-ECG_emotion_detection/ECG_New/training.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['Pulse_value'] = le.fit_transform(data['Pulse_value'])
    
    
    
   
    
    
   
  

    """Feature Selection => Manual"""
    x = data.drop(['label'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['label']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

    

    load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, background="green",
                    foreground="white", text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
    load.place(x=213, y=85)


def Model_Training():
    data = pd.read_csv(r"/home/pi/22E9547-ECG_emotion_detection/ECG_New/training.csv")
    data.head()

    data = data.dropna()


    """One Hot Encoding"""

    le = LabelEncoder()

    data['Pulse_value'] = le.fit_transform(data['Pulse_value'])
    
   
    
   
  
    

    """Feature Selection => Manual"""
    x = data.drop(['label'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['label']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=10)

    # from sklearn.ensemble  import RandomForestRegressor
    # svcclassifier = RandomForestRegressor()
    # svcclassifier.fit(x_train, y_train)
    # y_pred = svcclassifier.predict(x_test)
    
    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)
    
    # from sklearn.tree import DecisionTreeClassifier
    # svcclassifier = DecisionTreeClassifier()
    # svcclassifier.fit(x_train, y_train)
    # y_pred = svcclassifier.predict(x_test)
    
    

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    
    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as svm.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"svm.joblib")
    print("Model saved as svm.joblib")



def call_file():
    import Check_Prediction
    Check_Prediction.Train()


def window():
    root.destroy()

# button2 = tk.Button(root, foreground="white", background="Orange", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
# button2.place(x=20, y=90)

button3 = tk.Button(root, foreground="white", background="Orange", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model Training", command=Model_Training, width=15, height=2)
button3.place(x=20, y=170)

button4 = tk.Button(root, foreground="white", background="Orange", font=("Tempus Sans ITC", 14, "bold"),
                    text=" Prediction", command=call_file, width=30, height=2)
button4.place(x=20, y=250)
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=20, y=330)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
