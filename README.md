# Unit 2 Project: A Distributed Weather Station for ISAK
![b93685101c1460fc](https://user-images.githubusercontent.com/100017195/202971624-5e583f4a-3fc9-4300-b590-80c0c5aa6fce.jpg)
**Fig.1** Raspberry Pi meme [^0]

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

![sysdim_hl](https://user-images.githubusercontent.com/100017195/207243642-956054c9-8e5b-4cbe-b165-9fe626dac234.png)


**Fig.2** shows the system diagram for the proposed solution (**HL**). The indoor variables will be measured using a Raspberry PI and four DHT11 sensors located inside a room. Four sensors are used to determine more precisely the physical values and include measurement uncertainty. The outdoor variables will be requested to the remote server using a GET request to the API of the server at ```192.168.6.147/readings```. The local values are stored in a CSV database locally and POST to the server using the API and TOKEN authentication. A laptop computer is used for remotely controlling the local Rasberry Pi using a Dekptop sharing application (VNC Viewer). Data from the local raspberry is downloaded to the laptop for analysis and processing.

## How data is stored
We stored the temperature and humidity data  in both seperate database csv files, and sent the datas to the sensors created in the server everytime the set of data is collected. 

## Flow Diagram 1 - Main File
![IMG_0504](https://user-images.githubusercontent.com/100017195/205495755-11bcf00d-d1df-4470-b2fc-e9f43b84790f.jpeg)
![IMG_0505](https://user-images.githubusercontent.com/100017195/205495760-5109719e-7b78-419b-9498-d0ae682b3d31.jpeg)
**Fig.3** shows the flow diagram of the main file that collects datas from the server and stores them into csv files and sends them to the server.

## Flow Diagram 2 - Server Creation
![Untitled-19](https://user-images.githubusercontent.com/111893043/206170522-88960069-42a2-4ed3-b9d1-0e4238888a66.jpg)
![Untitled-20 3](https://user-images.githubusercontent.com/111893043/206171086-e86bfb21-3013-4bef-b45e-55e83ae545d8.jpg)

**Fig.4** shows the flow diagram of the initiation of accounts for the servers and sensors.

## Flow Diagram 3 - MVP
![Untitled-21](https://user-images.githubusercontent.com/111893043/206180312-15704e70-6f39-4dbe-98e7-e79ce5351f95.jpg)
**Fig.5** shows the flow diagrams for the minimum viable product for the project.



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
| 13       | Create 3 flow diagrams of aspects of code.                        | In order to clearly display in order to clearly display the algorithms used in the product and show how the product was developed.        | 60 mins                 | Dec 05 - Dec 09         | B
| 14       | Research safe humidity and temperature levels.                        | Determine whether humidity and temperature levels on the UWC ISAK campusa are healthy/safe or unhealthy/unsafe.        | 20 mins                 | Dec 05         | D
| 15       | Coding the code for getting data from school sensors.                        | In order to retrieve posted data from the server to apply to future codes and models.        | 45 mins                 | Dec 06         | C
| 16       | Adding codes of mvp, server initialization, and getting data from school sensor.                        | To make sure product development information is updated to Criteria C. Displays the details from how we created our product.        | 20 mins                 | Dec 06         | C
| 17       | Coding the graphings of school and room temperature and humidity datas. | To prepare scatter plot graphs with non-linear best fit functions        | 60 mins                 | Dec 09         | C
| 18       | Coding prototype graphing for one specific data | To plot graphs from all sensors and the average of one specific data (room temperature) | 35 mins                 | Dec 09         | C
| 19       | Upgrading the graphs with smoothing and prediction of the polynomial best fit | To plot smoothed data of sensors with a polynomial best fit which predicts the data 12 hours after the collected time.| 35 mins                 | Dec 10         | C
| 20       | Graphs with additional data | To plot smoothed average data of sensors with maximum, minimum and mean value, with an error bar indicating the standard deviation of the mean data.| 15 mins                 | Dec 10         | C
| 21       | Outline for video and compiling data and images to present the final product and solution. | To gather all information necessary in order to create an organized video presenting our product.| 240 mins                 | Dec 07-11         | D
| 22       | Create scientific poster. | To clearly present the background information, methodologies, materials, results, analysis and conclusion for the client.| 120 mins                 | Dec 07-11         | D
| 23       | Update show your CT | To update a pattern recognition and decomposition for computer thinking skills. | 15 mins                 | Dec 11         | C
| 24       | How data is stored | Upload short desctiption on how the data collected were stored | 3 mins                 | Dec 11         | B
| 25       | Video Creation | Demonstrate the product, describe how product met success critera and explain project clearly. | 20 mins                 | Dec 12         | D
| 26       | Finish updating project repository. | Compile all necessary information on the repository in order to submit. | 60 mins                 | Dec 12         | B

## Test Plan
| Software Test Type | Input | Process | Planned Output  |
|------|-------------|----------|---------|
| Integration Testing | Raspberry Pi and VNC Viewer | 1. Download vnc viewer. 2. Input raspberry pi address into vnc viewer. 3. Access raspberry pi through VNC viewer using username and password. | VNC viewer will authenticate username and password and be able to connect to raspberry pi remotely. |
| Unit Testing | Code to receive information from DHT sensor | 1. Run code. 2. Wait for output from DHT sensor. | Confirm that DHT sensor is functioning properly.|
| Performance Testing | Code to receive humidity and temperature data from DHT sensors | 1. Run code. 2. Measure response time. | Code will run and data will be collected and printed on the computer monitor within 5 seconds.|
| Unit Testing | Code for appending humidity and temperature data to csv file | 1. Run code. | A new csv file will be created for humidity and temperature (humidity.csv and temperatures.csv). Data from DHT sensors will be appended to csv files. |
| Integration Testing | Crontab and VNC Viewer | 1. Run code. 2. Wait to see code runs every 5 minutes and humidity and temperature data is appended to csv file every 5 minutes. | Temperature and humidity data is appended to designated csv file every 5 minutes. Information appended includes data from each of the four sensors, average of data and date and time that data is appended to file.|
| Unit Testing | Code for graphs. | 1. Run code. 2. Wait to see if graphs appear. 3. Confirm that graphs are accurate by comparing to data from CSV files. | Confirm that graph has correct plot for the graph of the line, standard deviation, mean, median, maximum, minimum, prediction, nonlinear model. Compare data with readings collected to ensure maximum accuracy. |



# Criteria C: Development

## Existing tools:
| Software/development tools | coding structure tools | Libraries    |
|----------------------------|------------------------|--------------|
| Python/Pycharm             | for loops              | datetime     |
| VNC viewer                 | API requests           | requests     |
|                            |                        | csv          |
|                            |                        | Adafruit_DHT |
|                            |                        | matplotlib   |
|                            |                        | numpy        |


## List of techniques used
| Technique |
|-----------|
| Posting to a remote server with server API. |
| Retrieving data from a remote server with server API and requests library. |
| For loops in order to run code under certain conditions. For example, to get readings for multiple DHT11 sensors with one for loop of code. Utilizing a for loop is more efficient than creating a code for each sensor separately. |
| Creating lists (in order to save data from DHT11 sensors by temperature and humidity). |
| Creating CSV files (in order to save data from DHT11 sensors by temperature and humidity). |
| Plot median, mean, maximum, minimum, standard deviation and a non linear model using python. |
| Predicting temperature and humidity values based on line of best fit equation (non linear model). |
| Smoothing data on a graph. |

## Computational Thinkings
### Decomposition:
Decomposition refers to breaking a task into smaller and addressable problems. In our codes for project 2, the skill of decomposition can be seen constantly in large, and smaller scales. For instance, when plotting the graphs of all 4 sensors with predictions, we decomposed the tasks into each sensor's average data, smoothing, plotting and the prediction calculation, as well as the plotting of the predictions. One sensor's plotting code can be used as an example shown below:

```.py
# room temperature
room_temp=[]
index=[]
prediction_index=[]
for temp_data in room_temp_data:
    temp_datas = temp_data.strip()
    values = temp_datas.split(",")
    room_temp.append(float(values[4]))
# smoothing data
room_temp_smooth=smoothing(room_temp, 10)
# create index for data
for i in range(len(room_temp_smooth)):
    index.append(i+1)
# create index for prediction
for i in range(ceil(len(index)*1.2)):
    prediction_index.append(i+1)
# calculate best fit polynomial
p = np.poly1d(np.polyfit(index, room_temp_smooth, power))
#start plotting graph
plt.figure(figsize=(fig_width,fig_height))
plt.subplot(4,1,1)
plt.plot(room_temp_smooth)
plt.plot(prediction_index,p(prediction_index), color="red")
plt.title("Room Temperature")
plt.ylabel("Average Temperature(°C)")
plt.xlabel("Measures")
```

### Pattern recognition, generalization and abstraction:
For the codes of the smoothed average of the sensors, there was a lot of repetition when it came to requesting the data for each of the four sensors from the server as well as plotting the average. This decreases the efficiency and simplicity of the code. In order to fix this, multiple functions were defined in order to create a template for the requesting and analysis of the data. These were placed in a cumulative library as shown below. Then, we were able to call these functions and also utilize for loops and inline for loops in order to eradicate any unnecessary repetition in the code for each sensor. This is shown below. 

Lib.py
```.py
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
```

### Algorithms:
In the initial code and MVP, we utilized a while loop in order for the code to loop and take readings at specific intervals. This was inefficient because the task is to get readings at a 5 minute interval for 48 hours, but with a while loop, if the computer was closed or the server lost connection, the code would stop running and therefore stop taking the necessary readings. In order to avoid having to keep the computer and VNC application running actively for 48 hours, we utilized a simple tool that can fix this problem, a crontab task through the raspberry pi terminal in order to create a task that would run the code every five minutes. 

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

<img width="776" alt="crontab" src="https://user-images.githubusercontent.com/100017195/206906756-9e9847ee-fc7d-41f9-a290-83ebf982f805.png">

**Fig.6** shows the cron tab for controlling the program to run every 5 minutes.


## Prototype codes
Below are the developments of the Python code being programmed for the project.
### Library
To improve the simplicity of codes, we created a library of frequently used functions. Please refer to the code in the link.

```.py
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
```

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
Logging in, registering and creating different sensors in the server. Code is as below:
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

# add 1 temperature sensor
auth = {'Authorization':f"Bearer {access_token}"}
new_sensor = {"type": "Temperature", "location": "R3-10A", "name": "temp_lyn_kris_1","unit":"C"}
r= requests.post('http://192.168.6.142/sensor/new',json=new_sensor, headers = auth)
print(r.json())

# add 1 humidity sensor
new_sensor = {"type": "Humidity", "location": "R3-10A", "name": "hum_lyn_kris_1","unit":"%"}
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
### raw data plotting
The code below shows how one raw data is accessed and plotted in a scatterplot. The graph is shown below.
```.py
room_temp=[]
index=[]
count=1
for temp_data in room_temp_data:
    temp_datas = temp_data.strip()
    values = temp_datas.split(",")
    room_temp.append(float(values[4]))
    index.append(count)
    count+=1
#start plotting graph
plt.figure(figsize=(fig_width,fig_height))
plt.subplot(4,1,1)
plt.scatter(index,room_temp)
plt.title("Room Temperature")
plt.ylabel("Average Temperature(°C)")
plt.xlabel("Measures")
```
![raw](https://user-images.githubusercontent.com/100017195/207007472-2f0c45c0-a039-4415-b916-752170f89ebf.jpeg)

**Fig.7** shows the raw datas of average plotted in scatter plots.

### merged graph - 4 sensors + average data - 1 data
We established a **prototype** of how each data can be individually viewed from each sensors' outcomes and view the average of the data using room temperature sensors as an example. The code plots the graps of smoothed room temperature data from all 4 sensors and a larger graph of the average temperature datas. Sensor 6 is used as the example of code below.

Smoothing (using smoothing functions in the library) and calculation of data of sensor 6:

```.py
data_6=[]

data_6=get_sensor(readings,6)

data_6=data_6[0:499]

data_6_smooth=smoothing(data_6,10)
```

Plotting graphs in **boxes**:
```.py
# plotting the data 
# style of graph
plt.style.use('seaborn-whitegrid')
fig=plt.figure(figsize=(10,8))
grid=GridSpec(4,4,figure=fig)
#create big plot
box1=fig.add_subplot(grid[0:4,0:3])
plt.plot(average_smooth)
plt.title("Smoothed average of 4 sensors")
plt.xlabel("Time")
plt.ylabel("Temperature in Celsius")

datas=[data_6_smooth,data_8_smooth,data_9_smooth,data_10_smooth]

#create small plots
for i in range(len(sensors)):
    box=fig.add_subplot(grid[i,3])
    plt.plot(datas[1])
    plt.title(f"Sensor {sensors[i]}")
    plt.xlabel("Time")
    plt.ylabel("Temperature in Celsius")
plt.show()
```

![4+1_data](https://user-images.githubusercontent.com/100017195/206707974-d5a1d7d6-fb11-493e-9684-c96a13daf260.jpeg)
**Fig.8** shows the prototype graph plotted with 4 separate sensor datas and one large graph of average data for room temperature.

### Polynomial fit with predictions
This program aims to plot the **smoothed** average data and plot a **polynomial best fit**, which **predicts** the datas for 12 hours after the collected data ends. Please refer to the code and graphs plotted below.

Calculation of polynomial of best fit:

```.py
p = np.poly1d(np.polyfit(index, room_temp_smooth, power))
```

Plotting existing data and the best fit that extends out side of the data for prediction

```.py
# create index for data
for i in range(len(room_temp_smooth)):
    index.append(i+1)
# create a separate index for prediction
for i in range(ceil(len(index)*1.2)):
    prediction_index.append(i+1)

# plot the data and prediction with the respective index
plt.plot(room_temp_smooth)
plt.plot(prediction_index,p(prediction_index), color="red")

plt.show()
```
![prediction_with_equation](https://user-images.githubusercontent.com/100017195/207009283-f8ed823f-69cb-434d-ab0f-27f1f3decae5.jpeg)


**Fig.9** shows the room and school temperature and humidity average data smoothed, with a polynomial best fit which extends 12 hours over the data collected for prediction with the calculated function of polynomial best fit displayed.

After experimenting on different exponents of best fit polynomial functions. The higher the exponent is, although it fits the graph better, in the predictions the shape of the end gets way too steep. Thus, after experimenting, we discovered that the **cubic polynomial** best fit works the best.

### Max, min, mean, medium & standard deviation 
This program aims to plot the maximum, minimum, medium values of the plotted mean values of data, and indicate the values with lines horizontal to the x-axis. The program also plots error bars to illustrate the dtandard deviation. Please refer to the code and graph plotted below.

This is an example code of how to plot minimum, maximum, mean, and standard deviation as error bar

```.py
# plot maximum, minimum, mean
plt.axhline(y=max(room_temp_smooth), color="red")
plt.axhline(y=min(room_temp_smooth), color="green")
plt.axhline(y=np.mean(room_temp_smooth), color="orange")
```

calculate standard deviation
```.py
std_dev=[]
sensor1=[]
sensor2=[]
sensor3=[]
sensor4=[]
for temp_data in room_temp_data:
    sensor1.append(float(values[0]))
    sensor2.append(float(values[1]))
    sensor3.append(float(values[2]))
    sensor4.append(float(values[3]))
# smoothing
sm1=smoothing(sensor1,10)
sm2=smoothing(sensor2,10)
sm3=smoothing(sensor3,10)
sm4=smoothing(sensor4,10)

for i in range(len(sm1)):
    datas=[sm1[i],sm2[i],sm3[i],sm4[i]]
    std_dev.append(np.std(datas))


plt.errorbar(index, room_temp_smooth, yerr=std_dev, fmt='o', color="lightblue")
plt.show()
```

![max, min, medium, stad](https://user-images.githubusercontent.com/100017195/207007875-3ef3238c-ce1d-41e0-8aaa-ed1bc961dbf4.jpeg)

**Fig.10** shows the average smoothed data for school and room temperature and humidity with the extra data including maximum, minimum, mean, and an error bar graph displaying the standard deviation.
Since for the school sensors there is only one for each data, but there are 4 sensors in the room. We could only plot the standard deviations for room sensors but not for the school sensors.

The standard deviation did not vary much from one to the adjacent one because there is not much difference in the measurements between sensors since the sensors are quite close to each other on the limited space on the breadboard.

# Criteria D: Functionality

## Scientific Poster
![ISAK Weather Station (4)](https://user-images.githubusercontent.com/111893043/207023819-cecf5274-a90b-4736-a3e9-4f76f4bb264b.jpeg)

**Fig.11** scientific poster summarizing the project.

## Product Demonstration and Solution Video

Link: https://www.youtube.com/watch?v=mEBOmnRET2s

[^0]: Cherry Pie Apple Pie Raspberry Pi Meme https://www.imagesplatform.com/post/cherry-pie-apple-pie-raspberry-pi-meme-vkE87
[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
[^3]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
[^4]:Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.  
[^5]:Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. 
[^6]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. 
[^7]: Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. 
