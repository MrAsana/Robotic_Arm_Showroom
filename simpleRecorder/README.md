# Simple Recorder

A sample program that provides key point recording and playback functions .

==WARNING== 

It is strictly prohibited to move any joints on the robotic arm when switching modes.

The main functions are as follows

```
===================================================
|         A sample program that provides          |
|    key point recording and playback functions   |
=================== USE KEYBOARD ==================
| [P] Position Mode                               |
| [S] Start dragging                              |
| [E] End dragging                                |
| [1-9] Write a key point                         |
|           and record the number you pressed     |
|               as the duration.                  |
| [R] Replay All                                  |
| [N] Play next point                             |
| [Z] Back to Zero position                       |
| [Q] Quit                                        |
===================================================
```

### Configurations

You may need to change the following configuration in `sample_func.py`

```
# = SETTINGS BELOW =


IP_ADDR = "192.168.50.235"
PORT = 26001
FILE_NAME = 'KeyPoints'
DEFAULT_TIMEOUT = 10
DEFAULT_ACCURACY = 0.0175  # rad, for every joint, 0.0175 rad= 1 degree


# ==================
```

Mainly change the IP address to the IP address of the industrial control computer that comes with the robot arm.

NOTE: For a 6-actuator system, change here in amber_api/cmd_10.py
in line 42

```
            if activated > 6: # Change here to 5 for a 6 actuator system
                return True
```
