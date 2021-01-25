import requests
with open(r'C:\1\dataset_3378_2.txt', 'r') as f:
    line = f.readline().strip()
r = requests.get(line)
print(len(r.text.splitlines()))
