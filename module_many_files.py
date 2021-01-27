import requests
with open(r'C:\1\dataset_3378_3.txt', 'r') as f:
    line = f.readline().strip()
r = requests.get(line)
for name in r:
    while 'We' not in r.text:
        r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r.text)
        print(r.text)