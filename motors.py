import time, math
#from adafruit_servokit import ServoKit

#kit = ServoKit(channels=16)

def IK_Solve(x, y, z):
    #Convert to polar coordinates
    theta = math.atan2(y, x)
    r = math.sqrt(x**2 + y**2) - 9

    #Base angle is equal to theta
    theta1 = theta + 90

    #Inverse Kinematic Equations for 3-link planar arm
    length1 = 102.7
    length2 = 96.7
    length3 = 35.1

    #Set end effector coordinates
    x_e = r
    y_e = z
    phi_e = math.pi/2

    #Find wrist coordinates
    x_w = x_e - length3 * math.cos(phi_e)
    y_w = y_e - length3 * math.sin(phi_e)
    print(x_w, y_w)

    #Woodward's method
    c2 = (x_w**2 + y_w**2 - length1**2 - length2**2)/(2*length1*length2)
    s2 = -math.sqrt(1-c2**2)
    theta3 = math.atan2(s2, c2)
    print(theta2)


    alpha = math.atan2(y_w, x_w)

    theta2 = math.pi - math.acos((length1**2 + length2**2 - x_w**2 - y_w**2)/(2*length1*length2))
    print(theta3)
    theta1 = alpha - math.acos((x_w**2 + y_w**2 + length1**2 - length2**2)/(2*length1*math.sqrt(x_w**2 + y_w**2)))
    print(theta2)
    theta4 = phi_e - theta1 - theta2
    print(theta4)

    return [theta1, theta2, theta3, theta4]
# kit.servo[0].angle = 180
# kit.continuous_servo[1].throttle = 1
# time.sleep(1)
# kit.continuous_servo[1].throttle = -1
# time.sleep(1)
# kit.servo[0].angle = 0
# kit.continuous_servo[1].throttle = 0
