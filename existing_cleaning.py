import csv
import sys
import regex

textFile = open('Clean_Data_Jugantor_02.txt', 'w', encoding='utf-8')
URL_LINK = 'result.csv'

with open(URL_LINK, encoding='utf-8') as unit_url_csv:
    readCSV = csv.reader(unit_url_csv)
    AllWordlist = []
    for row in readCSV:
        Wordlist = regex.findall(r"[\p{Bengali}]+", row[2])
        AllWordlist.extend(Wordlist)

    AllUniqueWordList = set(AllWordlist)
    AllUniqueWordList = sorted(AllUniqueWordList)

    for i in AllUniqueWordList:
        textFile.write(i)
        textFile.write('\n')