# Unit 2 Project: A Distributed Weather Station for ISAK
![b93685101c1460fc](https://user-images.githubusercontent.com/100017195/202971624-5e583f4a-3fc9-4300-b590-80c0c5aa6fce.jpg)

## Criteria A: Planning

## Problem definition

Kris san is a parent of an ISAK student and is worried about the safety of the humidity and temperature levels on the ISAK campus. Because she is a busy businesswoman travelling abroad, she would like for someone on campus to measure and store both the humidity and temperature levels in a dormitory and another location on campus outside of the dormitory for a minimum of 48 hours. With the data collected, she would like to confirm that the humidity and temperature levels on campus are safe for the health of her daughter and a prediction of humidity and temperature for the subsequent 12 hours. 

## Success Criteria

1. The solution provides a visual representation of the Humidity and Temperature values inside a dormitory (Local) and outside the house (Remote) for a period of minimum 48 hours. 
1. ```[HL]``` The local variables will be measure using a set of 4 sensors around the dormitory.
2. The solution provides a mathematical modelling for the Humidity and Temperature levels for each Local and Remote locations. ```(SL: linear model)```, ```(HL: non-lineal model)```
3. The solution provides a comparative analysis for the Humidity and Temperature levels for each Local and Remote locations including mean, standad deviation, minimum, maximum, and median.
4. ```(SL)```The Local samples are stored in a csv file and ```(HL)``` posted to the remote server.
5. Create a prediction the subsequent 12 hours for both temperature and humidity.
6. A poster summarizing the visual representations, model and analysis is created and communicated.


## Design Statement
We will design and make a poster for the client who is Kris san. The poster will include the system diagram and the visual representation and model of humidity and temperature in an ISAK room and an ISAK remote indoor location for 48 hours, and a prediction of a subsquent 12 hours. It will also present the health consequences for the humidity and temperature levels. This is achieved with the software Python in a Raspberry Pi. It will take approximately 1 month to make and will be evaluated according to the 6 criteria listed below.

## Rationale for Proposed Solution
Considering the client requirements an adequate solution includes a low cost sensing device for humidity and temperature and a custom data script that process and anaysis the samples acquired. For a low cost sensing device an adequate alternative is the DHT11 sensor[^1] which is offered online for less than 5 USD and provides adequare precision and range for the client requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the DHT22, AHT20 or the AM2301B [^2] have higher specifications, however the DHT11 uses a simple serial communication (SPI) rather than more eleborated protocols such as the I2C used by the alternatives. For the range, precision and accuracy required in this applicaiton the DHT11 provides the best compromise. Connecting the DHT11 sensor to a computer requires a device that provides a Serial Port communication. A cheap and often used alternative for prototyping is the Arduino UNO microcontroller [^3]. "Arduino is an open-source electronics platform based on easy-to-use hardware and software"[^4]. In additon to the low cost of the Arduino (< 6USD), this devide is programable and expandable[^1]. Other alternatives include diffeerent versions of the original Arduino but their size and price make them a less adequate solution.

Considering the budgetary constrains of the client and the hardware requirements, the software tool that I proposed for this solution is Python. Python is open source, it is mature and supported in mutiple platforms (platform-independent) including macOS, Windows, Linux and can also be used to program the Arduino microprocessor [^5][^6]. In comparison to the alternative C or C++, which share similar features, Python is a High level programming language (HLL) with high abstraction [^7]. For example, memory management is automatic in Python whereas it is responsability of the C/C++ developer to allocate and free up memory [^7], this could result in faster applications but also memory problems. In addition a HLL language will allow me and future developers extend the solution or solve issues proptly.

# Criteria B: Design

## System Diagram
![sysdim_hl](https://user-images.githubusercontent.com/100017195/202972155-a515b55d-e2e5-434d-97ce-878c8630040b.jpg)

**Fig.1** shows the system diagram for the proposed solution (**HL**). The indoor variables will be measured using a Raspberry PI and four DHT11 sensors located inside a room. Four sensors are used to determine more precisely the physical values and include measurement uncertainty. The outdoor variables will be requested to the remote server using a GET request to the API of the server at ```192.168.6.147/readings```. The local values are stored in a CSV database locally and POST to the server using the API and TOKEN authentication. A laptop computer is used for remotely controlling the local Rasberry Pi using a Dekptop sharing application (VNC Viewer). Data from the local raspberry is downloaded to the laptop for analysis and processing.

## Flow Diagram 1 - Main File
![IMG_0504](https://user-images.githubusercontent.com/100017195/205495755-11bcf00d-d1df-4470-b2fc-e9f43b84790f.jpeg)
![IMG_0505](https://user-images.githubusercontent.com/100017195/205495760-5109719e-7b78-419b-9498-d0ae682b3d31.jpeg)

## Flow Diagram 2 - Server Creation
![Untitled-19](https://user-images.githubusercontent.com/111893043/206170522-88960069-42a2-4ed3-b9d1-0e4238888a66.jpg)
![Untitled-20 3](https://user-images.githubusercontent.com/111893043/206171086-e86bfb21-3013-4bef-b45e-55e83ae545d8.jpg)

## Flow Diagram 3 - MVP
![Untitled-21](https://user-images.githubusercontent.com/111893043/206180312-15704e70-6f39-4dbe-98e7-e79ce5351f95.jpg)




## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Write the problem context                        | Have a clear description of the problem.         | 20 mins                 | Nov 21         | A
| 2       | Create bill of materials                        | Compile all necessary materials.         | 20 mins                 | Nov 21         | A
| 3       | Complete Design Statement                        | A clear outline of the final goal of the project and components that need to be completed.         | 20 mins                 | Nov 21         | A
| 4       | Collect materials and sign scope of work                        | Aquire all materials necessary in order to create weather station in dormitory and sign out materials with intention of only creating the weather station for the client.         | 15 mins                 | Nov 25         | A
| 5       | Download necessary libraries and applications.                        | Prepare computer to receive information from sensor and preparation for future coding.         | 20 mins                 | Nov 25         | A
| 6       | Connect raspberry pi to computer and test run of sensors.                        | Make sure sensors and raspberry pi are working properly. Complete preliminary construction of weather station         | 90 mins                 | Nov 29         | B
| 7       | Create MVP (Minimum Viable Product).                        | Test basic product before adding features to make sure the basic structure and features of product works properly before moving towards final, complete product.         | 60 mins                 | Nov 30         | C
| 8       | Register user to server and obtain access code.                        | Create a user with a secure username and password in order to access server. Obtain access code in order to be able to log in and post to server.        | 60 mins                 | Dec 02         | C
| 9       | Create code to take temperature and humidity data from DHT sensors.                        | Be able to obtain data from DHT sensors and view them on laptop.        | 30 mins                 | Dec 02         | C
| 10       | Set up cron tab.                        | In order to have DHT sensors send data to computer at regular interval of 5 minutes.        | 30 mins                 | Dec 02         | C
| 11       | Create code that saves temperature and humidity data to csv and send to server.                        | Humidity and temperature data sent to server every five minutes. Humidity and temperature data saved to designated csv files every 5 minutes.        | 60 mins                 | Dec 02         | C
| 12       | Run code for 48 hours in order to collect temperature and humidity data in R3-10A.                        | Obtain humidity and temperature data from R3-10A for 48 hours at 5 minute intervals.        | 48 hours                 | Dec 02         | C
| 13       | Create 3 flow diagrams of aspects of code.                        | In order to clearly display in order to clearly display the algorithms used in the product and show how the product was developed.        | xxx mins                 | Dec 05-xx         | B
| 14       | Research safe humidity and temperature levels.                        | Determine whether humidity and temperature levels on the UWC ISAK campusa are healthy/safe or unhealthy/unsafe.        | 20 mins                 | Dec 05         | D
| 15       | Coding the code for getting data from school sensors.                        | In order to retrieve posted data from the server to apply to future codes and models.        | 45 mins                 | Dec 06         | C
| 16       | Adding codes of mvp, server initialization, and getting data from school sensor.                        | To make sure product development information is updated to Criteria C. Displays the details from how we created our product.        | 20 mins                 | Dec 06         | C
| 17       | Coding the graphings of school and room temperature and humidity datas. | To prepare scatter plot graphs with non-linear best fit functions        | 60 mins                 | Dec 09         | C

## Test Plan
| Software Test Type | Input | Process | Planned Output  |
|------|-------------|----------|---------|
| Integration Testing | Raspberry Pi and VNC Viewer | 1. Download vnc viewer. 2. Input raspberry pi address into vnc viewer. 3. Access raspberry pi through VNC viewer using username and password. | VNC viewer will authenticate username and password and be able to connect to raspberry pi remotely. |
| Unit Testing | Code to receive information from DHT sensor | 1. Run code. 2. Wait for output from DHT sensor. | Confirm that DHT sensor is functioning properly.|
| Performance Testing | Code to receive humidity and temperature data from DHT sensors | 1. Run code. 2. Measure response time. | Code will run and data will be collected and printed on the computer monitor within 5 seconds.|
| Unit Testing | Code for appending humidity and temperature data to csv file | 1. Run code. | A new csv file will be created for humidity and temperature (humidity.csv and temperatures.csv). Data from DHT sensors will be appended to csv files. |
| Integration Testing | Crontab and VNC Viewer | 1. Run code. 2. Wait to see code runs every 5 minutes and humidity and temperature data is appended to csv file every 5 minutes. | Temperature and humidity data is appended to designated csv file every 5 minutes. Information appended includes data from each of the four sensors, average of data and date and time that data is appended to file.|


# Criteria C: Development

## Existing tools:
| Software/development tools | coding structure tools | Libraries    |
|----------------------------|------------------------|--------------|
| Python/Pycharm             | for loops              | datetime     |
| VNC viewer                 | API requests           | requests     |
|                            |                        | csv          |
|                            |                        | Adafruit_DHT |

## List of techniques used
| Technique |
|-----------|
| Posting to a remote server with server API. |
| Retrieving data from a remote server with server API and requests library. |
| For loops in order to run code under certain conditions. For example, to get readings for multiple DHT11 sensors with one for loop of code. Utilizing a for loop is more efficient than creating a code for each sensor separately. |
| Creating lists (in order to save data from DHT11 sensors by temperature and humidity). |
| Creating CSV files (in order to save data from DHT11 sensors by temperature and humidity). |

## Computational Thinkings

Algorithms: In the initial code and MVP, we utilized a while loop in order for the code to loop and take readings at specific intervals. This was inefficient because the task is to get readings at a 5 minute interval for 48 hours, but with a while loop, if the computer was closed or the server lost connection, the code would stop running and therefore stop taking the necessary readings. In order to avoid having to keep the computer and VNC application running actively for 48 hours, we utilized a simple tool that can fix this problem, a crontab task through the raspberry pi terminal in order to create a task that would run the code every five minutes. 

Code before:
```.py
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor failure, check wiring")
    time.sleep(3);
```
Crontab utilization:
The utilization of crontab, as shown below, allows the code to run every 5 minutes (therefore taking readings and posting them to the server consistently at the aforementioned interval) until the crontab is deleted. 

![Screen Shot 2022-12-06 at 14 14 20 Small](https://user-images.githubusercontent.com/111893043/205823869-357b16d5-a115-4512-93ab-38a5255afbe6.jpeg)

## Code development
Below are the developments of the Python code being programmed for the project.

### MVP-Minimum Viable Product
We created a MVP as a prototype of how the temperature and humidity data can be measured and collected. The MVP runs on Python code on Raspberry Pi which is connected to one DHT sensor. The code allows the Raspberry Pi to read one set of temperature and humidity data from the DHT sensor, and display the data as an output in the terminal. For more details, please refer to the Python code below.

Link to MVP video: https://www.youtube.com/watch?v=iYga3GLq-A4

```.py
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
PINS=[23, 18, 15, 14]


for pin in PINS:
   humidity, temperature = None, None
   while humidity is None or temperature is None:
       humidity, temperature= Adafruit_DHT.read_retry(DHT_SENSOR, pin)
   print(f"PIN No. {pin}: ""Humidity: {} %, Temperature: {} C".format(humidity, temperature))
```

### Server initialization
Logging in, registering and creating 8 sensors in the server. Code is as below:
```.py
import requests
# username+password
user={"username":"Lyn_Kris","password":"R310BestHouse"}

# register
req=requests.post('http://192.168.6.142/register',json=user)
print(req.json())

# login
req=requests.post('http://192.168.6.142/login',json=user)
access_token = req.json()['access_token']
print(f"token: {access_token}")

# add temperature sensor 1
auth = {'Authorization':f"Bearer {access_token}"}
new_sensor = {"type": "Temperature", "location": "R3-10A", "name": "temp_lyn_kris_1","unit":"C"}
r= requests.post('http://192.168.6.142/sensor/new',json=new_sensor, headers = auth)
print(r.json())
# add temperature sensor 2
new_sensor = {"type": "Temperature", "location": "R3-10A", "name": "temp_lyn_kris_2","unit":"C"}
r= requests.post('http://192.168.6.142/sensor/new',json=new_sensor, headers = auth)
print(r.json())
# add temperature sensor 3
new_sensor = {"type": "Temperature", "location": "R3-10A", "name": "temp_lyn_kris_3","unit":"C"}
r= requests.post('http://192.168.6.142/sensor/new',json=new_sensor, headers = auth)
print(r.json())
# add temperature sensor 4
new_sensor = {"type": "Temperature", "location": "R3-10A", "name": "temp_lyn_kris_4","unit":"C"}
r= requests.post('http://192.168.6.142/sensor/new',json=new_sensor, headers = auth)
print(r.json())

# add humidity sensor 1
new_sensor = {"type": "Humidity", "location": "R3-10A", "name": "hum_lyn_kris_1","unit":"%"}
r= requests.post('http://192.168.6.142/sensor/new',json=new_sensor, headers = auth)
print(r.json())
# add humidity sensor 2
new_sensor = {"type": "Humidity", "location": "R3-10A", "name": "hum_lyn_kris_2","unit":"%"}
r= requests.post('http://192.168.6.142/sensor/new',json=new_sensor, headers = auth)
print(r.json())
# add humidity sensor 3
new_sensor = {"type": "Humidity", "location": "R3-10A", "name": "hum_lyn_kris_3","unit":"%"}
r= requests.post('http://192.168.6.142/sensor/new',json=new_sensor, headers = auth)
print(r.json())
# add humidity sensor 4
new_sensor = {"type": "Humidity", "location": "R3-10A", "name": "hum_lyn_kris_4","unit":"%"}
r= requests.post('http://192.168.6.142/sensor/new',json=new_sensor, headers = auth)
print(r.json())
```

### Get data from school server
We need to get the temperature and humidity datas that the sensors at schools collected from the server and store them in csv files. Below is the code:

```.py
# This program gets the time and value of humidity/temperature and stores them in separate csv files.
import requests
import csv

req=requests.get('http://192.168.6.142/readings')
readings=req.json()['readings']
readings=readings[0]

for i in readings:
    if i['sensor_id']==4: # humidity sensor
        with open("school_humidity.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([i['datetime'],i['value']])

for i in readings:
    if i['sensor_id']==5: # temperature sensor
        with open("school_temperature.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([i['datetime'],i['value']])
```

### Graph plotting
This program gets data from the database files and plotts the datas into separate scatter plots. In addition, it also calculates and plots the non-linear lines of best fit. Please refer to the code and graphs plotted as below:

```.py
# this program plots the data from the csv files
import matplotlib.pyplot as plt
import numpy as np

with open("room_hum.csv", "r") as file:
    room_hum_data = file.readlines()
with open("room_temp.csv", "r") as file:
    room_temp_data = file.readlines()
with open("school_humidity.csv", "r") as file:
    school_hum_data = file.readlines()
with open("school_temperature.csv", "r") as file:
    school_temp_data = file.readlines()

fig_width= 15
fig_height= 25

# plot room temperature
room_temp=[]
index=[]
count=1
for temp_data in room_temp_data:
    temp_datas = temp_data.strip()
    values = temp_datas.split(",")
    room_temp.append(float(values[4]))
    index.append(count)
    count+=1
# calculate best fit 4 degree polynomial
p = np.poly1d(np.polyfit(index, room_temp, 5))

#start plotting graph
plt.figure(figsize=(fig_width,fig_height))
plt.subplot(4,1,1)
plt.scatter(index,room_temp)
plt.plot(index,p(index), color="red")
plt.title("Room Temperature")
plt.ylabel("Average Temperature")
plt.xlabel("Measures")


# plot room humidity
room_hum=[]
index=[]
count=1
for hum_data in room_hum_data:
    hum_datas = hum_data.strip()
    values = hum_datas.split(",")
    room_hum.append(float(values[4]))
    index.append(count)
    count+=1

p = np.poly1d(np.polyfit(index, room_hum, 5))

#size of graph
plt.subplot(4,1,2)
plt.scatter(index,room_hum)
plt.plot(index,p(index), color="red")
plt.title("Room Humidity")
plt.ylabel("Average Humidity")
plt.xlabel("Measures")


# plot school temperature
school_temp=[]
index=[]
count=1
for school_temp_datas in school_temp_data:
    school_temp_datas = school_temp_datas.strip()
    values = school_temp_datas.split(",")
    school_temp.append(float(values[1]))
    index.append(count)
    count+=1
p = np.poly1d(np.polyfit(index, school_temp, 5))
plt.subplot(4,1,3)
plt.scatter(index,school_temp)
plt.plot(index,p(index), color="red")
plt.title("School Temperature")
plt.ylabel("Average Temperature")
plt.xlabel("Measures")

# plot school humidity
school_hum=[]
index=[]
count=1
for school_hum_datas in school_hum_data:
    school_hum_datas = school_hum_datas.strip()
    values = school_hum_datas.split(",")
    school_hum.append(float(values[1]))
    index.append(count)
    count+=1
p = np.poly1d(np.polyfit(index, school_hum, 5))
plt.subplot(4,1,4)
plt.scatter(index,school_hum)
plt.plot(index,p(index), color="red")
plt.title("School Humidity")
plt.ylabel("Average Humidity")
plt.xlabel("Measures")

plt.show()
```
![myplot](https://user-images.githubusercontent.com/100017195/206483996-6ab5145b-8855-4ff8-bcb0-0cdb939da3f4.jpeg)



# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration

[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
[^3]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
[^4]:Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.  
[^5]:Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. 
[^6]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. 
[^7]: Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. 
