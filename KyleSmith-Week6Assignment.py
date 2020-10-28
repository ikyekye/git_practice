def miles_to_kilos():
    miles = int(input("How many miles have you driven?: ")) # Asking user for miles driven
    km = miles * 1.609 #Approximate distance of 1 km compared to 1 mile.
    print "If you have driven", miles, "miles, that is equal to", km, "kilometers."
miles_to_kilos()