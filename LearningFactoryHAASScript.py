import requests
import time
import psycopg2
import json
import pytz
import datetime 
    
ip = "128.173.94.88"

machine = "HAASData"

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Drillers03"
)

while machine == "HAASData":
    response = requests.get('http://' + ip + "/api/deviceData/" + machine)
    data = json.loads(response.text)
    
    haas_timestamp = datetime.datetime.fromtimestamp(data['machine_x']['timestamp'],
                                                  pytz.timezone('US/Eastern'))
    coolant_level = data['coolant_level']['value']
    spindle_rpm = data['spindle_rpm']['value']
    lower_spindle_cl = 10
    upper_spindle_cl = 90
    haas_x_coordinate = data['machine_x']['value']
    haas_y_coordinate = data['machine_y']['value']
    haas_z_coordinate = data['machine_z']['value']
    haas_a_coordinate = data['machine_a']['value']
    haas_b_coordinate = data['machine_b']['value']
    haas_x_work = data['work_x']['value']
    haas_y_work = data['work_y']['value']
    haas_z_work = data['work_z']['value']
    haas_a_work = data['work_a']['value']
    haas_b_work = data['work_b']['value']

    cur = conn.cursor()
    cur.execute("INSERT INTO lf.haas (timestamp, coolant_level, spindle_rpm, lower_spindle_cl,upper_spindle_cl, x_coordinate, y_coordinate, z_coordinate, a_coordinate, b_coordinate, x_work, y_work, z_work, a_work, b_work) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (haas_timestamp, coolant_level, spindle_rpm, lower_spindle_cl, upper_spindle_cl, haas_x_coordinate, haas_y_coordinate, haas_z_coordinate, haas_a_coordinate, haas_b_coordinate, haas_x_work, haas_y_work, haas_z_work, haas_a_work, haas_b_work,))
    # Commit the changes
    conn.commit()   
    
    print(haas_timestamp)
    
    time.sleep(1)
