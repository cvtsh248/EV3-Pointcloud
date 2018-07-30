# EV3-Pointcloud
A Work in progress 3D scanner made with the Lego Mindstorms EV3 home kit (31313) written in Python 2.7, and Lego's version of LabVIEW. The IR sensor is placed 18 cm above the pivot point (Z axis).

# Todo
Improve accuracy of readings

# Python Dependencies
* pyserial
* time
* struct
* math
* pyquaternion
* points (a module written for creating an OBJ file from given vertices, available on this github page)

# Hardware
1 Lego Mindstorms EV3 IR sensor, 1 EV3 Medium Servo Motor, 2 EV3 Large Servo Motors.

# Usage
Pair the EV3 and your computer

Go to the LabVIEW script and change the "receiving brick name" of all the bluetooth bricks to the name of your computer. This requires the EV3 software.

If you are using Linux, you must first copy the following command into terminal:
```
sudo rfcomm bind 0 <Bluetooth address of EV3>
```
This binds the socket rfcomm0 to the bluetooth output of the EV3.

Then replace line 10 of the python script, ```recivebt.py``` with ```EV3 = serial.Serial('/dev/rfcomm0')```.

If you are using a Mac, replace line 10 of the python script, ```recivebt.py``` with 
```EV3 = serial.Serial('/dev/tty.<EV3 Brick name goes here>-SerialPort')```.

Ensure that the EV3 software is not running while using the script.

Run the python script ```recivebt.py```.

I'm aware of the typo 'recive'. I just haven't changed it.
Wait for the following text to turn up in the console:
```Waiting for EV3 Bluetooth messages, CTRL C to quit.```

On your EV3 navigate to the folder TOWER, and run the program scan.

You should begin to see coordinates and numbers turning up on the console.

Once the numbers stop piling up in the console, and the EV3 shows that the program is over, hit CTRL C to exit and create the .obj file. You will see that in the folder the program is in, a file called out.obj will have appeared, and that .obj file contains the point cloud. 
