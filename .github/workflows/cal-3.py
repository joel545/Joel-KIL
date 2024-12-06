import calendar

def print_calendar(year, month):
    """
    打印指定年份和月份的月曆

    :param year: 年份 (int)
    :param month: 月份 (int, 1-12)
    """
    try:
        if 1 <= month <= 12:
            cal = calendar.TextCalendar()
            print(cal.formatmonth(year, month))
        else:
            print("月份必須在1到12之間")
    except Exception as e:
        print(f"發生錯誤: {e}")

# 範例使用
year = int(input("請輸入年份: "))
month = int(input("請輸入月份: "))
print_calendar(year, month)