import  csv

def getdictfromcsv():
    datafile = open(r'./data/datos_prueba_tecnica.csv')
    csvreader = csv.reader(datafile)

    header = next(csvreader)[0].split(";")
    number_columns = len(header)

    data = {}
    for row  in csvreader:
        newrow = row[0].split(";")
        data[newrow[0]] = {}
        for i in range(1, (number_columns -1)):
            data[newrow[0]][header[i]] = newrow[i]
    datafile.close()
    return data

def getGenders(data):
    males = 0
    females = 0
    for id in data:
        if data[id]["sexo"] == "H":
            males += 1
        elif data[id]["sexo"] == "M":
            females += 1
    print("Number of male employees: {}".format(males))
    print("Number of female employees: {}".format(females))

def totalSalary(data):
    equilibrhaTotal = 0
    aloveraTotal = 0
    for id in data:
        if data[id]["ID Empresa"] == "1":
            equilibrhaTotal += int(data[id]["salario bruto anual"])
        elif data[id]["ID Empresa"] == "2":
            aloveraTotal += int(data[id]["salario bruto anual"])
    print("Salario total Equilibrha: {}".format(equilibrhaTotal))
    print("Salario total Alovera: {}".format(aloveraTotal))


data = getdictfromcsv()
print(data["E00001"]["ID Empresa"])

getGenders(data)
totalSalary(data)