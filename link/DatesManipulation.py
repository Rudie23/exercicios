from datetime import date


def daysleft(year, month, day):
    today = date.today()
    wanted_date = date(year, month, day)

    days = wanted_date - today

    msgreturn = 'Left ' + str(days).replace('days, 0:00:00', '') + 'days to the date ' + wanted_date.strftime('%d/%m/%y')

    print(msgreturn)


daysleft(2022, 9, 23)