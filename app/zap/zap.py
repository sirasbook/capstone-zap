import csv
import json
import logging

report_path = "zap-report.json"
# Opening JSON file

f = open('report.json')

# returns JSON object as
# a dictionary
data = json.load(f)
report = {
    "alerts": []
}
# Iterating through the json
# list

count = 0

# print(data['site'][0]['alerts'])
for i in data['site'][0]['alerts']:
    count += 1
    report['alerts'].append({
        'alert-no': count,
        'name': i['name'],
        'risk': i['riskdesc'],
        'description': i['desc'],
        'instances': i['instances'],
        'solutions': i['solution'],
        'reference': i['reference']
    })

with open(report_path, 'w') as outfile:
    json.dump(report, outfile)

# Closing file
f.close()