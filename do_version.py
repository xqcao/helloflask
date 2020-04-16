import json

with open('commitflask.json', 'r') as ff1:
    data = json.load(ff1)

with open("allv.json", 'r') as ff2:
    data2 = json.load(ff2)
ii = 1
for dd in data[-1:]:
    try:
        data2[dd['sha']]
    except:
        data2[dd['sha']] = ii
    ii += 1

with open("allv.json", "w") as ff3:
    json.dump(data2, ff3)
