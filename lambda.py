import math
def speed(distance,time):
    return distance/time

distance = 100
time = 22

print(speed(distance,time))

print((lambda d,t : d/t)(distance,time))

print((lambda a,b : math.sqrt(a) + 2*a*b + math.sqrt(b))(5,8))