import datetime

with open ('test.txt', 'a') as f:
    start_time = datetime.datetime.now()
    summary = 0
    for x in range(20):
        summary += x ** 2 ** 2
    f.write(f'{summary} \n')
    print(summary)
    fin_time = datetime.datetime.now()
print('Старт:', start_time)
print('Окончание:', fin_time)
print("Потрачено времени: %s секунд" % (fin_time - start_time))
