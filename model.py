import  csv

#Esta función obtiene los datos y los carga en un diccionario
def getdictfromcsv():
    datafile = open(r'./data/datos_prueba_tecnica.csv', "r")
    csvreader = csv.reader(datafile)
    #Extraigo el header
    header = next(csvreader)[0].split(";")
    number_columns = len(header)
    #El diccionario tendrá como clave el ID de usuario y cada entrada será
    #un diccionario con los datos de un empleado
    data = {}
    for row  in csvreader:
        newrow = row[0].split(";")
        data[newrow[0]] = {} #Asigno cada key es un ID y le asigno un diccionario vacio
        for i in range(1, (number_columns)):
            data[newrow[0]][header[i]] = newrow[i] #Agrego los campos al diccionario vacio
    datafile.close()
    return data
#Esta funcion obtiene el total de empleados y de cada género
def getGenders(data):
    males = 0
    females = 0
    total = 0
    for id in data:
        if data[id]["sexo"] == "H":
            males += 1
            total += 1
        elif data[id]["sexo"] == "M":
            females += 1
            total += 1
    print("Total de empleados: {}".format(total))
    print("Numero de empleados hombre: {}".format(males))
    print("Numero de empleados mujer: {}".format(females))
#Esta funcion obtiene el total de salario de una empresa en el centro de trabajo especificado
def getTotalSalary(data, company : str, workcenter: str):
    total = 0
    for id in data:
        if (data[id]["ID Empresa"] == company) and (data[id]["Nombre centro trabajo"]== workcenter):
            total += int(data[id]["salario bruto anual"])
    print("Total salarios de la empresa {} en el centro de trabajo {}: {}".format(company, workcenter, total))
#Esta función comprueba si cada empleado pertenece a la compañia especficada y si gana más de un valor dado, lo imprime en un listado
def getHigherThanSalary(data, salary, company : str):
    print("Empleados que ganan mas de {} en la empresa {}:".format(salary, company))
    print(f"{'ID':<7}{'Nombre':<30}{'Salario':^7}{'Empresa':>20}")
    for id in data:
        if (data[id]["ID Empresa"] == company) and (int(data[id]["salario bruto anual"])> salary):
            fullname = data[id]["nombre"] + " " + data[id]["apellido1"] + " " + data[id]["apellido2"]
            print(f"{id:<7}{fullname:<30}{data[id]['salario bruto anual']:^7}{data[id]['Nombre empresa']:>20}")


if __name__ == "__main__":
    
    data = getdictfromcsv()
    getGenders(data)
    getTotalSalary(data, "1", "Alovera")
    getHigherThanSalary(data, 28000, "2")