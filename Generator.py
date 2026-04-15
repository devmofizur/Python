
def remote_control_next():
    channels = ["BTV","Jamuna TV", "CN","Desney+", "Dipto", "Channel i"]
    for item in channels:
        yield item # Prints and Remembers every iteration then stops here

itr = remote_control_next()
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


# Example

def fibonacci():
    a , b = 0 , 1
    while True:
        yield a
        a , b = b , a+b
    
for f in fibonacci():
    if f > 100:
        break
    print(f)