import random

def HeadingSensor():
    currentHeading = random.uniform(0,360)
    return currentHeading

def CoGSensor():
    currentCoG = random.uniform(0,360)
    return currentCoG

def SoGSensor():
    SoG = random.uniform(0,16)
    return SoG

def StWSensor():
    StW = random.uniform(0,16)
    return StW

def ApWindSpeedSensor():
    ApWindSpeed = random.uniform(0,60)
    return ApWindSpeed

def ApWindAngleSensor():
    ApWindAngle = random.uniform(0,360)
    return ApWindAngle

def RudderAngleSensor():
    RudderAngle = random.uniform(0,90)
    return RudderAngle


if __name__ == "__main__":
    i=0
    while i <= 5:
        test1 = CoGSensor()
        test2 = HeadingSensor()
        print(test1)
        print(test2)
        i += 1
    

