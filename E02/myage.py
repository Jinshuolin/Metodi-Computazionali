from datetime import datetime, timedelta
g = int (input ("Scrivere il giorno di nascita "))
m = int (input ("Scrivere il mese di nascita "))
y = int (input ("Scrivere l'anno di nascita "))
h = int (input ("Scrivere l'ora di nascita "))
M = int (input ("Scrivere il minuto di nascita "))
s = int (input( "Scrivere il secondo di nascita "))
mydate_str = None
if y >=1000:
    mydate_str = "{:}-{:}-{:} {}:{}:{}".format (g,m,y,h,M,s)
else:
    mydate_str = "{:}-{:}-000{:} {}:{}:{}".format (g,m,y,h,M,s)

mydate = datetime.strptime ( mydate_str,"%d-%m-%Y %H:%M:%S")
timediff = datetime.now() - mydate
datenow = datetime.now()
tot_years = datenow.year - mydate.year
print ("Hai vissuto", tot_years, "anni")
print ("Hai vissuto", timediff.days, "giorni")
print ("Hai vissuto", timediff.total_seconds(), "secondi")




