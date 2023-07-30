from datetime import datetime
"""current_datetime=datetime.now()
print(current_datetime)"""
#using strftime function
current_datetime=datetime.now()
print(current_datetime)
edited_datetime=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(edited_datetime)