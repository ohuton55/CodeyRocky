from ntpdatetime import now
ntp_now, fetched = now()
print(ntp_now.strftime('%d-%m-%Y %H:%M:%S'))
