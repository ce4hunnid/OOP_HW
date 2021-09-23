import Car_Class as cc

def main():
    bmw = cc.Car('2015','M3')
    for i in range(5):
        bmw.accelerate()
        speed = bmw.get_speed()
        print('Current speed:', speed)
        i += 1

    for i in range(5):
        bmw.brake()
        speed = bmw.get_speed()
        print('Current speed:', speed)
        i += 1

main()