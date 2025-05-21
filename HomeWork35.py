import csv

with open("data2.csv", 'w') as f:
    writer = csv.writer(f, delimiter=";", lineterminator="\r")
    writer.writerow(['hostname', 'vendor', 'model', 'location'])
    writer.writerow(['sw1', 'Cisco', '3750', 'London'])
    writer.writerow(['sw2', 'Cisco', '3850', 'Liverpool'])
    writer.writerow(['sw3', 'Cisco', '3650', 'Liverpool'])
    writer.writerow(['sw4', 'Cisco', '3650', 'London'])
