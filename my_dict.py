temper = {"city": "Москва", "temperature": "20"}
print(temper['city'])

temper['temperature']=str(int(temper["temperature"]) - 5)
print(temper)


print(temper.get('country', 'Russia'))
temper['date'] = '27.05.2019'
print(temper)
print(len(temper))