import RPi.GPIO as GPIO          
from time import sleep

in1 = 40
in2 = 38
ena = 36

in3 = 33
in4 = 35
enb = 37

in5 = 13
in6 = 15
enc = 11

in7 = 3
in8 = 5
end = 7

# in1 = 13
# in2 = 15
# ena = 11
# 
# in3 = 3
# in4 = 5
# enb = 7
# 
# in5 = 40
# in6 = 38
# enc = 36
# 
# in7 = 8
# in8 = 10
# end = 12
temp1=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)
GPIO.setup(enc,GPIO.OUT)
GPIO.output(in5,GPIO.LOW)
GPIO.output(in6,GPIO.LOW)

GPIO.setup(in7,GPIO.OUT)
GPIO.setup(in8,GPIO.OUT)
GPIO.setup(end,GPIO.OUT)
GPIO.output(in7,GPIO.LOW)
GPIO.output(in8,GPIO.LOW)

pa=GPIO.PWM(ena,1000)
pa.start(100)

pb=GPIO.PWM(enb,1000)
pb.start(100)

pc=GPIO.PWM(enc,1000)
pc.start(100)

pd=GPIO.PWM(end,1000)
pd.start(100)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=input()
    
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         GPIO.output(in5,GPIO.HIGH)
         GPIO.output(in6,GPIO.LOW)
         GPIO.output(in7,GPIO.HIGH)
         GPIO.output(in8,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         GPIO.output(in3,GPIO.LOW)
         GPIO.output(in4,GPIO.HIGH)
         GPIO.output(in5,GPIO.LOW)
         GPIO.output(in6,GPIO.HIGH)
         GPIO.output(in7,GPIO.LOW)
         GPIO.output(in8,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in5,GPIO.LOW)
        GPIO.output(in6,GPIO.LOW)
        GPIO.output(in7,GPIO.LOW)
        GPIO.output(in8,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
#         GPIO.output(in1,GPIO.HIGH)
#         GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
#         GPIO.output(in5,GPIO.HIGH)
#         GPIO.output(in6,GPIO.LOW)
#         GPIO.output(in7,GPIO.HIGH)
#         GPIO.output(in8,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(in5,GPIO.LOW)
        GPIO.output(in6,GPIO.HIGH)
        GPIO.output(in7,GPIO.LOW)
        GPIO.output(in8,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='l':
        print("low")
        pa.ChangeDutyCycle(25)
        pb.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        pa.ChangeDutyCycle(50)
        pb.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        pa.ChangeDutyCycle(75)
        pb.ChangeDutyCycle(75)
        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")