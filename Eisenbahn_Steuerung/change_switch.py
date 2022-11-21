def change_rail_switch(route, bahnhof):

    # Variables 
    row = 0
    column = 0
    switching_order = []
    # Switch Grid
    switch_change = [
                        [13, 14, 23, 27, 31, 32, 35, 41, 42, 45, 56, 62, 78, 83, 87],
                        [1, 1, 3, 3, 7, 7, 7, 7, 7, 7, 0, 0, 0, 5, 5],
                        [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 0, 0, 0, 1, 2],
                        [0, 0, 0, 0, 8, 8, 0, 8, 8, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 2, 1, 0, 2, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    ]

    # Überprüfen, welche Weichen wohin gestellt werden müssen
    for i in range(len(route)-1):
        station_now = route[i]
        station_next = route[i+1]

        switching_station = int(str(station_now)+(str(station_next)))

        for j in range(len(max(switch_change))):
            if switch_change[0][j] == switching_station:
                for k in range(1, len(switch_change)):
                    if switch_change[k][j] != 0:
                        #print(switch_change[k][j])
                        switching_order.append(switch_change[k][j])
                        row = row + 1
                    else:
                        break
                break

    return switching_order
