from datetime import datetime

ut1 = datetime.now()

ut2 = datetime(year= ut1.year + 1, month=1, day=1)

ut3 = ut2 - ut1

print( f'今年はあと{ut3.days}日' )