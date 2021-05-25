import json
import temp_color_match as tcm
import hum_color_match as hcm

# 전국

korea_dict = {}

for i in range(len(tcm.city)):
    korea_dict[tcm.city[i]] = [
        {"temperature": tcm.tempResultValues[i]},
        {"temp_color": tcm.tempResultColors[i]},
        {"moisture": hcm.humResultValues[i]},
        {"moi_color": hcm.humResultColors[i]}
    ]

with open('liveData.json', 'w', encoding='UTF-8-sig') as file:
    file.write(json.dumps(korea_dict, ensure_ascii=False))


# print(korea_dict)