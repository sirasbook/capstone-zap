#!/bin/sh

target="$1"

# Scan
../zap/zap-full-scan.py -t $target -g gen.conf -J app/reports/report.json

# Parse the report
python3 ./app/zap/zap.py

rm -rf /zap/wrk/app/reports/report.json