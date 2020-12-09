
own = open('unique_clean_data.txt', 'r', encoding='utf-8')
existing = open('ReUnique_Clean_Data_Jugantor_02.txt', 'r', encoding='utf-8')

vul_output = open('vulnerable_word_jugantor_02.txt', 'w', encoding='utf-8')
f1 = own.readlines()
f2 = existing.readlines()

OwnList = []
ExistingList = []
for line in f1:
    if line[-1]=='\n':
        OwnList.append(line[:-1])
    else:
        OwnList.append(line)

for line in f2:
    if line[-1]=='\n':
        ExistingList.append(line[:-1])
    else:
        ExistingList.append(line)


for i in ExistingList:
    if i not in OwnList:
        vul_output.write(i)
        vul_output.write('\n')





