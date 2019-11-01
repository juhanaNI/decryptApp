filepath = 'kaikkisanat.txt'
lines = [line.rstrip('\n') for line in open(filepath)]
print(lines)
print('öljypohjainen' in lines)
