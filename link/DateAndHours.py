from datetime import date, datetime


def DateHour():
    today = date.today()
    print('Hoje é:', today)
    print('Partes da data é', today.day, today.month, today.year)
    print('Número do dia da semana:', today.weekday())
    days = ['monday', 'tuesday', 'wedneday', 'thursday', 'friday', 'saturday', 'sunday']
    print('Name of the day of the week:', days[today.weekday()])

    date_time = datetime.now()
    print('Date and hour:', date_time)

    time_now = datetime.time(date_time)
    print('Currently hour:', time_now)


DateHour()
