AngkorWat = (13.4125, 103.866667)

print(type(AngkorWat))
# <class 'tuple'="">

print("AngkorWat is at latitude: {}".format(AngkorWat[0]))
# AngkorWat is at latitude: 13.4125

print("AngkorWat is at longitude: {}".format(AngkorWat[1]))
# AngkorWat is at longitude: 103.866667
location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])
length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))

tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b)
print(tuple_a[1])