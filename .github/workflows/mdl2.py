import cal2 as cal
yr1 = int(input("請輸入年份: "))
mn1 = int(input("請輸入月份: "))
if 1 <= mn1 <= 12:
    cal.prtcal(yr1,mn1)
    #cal = calendar.TextCalendar()
    #print(cal.formatmonth(year, month))
else:
    print("月份必須在1到12之間")