#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Name: Seth Weaver
# Part 1
# Remember wherever you see ??? you need to make a substitution.

import csv, requests # Yes, you can use "," to import multiple packages at once
from openpyxl import Workbook
from datetime import datetime


station_names = {} # Let's first define a blank dictionary, station name

# First we need to read in the data to create a dictionary for the station names and ids
# Your code for reading in a tab seperated file should go below here. See Example 4-1 and 4-2 as references.
with open('updated_station_name_id.txt','r') as file:
    reader = csv.DictReader(file, delimiter='\t')
    
    #Next we add the names from the file into the blank library station names
    for row in reader:
        station_names[row['station_id']] = row['station_name']


# Now we will work with the json data
# Call the json file from the given website. See Example 5-1.

# 'call' start

ImpJsonBikeData = 'CitiBikeData.json' # name of file which we will write in next line
#'Imp' abbreviation for import

OutJsonBikeData = open(ImpJsonBikeData, 'w') #opens the file that we named, and starts to write it
#'Out' appreviation for Output the output file we are writing

#I want to try to write my variables in the format
#(Abreviated action in filetype:)(.filetype)(Name)_(specific identifiers)
#As such, OutJsonBikeData is like saying Output a '.Json' named 'BikeData'

ImpTxtBikeData = requests.get('https://gbfs.citibikenyc.com/gbfs/en/station_status.json')
#this obtains the json we are wanting from the link contained in '...' using get()

# 'call' end

OutJsonBikeData.write(ImpTxtBikeData.text) #designates the program to write the data from 'ImpTxtBikeData' into the OutJsonBikeData

# "['data']['stations']" is a nested dictionary
data = ImpTxtBikeData.json()['data']['stations']

# Now we create the list of information
# For this part of the code provide an explanation in the comment box below regarding what the lines of code are doing
station_data = []
for station in data:
    station_id = station['station_id']
    station_name = station_names.get(station_id, 'Unknown Station')
    bikes = station.get('num_bikes_available', 0)
    e_bikes = station.get('num_ebikes_available', 0)
    scooters = station.get('num_scooters_available', 0)
    station_data.append((station_name, bikes, e_bikes, scooters))

station_data.sort(key=lambda x: x[0])

''' These dashed lines open a comment block. 

the for loop goes through the libary we defined on line 10 
in the data variable (the imported txt bike data,) looks at every station
then, it makes each station's 'ID' a variable in a list. 
Then it looks through every station name in imported bike data txt file, and finds the respective station id.
    for ex, it looks at some random row, then reads the row and matches that name to the id (the other column) in that row.
then it goes through each station in the json and reads the 'chunk' of information in that station

    for ex, one station looks like:
         "stations": [
      {
        "eightd_has_available_keys": false,
        "num_bikes_disabled": 0,
        "num_bikes_available": 18,
        "station_id": "16e70b05-5b73-4930-9dcf-f79e5ce9eaf5",
        "num_ebikes_available": 3,
        "is_installed": 1,
        "is_returning": 1,
        "num_scooters_available": 0,
        "num_scooters_unavailable": 0,
        "legacy_id": "4422",
        "num_docks_available": 5,
        "last_reported": 1738950207,
        "num_docks_disabled": 0,
        "is_renting": 1
      },
as it reads the chunk of text, we created several key/value pairs, specifically the available: bikes, e-bikes, and scooters.
    (right terminology? otherwise i would say "variables, then assigns the numeric value
      associated with the variable in that 'chunk' of json information)
once it has collected this information from the 'chunk', it then appending it in the order we listed.

I learned that, like matlab (i believe) python starts with numeric value 0, rather than one. So,
the last line sorts all of the information into the first column of the information we appended (by alphebetical order).
(better explained as if it was an array,
    that is, we make an array storing the information of the station name as a string in possition 0,
            we then store the available bikes, available e-bikes, and available scooters, in the ray (in that order, as such
            it is in the order of bikes as the '1' element, the e-bikes as the '2' element, and the scooters as the '3' element
        so, a general array would be [0 1 2 3] = ['name' bike ebike scooter]

end explanation (finally)

'''

# Now print the station, bikecount, ebikecount and scootercount for the first 10 stations. 
# See Lab Assignment 02 for a hint
for station_name, bikes, e_bikes, scooters in station_data[:10]:
    print(f"{station_name}: {bikes}, {e_bikes}, {scooters}")


# In[103]:


# Part 2
# Note: the station_data is created in Part 1 already

wb = Workbook()
ws = wb.active
# Add headers that describe each of the columns
ws.append(["Station Name", "Available Bikes", "Available E-bikes", "Available Scooters"])  

# Turn your dataset from part 1 into the excelsheet
# Iterate over ___ and append each tuple as a row in the Excel sheet.
# This part is an application of Example 4-5 
for row in station_data:
    ws.append(row)  

# This part is from Example 7-5 so most is filled out alread for you
# Like we did in Part 1 provide an explanation of the code in the comment box below
filename = f"Citibike-{datetime.now().strftime('%Y-%m-%d')}.xlsx"

#I feel like this should be exported as a csv since it has ~2200 rows... but okay! 

wb.save(filename)

'''

I believe this is similar to the 'close' function when dealing with the csv library.
It creates a variable, and in that variable, we name it using two different functions.
first, we give it the contant name "citibike-"then, with the {}, we use the function to check the date and time right now
then, inside the {} the program inserts the date and time.


looking up what fstring is, it says that it is a formatted string, and, being inside the {}, we are able to create a variable that,
inside the variable, is another variable that also gets updated when ever the program runs!

'''
print(' ') #gets rid of text from '''


# In[ ]:




