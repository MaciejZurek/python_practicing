address = "Attractive Street, Beverly Hills, CA 90120"

print(address[0:10])
print(address[19:32])
print(address[10:100]) # nie ma bledu
print(address[34:-6])
print(address[-8:-6])
print(address[-8:36])

street = address[0:17] # ta druga granica nie zawiera sie w przedziale, wpisujac 17 docieramy do 16 znaku
print(street)

print(address[5:])
print(address[13:])
print(address[:-20])
print(address[:]) # to inny obiekt, tak naprawde tworzy sie kopia oryginalu i jest wypisywana

