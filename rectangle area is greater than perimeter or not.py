length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area:", area)
print("Perimeter:", perimeter)

if perimeter > area:
    print("Perimeter is greater than area.")
elif perimeter < area:
    print("Area is greater than perimeter.")
else:
    print("Perimeter and area are equal.")
