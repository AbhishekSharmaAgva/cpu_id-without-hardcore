
import serial
import RPi.GPIO as GPIO
import os, time

def getserial():
		cpuserial = 0
		f = open('/proc/cpuinfo','r')
		for line in f:
			if line[0:6]=='Serial':
				cpuserial = line[10:26]
				f.close()
				return cpuserial
				exit()
		return 0

x = getserial()
#print(x)
file1 = open('/home/pi/myfile.txt',"r")
data = (file1.read(16))
#print(data)
file1.close()
file1 = open('/home/pi/myfile.txt',"w")
file1.write(data)
file1.close()
path =  '/home/pi/myfile.txt'
isExist = os.path.exists(path)
print(isExist)
file1 = open('/home/pi/myfile.txt',"r")
data1 = (file1.read(16))
#print (data1)
file1.close()
if(data == x):
	print("cpu_id match")
	GPIO.setmode(GPIO.BOARD)

	port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
	str = chr(26)
	while 1:
		port.write('AT'+'\r\n')
		rcv = port.read(128)
		print rcv
		time.sleep(0.1)

		port.write('AT+CPIN?\r\n')      # Disable the Echo
		rcv = port.read(128)
		print rcv
		time.sleep(0.1)

		port.write('AT+CREG?\r\n')      # Disable the Echo
		rcv = port.read(128)
		print rcv
		time.sleep(0.1)

		port.write('AT+CGATT?\r\n')      # Disable the Echo
		rcv = port.read(128)
		print rcv
		time.sleep(0.1)

		port.write('AT+CIPSHUT\r\n')  # Select Message format as Text mode 
		rcv = port.read(128)
		print rcv
		time.sleep(0.1)
 
		port.write('AT+CIPSTATUS\r\n')      # Disable the Echo
		rcv = port.read(128)
		print rcv
		time.sleep(0.1)

		port.write('AT+CIPMUX=0\r\n')   # New SMS Message Indications
		rcv = port.read(128)
		print rcv
		time.sleep(0.1)
 
# Sending a message to a particular Number
#	port.write("AT+CGDCONT=1"+","+'"IP"'+","'"airtelgprs.com"\r')
#	rcv = port.read(128)
#	print rcv
#	time.sleep(1)

		port.write('AT+CSTT="airtelgprs.com"\r\n')
		rcv = port.read(128)
		print rcv
		time.sleep(0.1)
	
		port.write('AT+CIICR\r\n')      # Disable the Echo
		rcv = port.read(128)
		print rcv
		time.sleep(0.1)

		port.write('AT+CIFSR\r\n')      # Disable the Echo
		rcv = port.read(128)
		print rcv
		time.sleep(0.1)

		port.write('AT+CIPSTATUS\r\n')      # Disable the Echo
		rcv = port.read(128)
		print rcv
		time.sleep(0.1)

		port.write('AT+CIPSTART="TCP","api.thingspeak.com","80"\r\n')      # Disable the Echo
#	time.sleep(0.3)
		rcv = port.read(128)
		print rcv
		time.sleep(3)

#	port.write('AT+HTTPINIT\r\n')      # Disable the Echo
#	time.sleep(1)
#	rcv = port.read(128)
#	print rcv
#	time.sleep(0.3)


		x='GET https://api.thingspeak.com/update?api_key=FVTA8D044KOWOM7C&field1=10\r\n'
		port.write('AT+CIPSEND\r\n')  # + x +'#026\r')      # Disable the Echo
		rcv = port.read(128)
		print rcv	
		time.sleep(0.1)
		port.write(x)
		rcv = port.read(128)
		print rcv
		port.write(str.encode())
		rcv = port.read(128)
		print rcv
 
#	x='GET https://api.thingspeak.com/update?api_key=FVTA8D044KOWOM7C&field1=5000'
		port.write('AT+CIPCLOSE=1'+'\r\n')      # Disable the Echo
		rcv = port.read(128)
		print rcv
       		time.sleep(0.1)

#	x='GET https://api.thingspeak.com/update?api_key=FVTA8D044KOWOM7C&field1=5000'
		port.write('AT+CIPSHUT'+'\r\n')      # Disable the Echo
		rcv = port.read(128)
		print rcv
	       	time.sleep(0.1)

else:
	print("cpu_id Mismatch")
	port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

	port.write('AT'+'\r\n')
	rcv = port.read(10)
	print rcv
	time.sleep(1)
 
	port.write('ATE0'+'\r\n')      # Disable the Echo
	rcv = port.read(10)
	print rcv
	time.sleep(1)
 
	port.write('AT+CMGF=1'+'\r\n')  # Select Message format as Text mode 
	rcv = port.read(10)
	print rcv
	time.sleep(1)
 
	port.write('AT+CNMI=2,1,0,0,0'+'\r\n')   # New SMS Message Indications
	rcv = port.read(10)
	print rcv
	time.sleep(1)
 
# Sending a message to a particular Number
 
	port.write('AT+CMGS="8218155505"'+'\r\n')
	rcv = port.read(10)
	print rcv
	time.sleep(1)
 
	port.write('error you putted the wrong raspberry pi'+'\r\n')  # Message
	rcv = port.read(10)
	print rcv
 
	port.write("\x1A") # Enable to send SMS
	for i in range(10):
		rcv = port.read(10)
		print rcv
