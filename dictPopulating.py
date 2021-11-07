import math
accidentTypeToNumber = {
    "Fatal": 5,
    "Injury Possible": 4,
    "Serious Injury Suspected": 3,
    "Minor Injury Suspected": 2,
    "Property Damage Only": 1,
    True: 1,
    False: 0}

# averages all points in area


def avgRiskDictionary(xmin, xmax, ymin, ymax, step, df, index):

    # initilize
    avgRiskDict = {}
    avgRiskDictValues = {}
    m = 100000
    invStep = 1/step
    for x in range(int(xmin*m), int(xmax*m), int(step*m)):
        for y in range(int(ymin*m), int(ymax*m), int(step*m)):
            avgRiskDict[(x/m, y/m)] = []

    for point in df.itertuples():
        x = math.floor(int(point.Latitude*invStep))/invStep
        y = math.floor(int(point.Longitude*invStep))/invStep
        avgRiskDict[(x, y)].append(point)

    for key, entry in avgRiskDict.items():
        sum = 0
        for row in entry:
            sum += accidentTypeToNumber[row[index+1]]
        length = len(entry)
        if(length > 0):
            sum = sum / len(entry)
        avgRiskDictValues[key] = sum*5

    return avgRiskDictValues
