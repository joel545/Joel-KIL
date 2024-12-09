import cal2 as cal

counter=0
while (counter<=0):
    print('=' * 10,"請輸入要顯示該月月曆的年月",'=' * 10)
    yr1 = int(input("請輸入年份: "))
    mn1 = int(input("請輸入月份: "))
    if 1 <= mn1 <= 12:
        cal.prtcal(yr1,mn1)
        counter=counter+1
        #cal = calendar.TextCalendar()
        #print(cal.formatmonth(year, month))
    else:
        print("月份必須在1到12之間，請重新輸入")