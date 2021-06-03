import get_live_data as data

# 전국

try:
    TEMP = []

    for i in range(len(data.korea_new)):
        TEMP.append(float(data.korea_new[i][1]))
        
    MAX = max(TEMP)
    MIN = min(TEMP)
    MID = (MAX + MIN) / 2

    MIN_2 = (MIN + MID) / 2
    MIN_1 = (MIN + MIN_2) / 2
    MIN_3 = (MIN_2 + MID) / 2

    MAX_2 = (MID + MAX) / 2
    MAX_1 = (MID + MAX_2) / 2
    MAX_3 = (MAX_2 + MAX) / 2

    temp_colors = [   
        "#f6a2b3",    #MIN
        "#f48aa0",    #MIN_1
        "#f2738c",    #MIN_2 
        "#f05c79",    #MIN_3
        "#ee4466",    #MID
        "#eb2d53",    #MAX_1
        "#e91640",    #MAX_2
        "#dc143c",    #MAX_3
        "#d2143a"]    #MAX

    tempResultValues = []
    tempResultColors = []

    for temp in TEMP:

        tempResultValues.append(temp)

        if MIN <= temp < MIN_1: tempResultColors.append(temp_colors[0])
        elif MIN_1 <= temp < MIN_2: tempResultColors.append(temp_colors[1])
        elif MIN_2 <= temp < MIN_3: tempResultColors.append(temp_colors[2])
        elif MIN_3 <= temp < MID: tempResultColors.append(temp_colors[3])
        elif MID <= temp < MAX_1: tempResultColors.append(temp_colors[4])
        elif MAX_1 <= temp < MAX_2: tempResultColors.append(temp_colors[5])
        elif MAX_2 <= temp < MAX_3: tempResultColors.append(temp_colors[6])
        elif MAX_3 <= temp < MAX: tempResultColors.append(temp_colors[7])
        elif temp == MAX: tempResultColors.append(temp_colors[8])
        else: tempResultColors.append("#ffffff")

except ValueError:
    tempResultValues = []
    tempResultColors = []
    pass

