import csv

def calculateCapacity(file_path):
    with open(file_path, 'r') as openfile:
        header = next(openfile)
        voltageCutOff_line = next(openfile)
        voltageCutOff = float(voltageCutOff_line[20:23])/1000
        allData = csv.reader(openfile)
        dataAsAList = list(allData)

    lastTimeValue = 0
    ampHoursTotal = 0

    for index, row in enumerate(dataAsAList):
        voltage = row[1]

        if voltage == '':
            voltage = 0

        voltage = float(voltage)

        if voltage != 0:
            last_nonzero_voltage = voltage

        if index > 0 and last_nonzero_voltage !=None and voltage == 0:
            voltage = last_nonzero_voltage
        
        current = voltage / 5

        time = int(row[0])/(3600)

        timeDifference = time - lastTimeValue
        lastTimeValue = time

        if int(row[2]) == 1:
            ampHoursTotal += current*timeDifference

    # print(f"Total capacity is {ampHoursTotal:.2f}Ah.")
    return(ampHoursTotal)

