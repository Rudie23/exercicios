import calendar


def CalendarText():
    calendartext = calendar.TextCalendar(calendar.SUNDAY)
    txtcalendar = calendartext.formatmonth(2022, 6)
    print(txtcalendar)


CalendarText()


def CalendarHTML():
    calendarhtml = calendar.HTMLCalendar(calendar.SUNDAY)
    htmlcalendar = calendarhtml.formatmonth(2022, 6)
    print(htmlcalendar)


CalendarHTML()