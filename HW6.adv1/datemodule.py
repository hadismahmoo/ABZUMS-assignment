def date(year,month,day):
    month=str(month)
    if len(month)==1:
        print(f"{year} - 0{month}- {day}")
    else:
        print(f"{year} - {month} - {day}")

