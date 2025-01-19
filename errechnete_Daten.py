import sensoren_self as s
import math

def TrueWindAngle():
    AWA = s.ApWindAngleSensor()                         # Scheinbarer Windwinkel
    AWS = s.ApWindSpeedSensor()                         # Scheinbare Windgeschwindigkeit
    SoG = s.SoGSensor()                                 # Geschwindigkeit über Grund

    AWA_rad = math.radians(AWA)
    TWx = math.cos(AWA_rad)*AWS-SoG                     # Umrechnung x-Komponente Wind mit Fahrtwind
    AWy = math.sin(AWA_rad)*AWS                         # Umrechnung y-Komponente Wind 
    TWA = math.degrees(math.atan2(AWy, TWx))            # Ausrehcnen wahrer Windwinkel
    if TWA < 0:
        TWA += 360                                      # Normalisierung auf 360°                
    return TWA


def TrueWindSpeed():
    AWA = s.ApWindAngleSensor()                         # Scheinbarer Windwinkel
    AWS = s.ApWindSpeedSensor()                         # Scheinbare Windgeschwindigkeit
    SoG = s.SoGSensor()                                 # Geschwindigkeit über Grund

    AWA_rad = math.radians(AWA)
    TWx = math.cos(AWA_rad)*AWS-SoG                     # Umrechnung x-Komponente Wind mit Fahrtwind
    AWy = math.sin(AWA_rad)*AWS                         # Umrechnung y-Komponente Wind                                     
    TWS = math.sqrt(TWx**2 + AWy**2)                    # Berechnung wahre Windgeschwindigkeit
    return TWS

def Current():
    StW = s.StWSensor()
    SoG = s.SoGSensor()
    CoG = s.CoGSensor()
    Heading = s.HeadingSensor()

    alphaC=math.radians(Heading-CoG)                    # Fahrtwinkel über Grund reltiv zum Heading

    yS=StW-math.cos(alphaC)*SoG                         # y-Komponente Strömung
    xS=math.sin(alphaC)*SoG                             # x-Komponente Strömung
    cS=math.sqrt(yS**2+xS**2)                           # Strömungsstärke
    alphaS_rad=math.atan2(xS, yS)                       
    alphaS=math.degrees(alphaS_rad)                     # Strömungswinkel

    return cS, alphaS

TWS = TrueWindSpeed() 
TWA = TrueWindAngle()
cS, alphaS = Current()
print(f'Strömungsgeschwindigkeit: {cS}kn')
print(f'Strömungswinkel: {alphaS}°')
print(f'Wahrer Windwinkel: {TWA}°')
print(f'Wahre Windgeschwindigkeit: {TWS}kn')