def get_sensor(readings: list, id: int) -> list:
    data = []
    for i in readings:
        if i['sensor_id'] == id:
            data.append(i['value'])
    return data
def download_data(url:str="192.168.6.142/readings")->list:
    req = requests.get(f"http://{url}")
    readings=req.json()['readings'][0]
    return readings
def smoothing(data:list,size_window:int=12):
    data_smooth=[]
    for i in range(0,len(data),size_window):
        data_in_window=data[i:i+size_window]
        average=sum(data_in_window)/size_window
        data_smooth.append(average)
    return data_smooth
