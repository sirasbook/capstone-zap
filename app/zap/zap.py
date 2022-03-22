import csv
import json
import logging

report_path = "/zap/wrk/app/reports/zap-report.json"

f = open('/zap/wrk/app/reports/report.json')
data = json.load(f)
report = {
    "alerts": []
}

count = 0

for i in range(len(data['site'])):
    for j in data['site'][i]['alerts']:
        count += 1
        report['alerts'].append({
            'alert_no': count,
            'name': j['name'],
            'risk': j['riskdesc'],
            'description': j['desc'],
            'instances': j['instances'],
            'count': j['count'],
            'solutions': j['solution'],
            'reference': j['reference'],
            'cweid': j['cweid'],
            'refid': j['alertRef']
        })

with open(report_path, 'w') as outfile:
    json.dump(report, outfile)

f.close()