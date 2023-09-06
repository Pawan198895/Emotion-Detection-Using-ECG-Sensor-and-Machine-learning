import Adafruit_ADS1x15
import serial
import time
import sys
import requests
import urlopen
import urllib
rate = [0]*10
amp = 100
GAIN = 2/3  
curState = 0
stateChanged = 0

ser = serial.Serial ("/dev/ttyS0", 9600)

User1API ='D3RKF00BXI4547VH'                                                          

#URL where we will send the data, Don't change it
baseURL1 = 'https://api.thingspeak.com/update?api_key=%s'%User1API

def send_to_prcessing1(data1):   # for tempreture Sensor
       ser.write(str(data1).encode())
       

def ECG():
        adc = Adafruit_ADS1x15.ADS1015()
        while True:
                Signal1 = adc.read_adc(0, gain=GAIN)   
                send_to_prcessing1(Signal1)
                
                
                if (Signal1 == 1649)or(Signal1 == 1648)or(Signal1 == 1650)or(Signal1 == 1647):
                       Signal1 = 0
                       print("Pulse value:" + str(Signal1))
                print("Pulse value:" + str(Signal1))
                conn = baseURL1 +'&field1=%s' % (Signal1)
                request = urllib.request.Request(conn)
                responce = urllib.request.urlopen(request)
                responce.close()
                time.sleep(0.5)
                
                                    
ECG()
