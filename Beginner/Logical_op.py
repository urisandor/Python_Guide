#or
temp = 30
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("the outdoor event is still scheduled")

#and

is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside!!")
    print("It is SUNNY!!")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif 29 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")