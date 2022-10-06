import math
print( math.pi )
radius_1=int(input("Enter radius_1: \n"))
radius_2=int(input("Enter radius_2: \n"))
Area_1=( math.pi )*radius_1**2
Area_2=( math.pi )*radius_2**2

print(f"Area of circle_1 is {Area_1}")
print(f"Area of circle_2 is {Area_2}")

if (Area_1>Area_2):
    print(f"Circle_1 area is greater and its area is {Area_1}")
elif (Area_1 == Area_2):
    print(f"Circle_1  and Circle_2 area are equal and their area is {Area_1 or Area_1}")
else:
    print(f"Circle_2 area is greater and its area is {Area_2}") 