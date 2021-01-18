genome = input().upper()
a = (genome.count('C')+genome.count('G'))
b = len(genome)
x = (a/b)*100
print(x)