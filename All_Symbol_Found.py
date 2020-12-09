import csv
import sys
import re

textFile = open('Find_All_Symbol.txt', 'w', encoding='utf-8')
URL_LINK = 'result.csv'

pattern = r"[অ-ঔ ক-ৎ য় ড় ঢ় ১-৯]"
symbol = []

with open(URL_LINK, encoding='utf-8') as unit_url_csv:
    readCSV = csv.reader(unit_url_csv)
    for row in readCSV:
        Line = str(row[2])

        for i in Line:
            if not bool(re.search(pattern, i)):
                if i not in symbol:
                    symbol.append(i)
                    textFile.write(i)
                    textFile.write('\n')

