counties=["Arapahoe","Denver","Jefferson"]

if "Arapahoe" in counties or 'El Paso' in counties:
    print('Arapahoe or El Paso is in the list of counties.')

else:
    print('Arapahoe and El Paso are not in the list of counties.')

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])
    
counties_dict={"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for key,value in counties_dict.items():
     print (key, value)

for key,value in counties_dict.items():
    print (key "county has", value "registered voters")


