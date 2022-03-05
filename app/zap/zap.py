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
for i in data['site'][0]['alerts']:
    count += 1
    report['alerts'].append({
        'alert_no': count,
        'name': i['name'],
        'risk': i['riskdesc'],
        'description': i['desc'],
        'instances': i['instances'],
        'count': i['count'],
        'solutions': i['solution'],
        'reference': i['reference'],
        'cweid': i['cweid'],
        'refid': i['alertRef']
    })

with open(report_path, 'w') as outfile:
    json.dump(report, outfile)

f.close()