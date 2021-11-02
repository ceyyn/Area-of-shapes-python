choice,color,vars = input("1: Circle\n2: Square\n3: Triangle\nSelect the shape :"),"\033[34m","\033[0m"
if choice == "1":
    choice = "Circle"
    r = int(input("Enter the r : "))
    result = 3 * (r*r)
elif choice == "2":
    choice = "Square"
    r = int(input("Enter the value of one edge : "))
    result = r*r
elif choice == "3":
    choice = "Triangle"
    r,height = int(input("Enter the base lenght : ")), int(input("Enter the height : "))
    result = (r * height) / 2
else :  print(color + "Anlaşılamadı."+ vars)
print(color +"Area of",choice, ": ",str(result) + vars)