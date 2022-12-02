# Unit 2 Project
![b93685101c1460fc](https://user-images.githubusercontent.com/100017195/202971624-5e583f4a-3fc9-4300-b590-80c0c5aa6fce.jpg)


# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

## Problem definition

Kris san is a parent of an ISAK student and is worried about the safety of the humidity and temperature levels on the ISAK campus. Because she is a busy businesswoman travelling abroad, she would like for someone on campus to measure and store both the humidity and temperature levels in a dormitory and another location on campus outside of the dormitory for a minimum of 48 hours. With the data collected, she would like to confirm that the humidity and temperature levels on campus are safe for the health of her daughter and a prediction of humidity and temperature for the subsequent 12 hours. 

## Proposed Solution
Considering the client requirements an adequate solution includes a low cost sensing device for humidity and temperature and a custom data script that process and anaysis the samples acquired. For a low cost sensing device an adequate alternative is the DHT11 sensor[^1] which is offered online for less than 5 USD and provides adequare precision and range for the client requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the DHT22, AHT20 or the AM2301B [^2] have higher specifications, however the DHT11 uses a simple serial communication (SPI) rather than more eleborated protocols such as the I2C used by the alternatives. For the range, precision and accuracy required in this applicaiton the DHT11 provides the best compromise. Connecting the DHT11 sensor to a computer requires a device that provides a Serial Port communication. A cheap and often used alternative for prototyping is the Arduino UNO microcontroller [^3]. "Arduino is an open-source electronics platform based on easy-to-use hardware and software"[^4]. In additon to the low cost of the Arduino (< 6USD), this devide is programable and expandable[^1]. Other alternatives include diffeerent versions of the original Arduino but their size and price make them a less adequate solution.

Considering the budgetary constrains of the client and the hardware requirements, the software tool that I proposed for this solution is Python. Python is open source, it is mature and supported in mutiple platforms (platform-independent) including macOS, Windows, Linux and can also be used to program the Arduino microprocessor [^5][^6]. In comparison to the alternative C or C++, which share similar features, Python is a High level programming language (HLL) with high abstraction [^7]. For example, memory management is automatic in Python whereas it is responsability of the C/C++ developer to allocate and free up memory [^7], this could result in faster applications but also memory problems. In addition a HLL language will allow me and future developers extend the solution or solve issues proptly.

**Design statement**
We will design and make a poster for a client who is Kris san. The poster will include the system diagram and the visual representation and model of humidity and temperature in an ISAK room for 48 hours, and a prediction of a subsquent 12 hours, it will also present the health consequences for the humidity and temperature levels. This is achieved with the software Python in a Raspberry Pi. It will take approximately 1 month to make and will be evaluated according to the criteria xxx.

[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
[^3]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
[^4]:Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.  
[^5]:Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. 
[^6]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. 
[^7]: Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. 

## Success Criteria

1. The solution provides a visual representation of the Humidity and Temperature values inside a dormitory (Local) and outside the house (Remote) for a period of minimum 48 hours. 
1. ```[HL]``` The local variables will be measure using a set of 4 sensors around the dormitory.
2. The solution provides a mathematical modelling for the Humidity and Temperature levels for each Local and Remote locations. ```(SL: linear model)```, ```(HL: non-lineal model)```
3. The solution provides a comparative analysis for the Humidity and Temperature levels for each Local and Remote locations including mean, standad deviation, minimum, maximum, and median.
4. ```(SL)```The Local samples are stored in a csv file and ```(HL)``` posted to the remote server.
5. Create a prediction the subsequent 12 hours for both temperature and humidity.
6. A poster summarizing the visual representations, model and analysis is created and communicated.

# Criteria B: Design

## System Diagram
![sysdim_hl](https://user-images.githubusercontent.com/100017195/202972155-a515b55d-e2e5-434d-97ce-878c8630040b.jpg)

**Fig.1** shows the system diagram for the proposed solution (**HL**). The indoor variables will be measured using a Raspberry PI and four DHT11 sensors located inside a room. Four sensors are used to determine more precisely the physical values and include measurement uncertainty. The outdoor variables will be requested to the remote server using a GET request to the API of the server at ```192.168.6.147/readings```. The local values are stored in a CSV database locally and POST to the server using the API and TOKEN authentication. A laptop computer is used for remotely controlling the local Rasberry Pi using a Dekptop sharing application (VNC Viewer). (Optional) Data from the local raspberry is downloaded to the laptop for analysis and processing.


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



## Test Plan
| Software Test Type | Input | Process | Planned Output  |
|------|-------------|----------|---------|

# Criteria C: Development

## List of techniques used

## Development


# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration

