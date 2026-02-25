try:
    while True:
        Number = float(input("Enter a number [0.0, 1.0]: "))
        if Number > 1.0 or Number < 0.0:
            print("Input the number in the [0.0, 1,0] range!")
        else:
            if Number >= 0.9:
                print("A")
            elif Number >= 0.8:
                print("B")
            elif Number >= 0.7:
                print("C")
            else:
                print("F")
except:
    print("Enter a number!")
