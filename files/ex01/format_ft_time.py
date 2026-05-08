import time
import datetime

timestamp = time.time()
dt = datetime.datetime.fromtimestamp(timestamp)

print(
    f"Seconds since January 1, 1970: {timestamp:,.4f}"
    f" or {timestamp:.2e} in scientific notation"
)
print(dt.strftime("%b %d %Y"))
