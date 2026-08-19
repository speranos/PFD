import datetime


today = datetime.datetime.now()

then = datetime.datetime(1970, 1, 1)

deff = today - then
print("Seconds since January 1, 1970:", deff.total_seconds(), " or " , format(deff.total_seconds(), ".2e"), " in scientific notation")

print(today.strftime("%b %d %Y"))