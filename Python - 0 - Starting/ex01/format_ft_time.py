import datetime

today = datetime.datetime.now()
tmp = today.strftime("%b")

print(f"Seconds since January 1, 1970: {today.timestamp():,.4f} or {today.timestamp():.2e} in scientific notation\n{tmp} {today.day} {today.year}")