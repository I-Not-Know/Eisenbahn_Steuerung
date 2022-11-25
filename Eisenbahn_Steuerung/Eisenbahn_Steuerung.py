# Library einbinden
from time import sleep
from position import *
from calc_route import *
from change_switch import *
from signalling_station import *
from server import send_switching_order

# Array deklarieren
bahnhof = ['Bahnhof 1', 'Bahnhof 2', 'Bahnhof 3', 'Bahnhof 4', 'Bahnhof 5', 'Bahnhof 6', 'Bahnhof 7', 'Bahnhof 8']

#print(len(map))

# Variablen

start = 0
end = 0
# Start und Endp
# Punkt des Zuges bestimmen
destination = get_start_end()

for i in range(2):
    print()

print(destination)
route = get_shortest_path(str(destination[0]), str(destination[1]))

route = list(map(int, route))
print(route)

print("Weichen werden gestellt...")

switching_order = change_rail_switch(route, bahnhof)

# Die switching_order muss zurück an den Client gesendet werden
print(switching_order)

# Sende die Reihenfolge
send_switching_order(switching_order)

switching_station(switching_order)
