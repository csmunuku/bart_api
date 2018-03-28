# bart_api
Scripts to read data from BART API in JSON Format using Default API Key.
---
### BSA:
http://api.bart.gov/api/bsa.aspx?cmd=count&key=MW9S-E7SL-26DU-VV8V&json=y
http://api.bart.gov/api/bsa.aspx?cmd=elev&key=MW9S-E7SL-26DU-VV8V&json=y
---
### Station List:
Station Name, Abbreviation, Addresses and Latitude, Longitude Info
http://api.bart.gov/api/stn.aspx?cmd=stns&key=MW9S-E7SL-26DU-VV8V&json=y
---
### Station Detailed Info:
More detailed Station Info
http://api.bart.gov/api/stn.aspx?cmd=stninfo&orig=DUBL&key=MW9S-E7SL-26DU-VV8V&json=y
Requests detailed information how to access the specified station as well as information about the neighborhood around the station.
Specifies whether the legend information should be included.
By default it is 0 (not shown), but can be turned on by setting it to 1. (Optional)
http://api.bart.gov/api/stn.aspx?cmd=stnaccess&orig=DUBL&key=MW9S-E7SL-26DU-VV8V&json=y&l=0
http://api.bart.gov/api/stn.aspx?cmd=stnaccess&orig=DUBL&key=MW9S-E7SL-26DU-VV8V&json=y&l=1
---
### ETD:
Requests Estimated Departure Time (ETD) for specified station.
http://api.bart.gov/api/etd.aspx?cmd=etd&orig=ALL&key=MW9S-E7SL-26DU-VV8V&json=y
http://api.bart.gov/api/etd.aspx?cmd=etd&orig=DUBL&direction=%s&key=MW9S-E7SL-26DU-VV8V&json=y
http://api.bart.gov/api/etd.aspx?cmd=etd&orig=DUBL&platform=2&direction=South&key=MW9S-E7SL-26DU-VV8V&json=y
http://api.bart.gov/api/etd.aspx?cmd=etd&orig=DUBL&platform=2&key=MW9S-E7SL-26DU-VV8V&json=y
http://api.bart.gov/api/etd.aspx?cmd=etd&orig=DUBL&platform=2&direction=%s&key=MW9S-E7SL-26DU-VV8V&json=y
---
### Route Info:
Requests detailed information current routes.
http://api.bart.gov/api/route.aspx?cmd=routes&key=MW9S-E7SL-26DU-VV8V&json=y
http://api.bart.gov/api/route.aspx?cmd=routes&date=today&key=MW9S-E7SL-26DU-VV8V&json=y
http://api.bart.gov/api/route.aspx?cmd=routes&sched=%s&key=MW9S-E7SL-26DU-VV8V&json=y
---
### Route Info:
Requests detailed information for a specific route.
http://api.bart.gov/api/route.aspx?cmd=routeinfo&route=11&key=MW9S-E7SL-26DU-VV8V&json=y
http://api.bart.gov/api/route.aspx?cmd=routeinfo&route=11&date=today&key=MW9S-E7SL-26DU-VV8V&json=y
http://api.bart.gov/api/route.aspx?cmd=routeinfo&route=11&sched=46&date=today&key=MW9S-E7SL-26DU-VV8V&json=y
---
### Schedules:
Requests detailed information about the current BART Schedules
http://api.bart.gov/api/sched.aspx?cmd=scheds&key=MW9S-E7SL-26DU-VV8V&json=y
---
### Holiday:
Requests information about the upcoming BART holidays, and what schedule will be run on those days.
http://api.bart.gov/api/sched.aspx?cmd=holiday&key=MW9S-E7SL-26DU-VV8V&json=y
---
### Special:
Requests information about the current and upcoming BART Special Schedules
http://api.bart.gov/api/sched.aspx?cmd=special&key=MW9S-E7SL-26DU-VV8V&json=y&l=1
---
### Schedule:
Requests detailed scheduled information for a specific station
http://api.bart.gov/api/stn.aspx?cmd=stnsched&orig=DUBL&key=MW9S-E7SL-26DU-VV8V&json=y
---
### Fare:
Requests the fare information for a trip between two stations.
http://api.bart.gov/api/sched.aspx?cmd=fare&orig=DUBL&dest=embr&date=today&key=MW9S-E7SL-26DU-VV8V&json=y
