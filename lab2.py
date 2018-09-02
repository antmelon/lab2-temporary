import os
def main():
    weeks = int(input("How many weeks: "))
    print(type(weeks))
    classes = int(input("How many classes: "))
    print(type(classes))
    tuition = int(input("How much is tuition: "))
    print(type(tuition))
    cost_per_week = ((tuition / classes) / weeks)
    print("Cost per week:", cost_per_week)
    print(type(cost_per_week))

    os.system("man man")
    os.system("man cat")
    os.system("man pwd")
    os.system("man mkdir")
    os.system("man rm")
    os.system("man cd")
    os.system("man ls")
    os.system("man mv")
    os.system("man cp")
    os.system("man python2")

main()
