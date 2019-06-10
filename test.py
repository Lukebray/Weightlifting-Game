dict = {'a':5, 'b':23, 'c':4}
maximum = max(dict, key=dict.get)
print(maximum)