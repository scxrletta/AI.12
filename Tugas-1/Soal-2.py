def circleWidth(radius):
    w = 22/7*radius*radius
    w_rounded = round(w, 2)
    print("A circle width a radius of {} cm has a width of {} cm\u00b2".format(radius, w_rounded))

r = float(input("Input circle radius here: "))

circleWidth(r)