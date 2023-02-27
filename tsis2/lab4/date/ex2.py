from datetime import date, timedelta
print('Yesterday :', date.today() - timedelta(1))
print('Today :', date.today())
print('Tomorrow :', date.today() + timedelta(1))