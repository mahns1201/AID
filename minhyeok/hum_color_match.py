import get_live_data as data

# 전국

try:
    HUM = []

    for i in range(len(data.korea_new)):
        HUM.append(float(data.korea_new[i][2]))

    MAX = max(HUM)
    MIN = min(HUM)
    MID = (MAX + MIN) / 2

    MIN_2 = (MIN + MID) / 2
    MIN_1 = (MIN + MIN_2) / 2
    MIN_3 = (MIN_2 + MID) / 2

    MAX_2 = (MID + MAX) / 2
    MAX_1 = (MID + MAX_2) / 2
    MAX_3 = (MAX_2 + MAX) / 2

    hum_colors = [
        "#9999ff",    #MIN
        "#8080ff",    #MIN_1
        "#6666ff",    #MIN_2 
        "#4d4dff",    #MIN_3
        "#3333ff",    #MID
        "#1a1aff",    #MAX_1
        "#0000ff",    #MAX_2
        "#0000e6",    #MAX_3
        "#0000cc"]    #MAX

    humResultValues = []
    humResultColors = []

    for hum in HUM:

        humResultValues.append(hum)

        if MIN <= hum < MIN_1: humResultColors.append(hum_colors[0])
        elif MIN_1 <= hum < MIN_2: humResultColors.append(hum_colors[1])
        elif MIN_2 <= hum < MIN_3: humResultColors.append(hum_colors[2])
        elif MIN_3 <= hum < MID: humResultColors.append(hum_colors[3])
        elif MID <= hum < MAX_1: humResultColors.append(hum_colors[4])
        elif MAX_1 <= hum < MAX_2: humResultColors.append(hum_colors[5])
        elif MAX_2 <= hum < MAX_3: humResultColors.append(hum_colors[6])
        elif MAX_3 <= hum < MAX: humResultColors.append(hum_colors[7])
        elif hum == MAX: humResultColors.append(hum_colors[8])
        else: humResultColors.append("#ffffff")

except ValueError:
    humResultValues = []
    humResultColors = []
    pass

