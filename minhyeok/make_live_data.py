import json
import time
import get_city as city
import temp_color_match as tcm
import hum_color_match as hcm

# 전국

while True:
    korea_dict = {}

    if tcm.tempResultValues == [] or tcm.tempResultColors ==[] or hcm.humResultValues == [] or hcm.humResultColors ==[]:
        print(time.strftime('%Y/%m/%d %H:%M:%S'), "loading now...") 

    else:

        for i in range(len(city.city)):
            korea_dict[city.city[i]] = [
                {"temperature": tcm.tempResultValues[i]},
                {"temp_color": tcm.tempResultColors[i]},
                {"humidity": hcm.humResultValues[i]},
                {"hum_color": hcm.humResultColors[i]}
            ]

        with open('liveData.json', 'w', encoding='UTF-8-sig') as file:
            file.write(json.dumps(korea_dict, ensure_ascii=False))

        print(time.strftime('%Y/%m/%d %H:%M:%S'), "worked properly!")
        
    time.sleep(61)

    


# print(korea_dict)