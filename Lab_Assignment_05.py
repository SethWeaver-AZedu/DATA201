# %%
# Dictionary defining what each states abreviation is in 'long-form'
state_names = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas',
    'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware',
    'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho',
    'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas',
    'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi',
    'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada',
    'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York',
    'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma',
    'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah',
    'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia',
    'WI': 'Wisconsin', 'WY': 'Wyoming', 'DC': 'District of Columbia', 'AS': 'American Samoa',
    'GU': 'Guam', 'MP': 'Northern Mariana Islands', 'PR': 'Puerto Rico', 'VI': 'Virgin Islands'
}

# %%
import pandas as pd
import csv

'''
1. Read in the data 
2. Set up a new output file. 
    Note: this one should not be your final file, it is a transformation of the base data with an additional column of State
3. Create a new Header Row
4. Add the header row to the new file
5. Add the data to the dataset
    Note: We provide some assistance with pieces of this part.
'''

# Complete Steps 1 - 4 by using Example 7-10 as an outline. You will need to use BorrowerState and State instead of their column names

# 'Step 1' open as read, and dict read PPPData

PPPData = open('public_150k_plus_recent.csv','r')

PPPDataReader = csv.DictReader(PPPData)

# 'Step 2' open and write, and dict write AugPPPData (a new file we create)

AugPPPData = open('Aug_public_150k_plus_recent.csv', 'w')
AugPPPDataWriter = csv.writer(AugPPPData)
        
    # Create a new header row
HeaderRow = []
for item in PPPDataReader.fieldnames:
    HeaderRow.append(item)
    if item == 'BorrowerState':
        HeaderRow.append('States')

#now, write the expanded header row into our output file

AugPPPDataWriter.writerow(HeaderRow)

#Adding the data to the dataset
for row in PPPDataReader:
    if not row['BorrowerState']:
        continue
        
    new_row = []

    for column_name in PPPDataReader.fieldnames:
        new_row.append(row[column_name])

        if column_name == 'BorrowerState':
            State = state_names[row['BorrowerState']]
            new_row.append(State)
        
    AugPPPDataWriter.writerow(new_row)

PPPData.close()
AugPPPData.close()

# %% [markdown]
# ## Task 2 - Create the Table CSV File
# 
# **This code is similar to pieces of Lab 02**

# %%
''' (Read in the Data - See what you did in step 1 above (similar to lab 2))
 in lab 2, we imported the csv file we were using, then using the csv.dictreader(file,delimiter=','), read the rows of the source file

then, creating a dictionary to store key:value pairs which are gathered later on in a for loop
then, read through each row storing the key:value from row entry and iterate through each row, and save only the rows with entries. This functionally counts the number of loans issued to a specific state. 

after this, the code is setup to then count the number of loans in a specific range of monetary value (defined in assignment instructions) 

'''

# %%
'''
In this part we will create a dictionary that we can then write into a csv file. 
These are the steps that we will follow:

1. Create the dictionary
2. Iterate through the dataset row by row and increase counts for each category as appropriate.
    - We look at the State and Current Approval Amount for loans
'''
# Read the augmented data
source_file = open('Aug_public_150k_plus_recent.csv', 'r')

stateloans_reader = csv.DictReader(source_file)
    
# Initialize the dictionary to store loan data by state
stateloans = {}

for row in stateloans_reader:
    state = row['States']
    loan = float(row['CurrentApprovalAmount'])

    #Check to see if the state is already in dictionary. If it is not, create a new dictionary for the particular state
    if state not in stateloans:
        stateloans[state] = { #this pretty much initializes the states values for each column we are interested in.
                'Total': 0,
                '$150K - $350': 0,
                '$350k - $1m': 0,
                '$1m - $2m': 0,
                '$2m - $5m': 0,
                '$5m - $10m': 0,
                'Other': 0
            }

    #Now increase the overall total counter
    stateloans[state]['Total'] +=1

    #Now increase the particular loan category counter by going through and checking the value of the loan column, and increment the number of times a condiction was satisfied, and store the total incriments in the respective category
    if (150*10**3) <= loan < (350*10**3):
        stateloans[state]['$150K - $350'] += 1
    elif (350*10**3) <= loan < (10**6):
        stateloans[state]['$350k - $1m'] += 1
    elif (10**6) <= loan < (2*10**6):
        stateloans[state]['$1m - $2m'] += 1
    elif (2*10**6) <= loan < (5*10**6):
        stateloans[state]['$2m - $5m'] += 1
    elif (5*10**6) <= loan < (10*10**6):
        stateloans[state]['$5m - $10m'] += 1
    else:
        stateloans[state]['Other'] += 1
    

# %%
# Setting up the output files (See beginning of Example 7-1)
output_file = open('LoansByState.csv','w') #open a new file (the required output csv file, named LoansByState.csv) in a write mode (aka create a new file)

#Setting up the headers
new_fieldnames = ['State', 'Total', '$150K - $350', '$350k - $1m', '$1m - $2m', '$2m - $5m', '$5m - $10m','Other'] #this is the order of the columns in the desired output table example
output_writer = csv.DictWriter(output_file, fieldnames = new_fieldnames) # prepare the filednames to be written into the output file, 
output_writer.writeheader() #then, acutally  write the filednames to the output file

# %%
'''
for every row in the state column in the stateloans dictionary, then sort the strings in the state column (the key!) and returns a dictionary with the keys being states, and the values being the total loans from a state, and the remaining colums as values for the key:value pairs. then, combine them into a singular row and update the total values for each state row by writing the rows with the defined dictionary (line 5 "row = {'State': state}")
'''
for state in sorted(stateloans.keys()):
    row = {'State': state}  
    row.update(stateloans[state])
    output_writer.writerow(row)


# %%
#Closing the output file
output_file.close()
source_file.close()



# %%
