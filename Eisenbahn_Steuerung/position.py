def get_start_end(start, end, bahnhof):
    correct = False
    while correct == False:
        print("Geben Sie den Startpunkt an:")
        start = int(input()) - 1;
        if start < len(bahnhof) and start >= 0:
            correct = True
            start = start + 1
        else:
            print('Out of bound')

    # Eingabe des Zieles
    correct = False
    while correct == False:
        print("Geben Sie den Endpunkt an:")
        end = int(input()) - 1;
        if end < len(bahnhof) and end >= 0:
            correct = True
            end = end + 1
        else:
            print('Out of bound')

    return start, end
