import json
import re

file = open('websiteData.txt', 'r+')

d = {}
human_email_count = 0
non_human_email_count = 0
for line in file:
    words = line.split(' ')
    for word in words:
        human_mail = re.findall(r"[a-z]+\.+[a-z]+@[\w.]+com", word)
        non_human_mail = re.findall(r"^[\w]{2,8}@[\w.]+com", word)
        if human_mail:
            human_email_count += 1
            d[human_mail[0]] = {'Occurrence': human_email_count, 'EmailType': 'Human'}

        if non_human_mail:
            non_human_email_count += 1
            d[non_human_mail[0]] = {'Occurrence': non_human_email_count, 'EmailType': 'Non-Human'}

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=4)