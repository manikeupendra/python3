tel = {'jack': 4098, 'sape': 4139}
print(tel)
tel['guido'] = 4127
print(tel)

print(tel['jack'])


del tel['sape']
print(tel)
tel['irv'] = 4127
print(tel)


list(tel)
print(tel)

sorted(tel)
print(tel)

print('guido' in tel)

print('jack' not in tel)