import json
import re

file = open('websiteData.txt', 'r+')

d = {}
human_email = []
non_human_email = []
for line in file:
    words = line.split(' ')
    for word in words:
        human_mail = re.findall(r"[a-z]+\.[a-z0-9]+@[\w]+\.[a-z]{2,3}", word)
        non_human_mail = re.findall(r"^[\w]{2,8}@[\w]+\.[a-z]{2,3}", word)
        if human_mail:
            human_email.append(human_mail[0])

        if non_human_mail:
            non_human_email.append(non_human_mail[0])

human = list(set(human_email))
non_human = list(set(non_human_email))
index = 0
for i in human:
    d[i] = {"Occurrence": human_email.count(i), "EmailType": "Human"}
    index += 1

for i in non_human:
    d[i] = {"Occurrence": non_human_email.count(i), "EmailType": "Non-Human"}
    index += 1

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=4)