import requests
import time
import psycopg2
import json
import pytz
import datetime 
    
ip = "128.173.94.88"

machine = "UR5"

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Drillers03"
)

while machine == "UR5":
    response = requests.get('http://' + ip + "/api/deviceData/" + machine)
    data = json.loads(response.text)
   
    ur5_timestamp = datetime.datetime.fromtimestamp(data['x']['timestamp'], 
                                                 pytz.timezone('US/Eastern'))
    ur5_x_coordinate = data['x']['value']
    ur5_y_coordinate = data['y']['value']
    ur5_z_coordinate = data['y']['value']
    ur5_rx_coordinate = data['rx']['value']
    ur5_ry_coordinate = data['ry']['value']
    ur5_rz_coordinate = data['rz']['value']
            
    cur = conn.cursor()
    cur.execute("INSERT INTO lf.ur5 (timestamp, x_coordinate, y_coordinate, z_coordinate, rx_coordinate, ry_coordinate, rz_coordinate) VALUES (%s, %s, %s, %s, %s, %s, %s)", (ur5_timestamp, ur5_x_coordinate, ur5_y_coordinate, ur5_z_coordinate, ur5_rx_coordinate, ur5_ry_coordinate, ur5_rz_coordinate,))
    # Commit the changes
    conn.commit()   
    
    print(ur5_timestamp)
        
    time.sleep(1)
 
    

    


