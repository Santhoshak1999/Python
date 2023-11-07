from  datetime import date
f_date = date(2013, 12, 22)
s_date = date(2014, 1, 1)

delta = s_date - f_date
print(delta.days)

