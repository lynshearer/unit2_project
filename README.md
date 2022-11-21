# Unit 2 Project
![b93685101c1460fc](https://user-images.githubusercontent.com/100017195/202971624-5e583f4a-3fc9-4300-b590-80c0c5aa6fce.jpg)


# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

## Problem definition

Kris san is a parent of an ISAK student and is worried about the safety of the humidity and temperature levels on the ISAK campus. Because she is a busy businesswoman travelling abroad, she would like for someone on campus to measure and store both the humidity and temperature levels in a dormitory and another location on campus outside of the dormitory for a minimum of 48 hours. With the data collected, she would like to confirm that the humidity and temperature levels on campus are safe for the health of her daughter and a prediction of humidity and temperature for the subsequent 12 hours. 

## Proposed Solution
Considering the client requirements an adequate solution includes a low cost sensing device for humidity and temperature and a custom data script that process and anaysis the samples acquired. For a low cost sensing device an adequate alternative is the DHT11 sensor[^1] which is offered online for less than 5 USD and provides adequare precision and range for the client requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the DHT22, AHT20 or the AM2301B [^2] have higher specifications, however the DHT11 uses a simple serial communication (SPI) rather than more eleborated protocols such as the I2C used by the alternatives. For the range, precision and accuracy required in this applicaiton the DHT11 provides the best compromise. Connecting the DHT11 sensor to a computer requires a device that provides a Serial Port communication. A cheap and often used alternative for prototyping is the Arduino UNO microcontroller [^3]. "Arduino is an open-source electronics platform based on easy-to-use hardware and software"[^4]. In additon to the low cost of the Arduino (< 6USD), this devide is programable and expandable[^1]. Other alternatives include diffeerent versions of the original Arduino but their size and price make them a less adequate solution.

The 


**Design statement**
Lyn and Kris will design and make a poster for a client who is xxx. The poster will include the system diagram and the visual representation and model of humidity and temperature in an ISAK room for 48 hours, and a prediction of a subsquent 12 hours, it will also present the health consequences for the humidity and temperature levels. This is achieved with the software Python in a Raspberry Pi. It will take approximately 1 month to make and will be evaluated according to the criteria xxx.

[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
[^3]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
[^4]:Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.  

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


## Test Plan

# Criteria C: Development

## List of techniques used

## Development


# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration
