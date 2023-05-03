# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:09:15 2023

@author: awald
"""

import requests
import time
import psycopg2
import json
import pytz
import datetime 


    
    
ip = "128.173.94.88" # ip address that can be used to access the LF api from any network with internet connection

#machine = 'f170_D12827'
#machine = 'f170_D12903' # machine id for the Stratasys 1


# establishing connection to the locally installed PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="tjkdlsa89234f!"
)


### This bit of code is just for printing out variables so I can see what they're outputing. For testing purposes

response = requests.get('http://' + ip + "/api/deviceData/" + machine)
data = json.loads(response.text)

status = data["doorLockState"]["value"] #Status shows whether the printer is active or inactive
material_type = data["m1Material"]["value"] #Filament color

start_time = datetime.datetime.fromtimestamp(data["layers"]["timestamp"],
                                            pytz.timezone('US/Eastern'))
timestamp = datetime.datetime.fromtimestamp(data["s1TAct"]["timestamp"],
                                            pytz.timezone('US/Eastern'))
cur_layer = int(data["curLayer"]["value"])
total_layers = int(data["layers"]["value"])
job_progress = cur_layer/total_layers #this takes the current layer of the print / the total number of layers. Basically giving the job progress as a percent value
sup_act_temp = round(float(data["s1TAct"]["value"]), 1)
sup_com_temp = round(float(data["s1TCom"]["value"]), 1)
sup_temp_dif = sup_com_temp - sup_act_temp
# if status == "INACTIVE":
#     finish_time = timestamp




x_val = data["x1Act"]["value"]
print(x_val)

     


#print(start_time)
#print(timestamp)
#print(finish_time)


print(status)
# print(material_type)
# print(cur_layer)
# print(total_layers)
print(job_progress)
#print(sup_act_temp)

print("")
print("Run count:")
###



### This while loop actually loads variables into the database every 5 seconds

i = 0 #setting a counting variable to see how many times the loop is run

while machine == 'f170_D12903':
    response = requests.get('http://' + ip + "/api/deviceData/" + machine)
    data = json.loads(response.text)
    
    status = data["doorLockState"]["value"]
    material_type = data["m1Material"]["value"]
    
    start_time = datetime.datetime.fromtimestamp(data["layers"]["timestamp"],
                                                pytz.timezone('US/Eastern'))
    timestamp = datetime.datetime.fromtimestamp(data["s1TAct"]["timestamp"],
                                                pytz.timezone('US/Eastern'))
    cur_layer = int(data["curLayer"]["value"])
    total_layers = int(data["layers"]["value"])
    job_progress = cur_layer/total_layers #this takes the current layer of the print / the total number of layers. Basically giving the job progress as a percent value
    
    sup_act_temp = round(float(data["s1TAct"]["value"]), 1)
    sup_com_temp = round(float(data["s1TCom"]["value"]), 1)
    sup_temp_dif = sup_com_temp - sup_act_temp

    
    
    i = i+1
    x_val = data["x1Act"]["value"]
    #print(x_val)
    
    print(i)
    # print("support temps:")
    
    # print(sup_act_temp)
    # print(sup_com_temp)
    # print(sup_temp_dif)
    # print("")
    
    cur = conn.cursor()
    cur.execute("INSERT INTO lf.strata_1 (timestamp, status, material_type, temp, job_progress, start_time) VALUES (%s, %s, %s, %s, %s, %s)", (timestamp, status, material_type, sup_act_temp, job_progress, start_time,))
    # Commit the changes
    conn.commit()   
    
    time.sleep(3)
    
###
