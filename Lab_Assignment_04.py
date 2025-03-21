    # %%
# Name: Seth Weaver
# Remember wherever you see ??? you need to make a substitution.

import pandas as pd


# See Example 6-1 for a hint
ppp_data = pd.read_csv('public_150k_plus_recent.csv')

# Next we will work with accessing the lenders
ppp_data['ServicingLenderName'] = ppp_data['ServicingLenderName'].str.strip()


'''
the line above is saying to change the column named 'ServiceLenderName' and to change that row with the same row (like saying ppp['row1'] = ppp['row1'].SomeChangeFunction()) by the function .str.strip(). This function goes into the column and gets rid of any 'extra' whitespace that you'd have before or after the string. This is a form of cleaning by making sure all of the values have a consistent formatting.
'''

# Continue with the lenders
# woahhhh i knew what to do here almost instantly for once woahhh

lenders_list = sorted(ppp_data['ServicingLenderName'].dropna().unique())

'''
this is number 2 in the outline.

sorted() is a function that sorts a list in ascending order. this creates a list and sorts it by the unique values in the column 'ServicingLenderName' in the ppp_data dataframe, then removes any missing values, and makes entries for each unique name. This may be problematic if someone mispelled the name of the lender, or if someone accidentally typed something in wrong. This step is also a form of cleaning
'''

# Print a list of the first 10 lenders
for lenders in lenders_list[:10]:
    print(lenders_list)

# Now we will move onto the loan type for each lender
lenders_loan_data = ppp_data.groupby(['ServicingLenderName','LoanStatus']).size()

print(lenders_loan_data[:10])

'''
this is outline of #3

we then group the data in a series (essentially a data frame with a value paired to its respective key (item in the column)) from values in the 'ServicingLenderName' column and the 'LoanStatus' column (with the ServicingLenderName being the key, and LoanStatus being the value). size() is a function that counts the number of times the pair of values is referenced in the data set.

'''

# Finally we will put it all together so you can write out the csv file
lenders_loan_state_data = ppp_data.groupby(['BorrowerState','ServicingLenderName','LoanStatus']).size().unstack(fill_value=0) # 

lenders_loan_state_data.reset_index(inplace=True)

lenders_loan_state_data = lenders_loan_state_data.sort_values(by=['BorrowerState', 'ServicingLenderName'])

'''

outline number 4!

this takes the ppp_data dataframe and creates essentially two columns with the 'BorrowerState', 'ServicingLenderName', and 'LoanStatus'. then, it sizes (essentially counts) the number of references a row is referenced in the data set 
    (Rewording the last sentance, it looks through the rows, counts the number of rows that exactly match eachother in the borrowerstate, servicinglendername, and loanstatus columns, and then creates a new column with the count of each row's number of references) 

then it uses the unstack function to take the 'LoanStatus' (as it is the very last column in the groupby function (therefore, i think of it as the last column has the lower heiarchy)) and makes each unique value in the 'LoanStatus' column a new column, with the number of times a unique 'loanstatus' was referenced in the column. (which i believe the number of times the exact row combination was referenced is its own column)
    (rewording again, it looks through the newly grouped dataframe, and, since loan status has different possible strings, it breaks the loan status column into a column for each string found in the column, then lables the column with then name it found (such as exempt 4), and the number of times it was that specific loan status (and therefore, exact row combination) is the the dataframe)

    finally, if there was no reference to a specific loan status, it fills the column with a 0.

    the line underneith it clears the index of the dataframe and tells python to do it in place (so it doesn't create a copy of the dataframe)

    finally, the last line sorts the dataframe by the 'BorrowerState' and 'ServicingLenderName' columns, which will make our data frame be in the order of state, bank, then the unique types of loan statuses.    
    '''

#this reads the dataframe, and goes to the column named 'ServicingLenderName' and renames it to the thing that we put after the colon. if the inplace=false the function would tell the csv file to (essentially) create a copy of the renamed 'ServicingLenderName' column which would result in in the original column still being there. SO, with inplace=True, it tells the csv file to replace the original column with the renamed column.


# Last we write the file to the csv

#this was the easiest part???????????? what?????????

output_file = 'LoanStatusByBank.csv'

lenders_loan_state_data.to_csv(output_file, index=False) #we then convert the stored variable (dataframe) lenders_loan_state_data to a csv with the .to_csv, and what the name of the file is going to be (output_file) and the index=False is to tell the csv file not to include the index column.


print(f"File '{output_file}' creation...Done") #tells us the operation above was completed.

# %%
print(lenders_loan_state_data.head(20).to_string(index=False)) #for my own personal sanity to see the output more cleanly


# %%



