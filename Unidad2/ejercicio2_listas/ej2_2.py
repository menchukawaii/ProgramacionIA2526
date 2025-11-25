beatles= []
beatles.append("Jonh Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

for i in range(2):
    beatles.append(input("Introduce un nombre"))
    
del beatles[-2:]
beatles.insert(0, "Ringo Starr")
print(beatles)
print(len(beatles))
