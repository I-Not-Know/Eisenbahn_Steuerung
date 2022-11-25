def switching_station(switching_order):
    # Reihenfolge muss angepasst werden, was links, was rechts
    for i in range(0, len(switching_order), 2):
        print("Weiche:", switching_order[i], " Richtung:", switching_order[i+1])
