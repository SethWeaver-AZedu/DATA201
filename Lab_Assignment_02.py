#!/usr/bin/env python
# coding: utf-8

# # Citibike Data
# 
# New York City has a bike rental program called Citibike sponsored by Citibank and Lyft. There are bike rental stations scattered throughout the city. The goal of this assignment is to create a function to count the number of Citibike trips originating at each station in January 2024. 
# 
# ## Instructions 
# To get started, download the Citi Bike trip data for January 2024. You can find the data in D2L titled *citibike_tripdata.csv*. This data originally was obtained from [https://s3.amazonaws.com/tripdata/JC-202401-citibike-tripdata.csv.zip](https://s3.amazonaws.com/tripdata/JC-202401-citibike-tripdata.csv.zip).
# 
# 1. Write a python function which reads the CSV file, and outputs the number of rides originating at each station. Call your function **bike_counts()**.
#    * The example given at the end of Chapter 2 in *Practical Python Data Wrangling and Data Quality* will help you get started.
# 2. Test your function using the Citbike Trip data (csv file that you downloaded).
#    * Your output list should be in alphabetical order, and each line of your output should have the form “station_name: number_of_rides.”  
#    * Below is a truncated example of what the output should look like
# 3. Submit your assignment to Gradescope. Your submission must include:
#    * A standalone `Python` file, named **Lab_Assignment_02**, containing your code. This must be a `.py` file containing only comments and `python` code.
#      * **Do not submit a Jupyter notebook**.
#    * The Citibike trip data, named **citibike_tripdata.csv**.
#    * **Note:** These must be uploaded as a .zip file.
#      * To zip your files, select both files by holding down cmd(mac)/ctrl(pc) and click on both files. Then right click on the files and click compress(mac)/zip(pc).
# 
# You code will be graded on the following criteria: 
# 
# - Programming style: Your code should be well documented and clearly structured. All variables and functions should be given descriptive names. You should include enough comments in your code that a colleague or fellow student understands what each function does and can follow the logic of your code. On the other hand, be sure your code does not contain any extraneous comments left over from idle or a Jupyter notebook. 
# - Your code must give the correct output when run in the same directory with the CSV file. 
# - The output must be in the same order and format as the example below. Be sure your code does not produce any other output. Be sure to properly handle any “bad data.” 
# 
# ## Partial Expected Output 
# 
# **Note**: There is one row with blank station name.
# 
# ```{python}
# : 1
# 11 St & Washington St: 947
# 12 St & Sinatra Dr N: 652
# 14 St Ferry - 14 St & Shipyard Ln: 692
# 2 St & Park Ave: 520
# 4 St & Grand St: 674
# 4 St & River St: 602
# 5 Corners Library: 130
# 6 St & Grand St: 590
# 7 St & Monroe St: 719
# 8 St & Washington St: 1006
# 9 St HBLR - Jackson St & 8 St: 719
# Adams St & 12 St: 267
# Adams St & 2 St: 771
# . 
# . 
# . 
# (…and so on….) 
# ```
# 

# In[185]:


# Name: Seth Weaver

import csv

def Bike_Counts(csv_file):
    source_file = open(csv_file, "r") 
    # I removed the quotation marks because it simply was NOT working, and the built in
    # ai told me it might work. read the variable inside the brackets (csv_value)
    
    ReadSource = csv.DictReader(source_file, delimiter=',') 
    #the thing missing was the .DictReader for the file we import into the variable 'csv_file'

    #The variable defined below sets up your new dictionary, where you will add the station 
    #names and counts as you iterate through the data.
    ride_counts = {}
        #ride_counts is the library used later for the 'if ... in ...' statement to store all 
        #the information
    
    ### Use the information found in Examples 2-15 to 2-19 in Chapter 2 of the textbook for 
    ### some hints about what should go inside here. 
        # this 'help' felt VERY DISTANTLY related... it felt like 
        # 'long ago, in a galaxy far, far away...'
  
    for row in ReadSource: #for every row read in the source_file, first:
        station = row["start_station_name"] 
        #Store any 'strings' in the 'start_station_name' column in the read csv as a name
        ##then, check:
        if station in ride_counts:     #if it is already stored,
            #if it is: incriment the count...... Was this the hint????
            ride_counts[station] = ride_counts[station] + 1 

        elif station == "" or None: #else form of if (elif)
            #check if the station name is a blank string or no value,
            
            continue  #if it is, skip the row (dont index it)
            
        else:
            ride_counts[station] = 1 #it wasnt, meaning it has some value, or is named, 
            # making us 'index' it into the libary

    sorted_stations = dict(sorted(ride_counts.items()))
    #s orts the ride_counts libary alphabetically (checking character by character, making it 
    # *somewhat* alphabetically)
    return(sorted_stations) # essentially 'closes out' the function we were defining, stopping
    # the function we were defining from 'collecting' more code for the function
    
station_counts = Bike_Counts('citibike_tripdata.csv') # essentially does two things
# first, Bike_Counts('citibike_tripdata.csv') essentially runs: 'csv_file = 'citibike_tripdata.csv'
# second, it takes the station_counts is made a variable, essentially 'shortcutting' us from 
# having to write Bike_Counts('citibike_tripdata.csv') several times

for i, (station, number) in enumerate(station_counts.items()): # makes the station_counts, our
    #'shortcut' for the user-defined function we made, and makes it an index with
    # the station and count (number of times station is mentioned) grouped together
    # i tried a few different things with 'value' such as count, and number... not quite sure
    # what the second part does if im not going to lie...
    if i >= 10:
        break

for station, number in station_counts.items():
    print(f"{station}: {number}") ##MUST match the previous stuff we defined, and it is important
# that we keep {station}: {something}


# In[ ]:




