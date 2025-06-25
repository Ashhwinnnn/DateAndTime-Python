import datetime

str_date=input('Enter date in DD-MM-YYY: ')
d,m,y= str_date.split('-')

d1=datetime.date(int(y),int(m),int(d))
first_day=datetime.date(int(y),1,1)

diff=d1-first_day

print('Day number: ', diff.days+1)