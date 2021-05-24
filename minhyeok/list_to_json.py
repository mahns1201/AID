import json
import color_match as cm

# 전국

korea_dict = {}

for i in range(len(cm.city)):
    korea_dict[cm.city[i]] = [
        {"temperature": cm.tempResultValues[i]},
        {"temp_color": cm.tempResultColors[i]},
        {"moisture": cm.humResultValues[i]},
        {"moi_color": cm.humResultColors[i]}
    ]

with open('dict_to_json.json', 'w', encoding='UTF-8-sig') as file:
    file.write(json.dumps(korea_dict, ensure_ascii=False))


print(korea_dict)