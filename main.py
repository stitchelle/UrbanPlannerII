from building import Building
from city import City

stitchelle = City("Stitchelle", 2018)

iheart = Building("iHeart")
smile = Building("Smile")
nss = Building("NSS")
ubs = Building("UBS")

stitchelle.buildings.append(iheart)
stitchelle.buildings.append(smile)

for building in stitchelle.buildings:
    print(building.name)

