import serial
ser = serial.Serial('COM3' ,9600 )

def control(command):
    if 'on' in command:
        ser.write(b'Y')
    if 'off' in command:
        ser.write(b'N')

while True:
    command = input("Enter On to Trun on LED & off to turn off LED: \t")
    control(command)
