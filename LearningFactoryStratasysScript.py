import requests
import time
import psycopg2
import json
import pytz
import datetime 
    
ip = "128.173.94.88"

machine = "f170_D12827" 

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Drillers03"
)

while machine == 'f170_D12827':
    response = requests.get('http://' + ip + "/api/deviceData/" + machine)
    data = json.loads(response.text)
    
    strata1_timestamp = datetime.datetime.fromtimestamp(data["s1TAct"]["timestamp"],
                                            pytz.timezone('US/Eastern'))
    strata1_status = data["doorLockState"]["value"]
    strata1_material_type = data["m1Material"]["value"]
    
    strata1_cur_layer = int(data["curLayer"]["value"])
    strata1_total_layers = int(data["layers"]["value"])
    strata1_temperature = data["s1TAct"]["value"]
    strata1_lower_temp_cl = 80
    strata1_upper_temp_cl = 250
    strata1_job_progress = strata1_cur_layer/strata1_total_layers
    
    cur = conn.cursor()
    cur.execute("INSERT INTO lf.strata1 (timestamp, status, material_type, temperature, lower_temp_cl, upper_temp_cl, job_progress) VALUES (%s, %s, %s, %s, %s, %s, %s)", (strata1_timestamp, strata1_status, strata1_material_type, strata1_temperature, strata1_lower_temp_cl, strata1_upper_temp_cl, strata1_job_progress,))
    # Commit the changes
    conn.commit()   
    
    print(strata1_timestamp)
    
    time.sleep(1)
    








