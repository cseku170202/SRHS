import csv
import re
import os
import glob
import pandas as pd


def append_to_csv(row,category):
    global CSV_LINK
    with open("Found_"+category+".txt", mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            news_article_writer.writerow(row)
    #news_article_writer.close()
    pass



all_problem={}
no_of_prob=-1
with open('unique_sorted_initial_incorrect_data.txt','r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for Line in csv_reader:
        Test=str(Line)
        L=len(Test)
        Flag=0
        for i in range(L):
            
            if not(bool(re.search('[অ-হ]', Test[i]))):
                    char=Test[i]
                    Flag=1
                   
                    if Test[i]=='"':
                        append_to_csv(Line,"Found_doubleQuate")
                        continue
                    if Test[i]=='\\':
                        
                        append_to_csv(Line,"Found_backslash")
                    if Test[i]=='/':
                        append_to_csv(Line,"Found_forwardslash")
                        continue
                    if Test[i]=='?':
                        append_to_csv(Line,"Found_Question_Mark")
                        continue
                    if Test[i]=='*':
                        append_to_csv(Line,"Found_star")
                        continue
                    if Test[i]=='>':
                        append_to_csv(Line,"Found_curveBrace")
                        continue
                    if all_problem.__contains__(Test[i]): 
                        key=Test[i]
                        value=all_problem[key]
                        append_to_csv(Line,value)
                        
                    else:
                        no_of_prob=no_of_prob+1
                        key=Test[i]
                        value=str(no_of_prob)
                        all_problem[key] =value
                        First_passenger="About:"+Test[i]
                        First_passenger=list(First_passenger)# good to use this line 
                        append_to_csv(First_passenger,value)
                        append_to_csv(Line,value)
                        

                    #append_to_csv(Line,char)             
        if Flag==0:
            append_to_csv(Test,"Found_Normal")
             
#####third pard ,creating a text or csv file where we keep all sysmbol and there corresponding file index 

for key,value in all_problem.items():
    data=str(key)+" "+str(value)
    #append_to_csv([key,value],"ALL_SYMBOLS")#Csv
    append_to_csv([data],"ALL_SYMBOLS")#txt