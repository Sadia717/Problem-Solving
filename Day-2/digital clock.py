from datetime import datetime
import pytz

a= pytz.timezone('ASia/Kolkata')
b= datetime.now(a)
print(b)
