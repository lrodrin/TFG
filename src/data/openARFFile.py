file = open('weather.arff')

for line in file.readlines():
    print(line)

file.close()